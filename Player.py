from pico2d import *
import lobby
import converter

import game_framework


class Player:
    Image_init = None
    TIME_PER_ACTION = 0.2
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self):
        self.x = 150
        self.y = 240
        self.sum_x = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.frame = 0.0
        self.total_frames = 0.0
        self.hp_frame = 0.0
        self.hpsize = 0.0
        self.hpmove = 0
        self.big_time = 0
        self.hp_time = 0
        self.dead_time = 0
        self.state = "Run"
        self.power = False
        self.big = False
        self.bool_hp = False
        self.bool_dead = False
        self.back_lobby = False
        self.score = 0
        self.dead_count = 0
        self.result_count = 0
        ######사운드#####
        self.bgm = load_music('Sound\\Stage1.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

        self.jump_sound = load_wav('Sound\\jump.wav')
        self.jump_sound.set_volume(64)

        self.slide_sound = load_wav('Sound\\slide.wav')
        self.slide_sound.set_volume(64)

        self.giant_jump_start_sound = load_wav('Sound\\g_giantjump.wav')
        self.giant_jump_start_sound.set_volume(64)

        self.giant_jump_end_sound = load_wav('Sound\\g_giantland.wav')
        self.giant_jump_end_sound.set_volume(128)

        self.dead_sound = load_wav('Sound\\g_end.wav')
        self.dead_sound.set_volume(128)

        self.result_sound = load_wav('Sound\\r_score.wav')
        self.result_sound.set_volume(128)

        if Player.Image_init == None:
            self.run_cookie = load_image('Image\\stage1_cookie\\cookie_run.png')
            self.slide_image = load_image('Image\\stage1_cookie\\cookie_run_slide.png')
            self.jump_image_first = load_image('Image\\stage1_cookie\\cookie_run_jump2.png')
            self.jump_image_second = load_image('Image\\stage1_cookie\\cookie_run_jump.png')
            self.run_cookie_collid = load_image('Image\\stage1_cookie\\cookie_run_collid2.png')
            self.run_cookie_big = load_image('Image\\stage1_cookie\\cookie_run_big.png')
            self.slide_image_big = load_image('Image\\stage1_cookie\\cookie_run_slide_big.png')
            self.jump_image_first_big = load_image('Image\\stage1_cookie\\cookie_run_jump2_big.png')
            self.jump_image_second_big = load_image('Image\\stage1_cookie\\cookie_run_jump_big.png')
            self.dead_cookie = load_image('Image\\stage1_cookie\\cookie_run_dead.png')
            self.big_icon = load_image('Image\\big_icon.png')
            self.hp_icon = load_image('Image\\hp_icon.png')
            #score 이미지 저장
            self.jelly = load_image('Image\\item_jelly.png')
            self.one = load_image('Image\\Number\\1.png')
            self.two = load_image('Image\\Number\\2.png')
            self.three = load_image('Image\\Number\\3.png')
            self.four = load_image('Image\\Number\\4.png')
            self.five = load_image('Image\\Number\\5.png')
            self.six = load_image('Image\\Number\\6.png')
            self.seven = load_image('Image\\Number\\7.png')
            self.eight = load_image('Image\\Number\\8.png')
            self.nine = load_image('Image\\Number\\9.png')
            self.zero = load_image('Image\\Number\\0.png')
            self.result = load_image('image\\result.png')
            self.result_ok = load_image('image\\result_ok.png')
            self.result_ok_click = load_image('image\\result_ok_click.png')
            #체력 이미지 저장
            self.hp = load_image('Image\\hp.png')

        self.dir = "Right"
        self.jump = 0
        self.jump_gravity = 0

    def __del__(self):
        self.total_frames
        self.hp_frame
        self.hpsize
        self.hpmove

    def update(self, frame_time, hpsize):
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.hp_frame += self.total_frames
        print(int((self.hp_frame) / 5000) + self.hpmove)
        self.hpsize = int((self.hp_frame) / 5000) + self.hpmove + hpsize
        self.frame = int(self.total_frames) % 6
        self.gravity()
        #print(self.total_frames)
        if self.hpsize >= 500:
            self.state = "Dead"
            self.frame = 0
            if self.dead_count == 0:
                self.dead_sound.play()
                self.dead_count += 1

        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Dead":
            if self.hpsize > 510:
                self.bool_dead = True
            self.frame = (self.frame +1) % 4
        elif self.state == "Jump" and self.state == "Slide":
            self.power = True
            self.frame = 0
        elif self.state == "Jump" and self.y <= 250:
            self.state = "Run"
        elif self.state == "Jump_Big" and self.y <= 250:
            self.giant_jump_end_sound.play()
            self.state = "Big"

        elif self.state == "Big" or self.state == "Slide_Big" or self.state == "Jump_Big":
            if self.big_time + 100 < self.total_frames:
                self.state = "Run"
                if self.big_time + 50 < self.total_frames:
                    self.big = False
                    self.big_time = 0

            if self.hp_time + 50 < self.total_frames:
                self.bool_hp = False
                self.hp_time = 0

        #elif self.state == "Collid":
            #self.power = True
            #if self.total_frames > self.total_frames + 10:
                #self.state = "Run"


    def get_bb(self):
        if self.state == "Run":
            return self.x - 20, self. y - 35, self.x + 20, self.y + 43
        elif self.state == "Slide":
            return self.x - 20, self. y - 35, self.x + 20, self.y - 15
        elif self.state == "Jump":
            return self.x - 20, self. y - 35, self.x + 20, self.y + 43
        elif self.state == "Big":
            return self.x - 130, self. y - 30, self.x + 130, self.y + 150
        elif self.state == "Jump_Big":
            return self.x - 130, self. y - 30, self.x + 130, self.y + 150
        elif self.state == "Slide_Big":
            return self.x - 130, self. y - 30, self.x + 130, self.y + 100

        '''if self.state == "Run":
            return self.x - 32, self. y - 43, self.x + 32, self.y + 43
        elif self.state == "Slide":
            return self.x - 32, self. y - 43, self.x + 32, self.y
        elif self.state == "Jump":
            return self.x - 32, self. y - 43, self.x + 32, self.y + 43'''

        return self.x - 32, self. y - 43, self.x + 32, self.y + 43

    #def draw_bb(self):
        #draw_rectangle(*self.get_bb())


    def gravity(self):
        if (self.y - 45 - self.jump_gravity) > 195:
            self.jump_gravity += 2
            self.y -= self.jump_gravity / 2
        else:
            self.y = 240
            self.jump_gravity = 0

    def draw(self):
        if self.state == "Run":
            self.run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y)
        elif self.state == "Slide":
            self.slide_image.draw(self.x, self.y - 17)
        elif self.state == "Jump":
            if self.jump % 2 == 1:
                self.jump_image_first.draw(self.x, self.y)
            elif self.jump % 2 == 0:
                self.jump_image_second.draw(self.x, self.y)


        elif self.state == "Big":
            self.run_cookie_big.clip_draw(self.frame * 300, 0, 300, 348, self.x, self.y + 130)
            if self.big_time + 20 > self.total_frames:
                self.big_icon.draw(400, 400)

        elif self.state == "Slide_Big":
            self.slide_image_big.draw(self.x, self.y + 50)
            if self.big_time + 20 > self.total_frames:
                self.big_icon.draw(400, 400)

        elif self.state == "Jump_Big":
            if self.jump % 2 == 1:
                self.jump_image_first_big.draw(self.x, self.y + 130)
                if self.big_time + 20 > self.total_frames:
                    self.big_icon.draw(400, 400)
            elif self.jump % 2 == 0:
                self.jump_image_second_big.draw(self.x, self.y + 130)
                if self.big_time + 20 > self.total_frames:
                    self.big_icon.draw(400, 400)

        elif self.state == "Collid":
            self.run_cookie_collid.clip_draw(self.frame * 53, 0, 53, 81, self.x, self.y)

        elif self.state == "Dead":
            if self.frame >= 4:
                self.frame = 4
            self.dead_cookie.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y + 10)



        if self.bool_dead == True and self.result_count == 0:
            self.bgm.stop()
            self.result_sound.play()
            self.result_count += 1
        if self.bool_dead == True:
            self.result.draw(400, 400)
            if self.mouse_x > 354 and self.mouse_x < 446 and self.mouse_y > 259 and self.mouse_y < 291:
                self.result_ok_click.draw(400, 275)
            else:
                self.result_ok.draw(400 ,275)

            if converter.player_money % 10 == 0:
                self.zero.draw(460, 440)
            elif converter.player_money % 10 == 1:
                self.one.draw(460, 440)
            elif converter.player_money % 10 == 2:
                self.two.draw(460, 440)
            elif converter.player_money % 10 == 3:
                self.three.draw(460, 440)
            elif converter.player_money % 10 == 4:
                self.four.draw(460, 440)
            elif converter.player_money % 10 == 5:
                self.five.draw(460, 440)
            elif converter.player_money % 10 == 6:
                self.six.draw(460, 440)
            elif converter.player_money % 10 == 7:
                self.seven.draw(460, 440)
            elif converter.player_money % 10 == 8:
                self.eight.draw(460, 440)
            elif converter.player_money % 10 == 9:
                self.nine.draw(460, 440)

            if int(converter.player_money / 10) % 10 == 0:
                self.zero.draw(400, 440)
            elif int(converter.player_money / 10) % 10 == 1:
                self.one.draw(400, 440)
            elif int(converter.player_money / 10) % 10 == 2:
                self.two.draw(400, 440)
            elif int(converter.player_money / 10) % 10 == 3:
                self.three.draw(400, 440)
            elif int(converter.player_money / 10) % 10 == 4:
                self.four.draw(400, 440)
            elif int(converter.player_money / 10) % 10 == 5:
                self.five.draw(400, 440)
            elif int(converter.player_money / 10) % 10 == 6:
                self.six.draw(400, 440)
            elif int(converter.player_money / 10) % 10 == 7:
                self.seven.draw(400, 440)
            elif int(converter.player_money / 10) % 10 == 8:
                self.eight.draw(400, 440)
            elif int(converter.player_money / 10) % 10 == 9:
                self.nine.draw(400, 440)

            if int(converter.player_money / 100) == 0:
                self.zero.draw(340, 440)
            elif int(converter.player_money / 100) == 1:
                self.one.draw(340, 440)
            elif int(converter.player_money / 100) == 2:
                self.two.draw(340, 440)
            elif int(converter.player_money / 100) == 3:
                self.three.draw(340, 440)
            elif int(converter.player_money / 100) == 4:
                self.four.draw(340, 440)
            elif int(converter.player_money / 100) == 5:
                self.five.draw(340, 440)
            elif int(converter.player_money / 100) == 6:
                self.six.draw(340, 440)
            elif int(converter.player_money / 100) == 7:
                self.seven.draw(340, 440)
            elif int(converter.player_money / 100) == 8:
                self.eight.draw(340, 440)
            elif int(converter.player_money / 100) == 9:
                self.nine.draw(340, 440)
            #self.bool_dead = False

        if self.bool_hp == True:
            if self.hp_time + 20 > self.total_frames:
                self.hp_icon.draw(400, 400)

        '''if self.state == 'Jump_Big' and self.y <= 251:
                             self.giant_jump_end_sound.play()'''


        ###score부분
        if converter.player_money % 10 == 0:
            self.zero.draw(750, 750)
        elif converter.player_money % 10 == 1:
            self.one.draw(750, 750)
        elif converter.player_money % 10 == 2:
            self.two.draw(750, 750)
        elif converter.player_money % 10 == 3:
            self.three.draw(750, 750)
        elif converter.player_money % 10 == 4:
            self.four.draw(750, 750)
        elif converter.player_money % 10 == 5:
            self.five.draw(750, 750)
        elif converter.player_money % 10 == 6:
            self.six.draw(750, 750)
        elif converter.player_money % 10 == 7:
            self.seven.draw(750, 750)
        elif converter.player_money % 10 == 8:
            self.eight.draw(750, 750)
        elif converter.player_money % 10 == 9:
            self.nine.draw(750, 750)

        if int(converter.player_money / 10) % 10 == 0:
            self.zero.draw(717, 750)
        elif int(converter.player_money / 10) % 10 == 1:
            self.one.draw(717, 750)
        elif int(converter.player_money / 10) % 10 == 2:
            self.two.draw(717, 750)
        elif int(converter.player_money / 10) % 10 == 3:
            self.three.draw(717, 750)
        elif int(converter.player_money / 10) % 10 == 4:
            self.four.draw(717, 750)
        elif int(converter.player_money / 10) % 10 == 5:
            self.five.draw(717, 750)
        elif int(converter.player_money / 10) % 10 == 6:
            self.six.draw(717, 750)
        elif int(converter.player_money / 10) % 10 == 7:
            self.seven.draw(717, 750)
        elif int(converter.player_money / 10) % 10 == 8:
            self.eight.draw(717, 750)
        elif int(converter.player_money / 10) % 10 == 9:
            self.nine.draw(717, 750)

        if int(converter.player_money / 100) == 0:
            self.zero.draw(684, 750)
        elif int(converter.player_money / 100) == 1:
             self.one.draw(684, 750)
        elif int(converter.player_money / 100) == 2:
            self.two.draw(684, 750)
        elif int(converter.player_money / 100) == 3:
            self.three.draw(684, 750)
        elif int(converter.player_money / 100) == 4:
            self.four.draw(684, 750)
        elif int(converter.player_money / 100) == 5:
            self.five.draw(684, 750)
        elif int(converter.player_money / 100) == 6:
            self.six.draw(684, 750)
        elif int(converter.player_money / 100) == 7:
            self.seven.draw(684, 750)
        elif int(converter.player_money / 100) == 8:
            self.eight.draw(684, 750)
        elif int(converter.player_money / 100) == 9:
            self.nine.draw(684, 750)

        self.jelly.draw(651, 750)


        #hp바 구현
        self.hp.clip_draw(self.frame * 10, 0, 500 - int(self.hpsize), 36, 300 - int(self.hpsize / 2), 750)
        #self.run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y)
        #print(self.hpsize)
            #self.run_cookie_collid.draw(self.x, self.y)
        #self.run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y + 200, 500, 500)


    def handle_events(self, event):
            events = get_events()

            if event.type == SDL_QUIT:
                game_framework.quit()

            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = 800 - event.y


            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_DOWN:
                    self.slide_sound.play()
                    if self.state == "Big":
                        self.state = "Slide_Big"
                    else:
                        self.state = "Slide"

                elif event.key == SDLK_UP:
                    if self.state == "Big":
                        self.giant_jump_start_sound.play()
                        self.state = "Jump_Big"
                    else:
                        self.jump_sound.play()
                        self.state = "Jump"
                    self.jump += 1


                    if (self.y - 45) == 195:
                        self.jump_gravity = -35

                elif event.key == SDLK_1:
                    self.score += 100
                elif event.key == SDLK_3:
                    self.hpmove = 490


            elif event.type == SDL_KEYUP:
                if event.key == SDLK_DOWN:
                    if  self.state == "Slide_Big":
                        self.state = "Big"
                    else:
                        self.state = "Run"


class Player_second:
    Image_init = None
    TIME_PER_ACTION = 0.2
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self):
        self.x = 560
        self.y = 240
        self.sum_x = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.frame = 0.0
        self.total_frames = 0.0
        self.hp_frame = 0.0
        self.hpsize = 0.0
        self.hpmove = 0
        self.big_time = 0
        self.hp_time = 0
        self.dead_time = 0
        self.state = "Run"
        self.power = False
        self.big = False
        self.bool_hp = False
        self.bool_dead = False
        self.back_lobby = False
        self.score = 0
        self.dead_count = 0
        self.result_count = 0
        ######사운드#####
        self.bgm = load_music('Sound\\Stage2.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

        self.jump_sound = load_wav('Sound\\jump.wav')
        self.jump_sound.set_volume(64)

        self.slide_sound = load_wav('Sound\\slide.wav')
        self.slide_sound.set_volume(64)

        self.giant_jump_start_sound = load_wav('Sound\\g_giantjump.wav')
        self.giant_jump_start_sound.set_volume(64)

        self.giant_jump_end_sound = load_wav('Sound\\g_giantland.wav')
        self.giant_jump_end_sound.set_volume(128)

        self.dead_sound = load_wav('Sound\\g_end.wav')
        self.dead_sound.set_volume(128)

        self.result_sound = load_wav('Sound\\r_score.wav')
        self.result_sound.set_volume(128)

        if Player.Image_init == None:
            self.run_cookie = load_image('Image\\stage2_cookie\\cookie_run.png')
            self.slide_image = load_image('Image\\stage2_cookie\\cookie_run_slide.png')
            self.jump_image_first = load_image('Image\\stage2_cookie\\cookie_run_jump2.png')
            self.jump_image_second = load_image('Image\\stage2_cookie\\cookie_run_jump.png')
            self.run_cookie_collid = load_image('Image\\stage2_cookie\\cookie_run_collid2.png')
            self.run_cookie_big = load_image('Image\\stage2_cookie\\cookie_run_big.png')
            self.slide_image_big = load_image('Image\\stage2_cookie\\cookie_run_slide_big.png')
            self.jump_image_first_big = load_image('Image\\stage2_cookie\\cookie_run_jump2_big.png')
            self.jump_image_second_big = load_image('Image\\stage2_cookie\\cookie_run_jump_big.png')
            self.dead_cookie = load_image('Image\\stage2_cookie\\cookie_run_dead.png')
            self.big_icon = load_image('Image\\big_icon2.png')
            self.hp_icon = load_image('Image\\hp_icon2.png')
            #score 이미지 저장
            self.jelly = load_image('Image\\item_jelly2.png')
            self.one = load_image('Image\\Number\\1_2.png')
            self.two = load_image('Image\\Number\\2_2.png')
            self.three = load_image('Image\\Number\\3_2.png')
            self.four = load_image('Image\\Number\\4_2.png')
            self.five = load_image('Image\\Number\\5_2.png')
            self.six = load_image('Image\\Number\\6_2.png')
            self.seven = load_image('Image\\Number\\7_2.png')
            self.eight = load_image('Image\\Number\\8_2.png')
            self.nine = load_image('Image\\Number\\9_2.png')
            self.zero = load_image('Image\\Number\\0_2.png')
            self.result = load_image('image\\result.png')
            self.result_ok = load_image('image\\result_ok.png')
            self.result_ok_click = load_image('image\\result_ok_click.png')
            #체력 이미지 저장
            self.hp = load_image('Image\\hp_2.png')

        self.dir = "Right"
        self.jump = 0
        self.jump_gravity = 0

    def __del__(self):
        self.total_frames
        self.hp_frame
        self.hpsize
        self.hpmove

    def update(self, frame_time, hpsize):
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.hp_frame += self.total_frames / 2
        print(int((self.hp_frame) / 5000) + self.hpmove)
        self.hpsize = int((self.hp_frame) / 5000) + self.hpmove + hpsize
        self.frame = int(self.total_frames) % 6
        self.gravity()
        #print(self.total_frames)
        if self.hpsize >= 500:
            self.state = "Dead"
            self.frame = 0
            if self.dead_count == 0:
                self.dead_sound.play()
                self.dead_count += 1

        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Dead":
            if self.hpsize > 510:
                self.bool_dead = True
            self.frame = (self.frame +1) % 4
        elif self.state == "Jump" and self.state == "Slide":
            self.power = True
            self.frame = 0
        elif self.state == "Jump" and self.x >= 550:
            self.state = "Run"
        elif self.state == "Jump_Big" and self.x >= 550:
            self.giant_jump_end_sound.play()
            self.state = "Big"

        elif self.state == "Big" or self.state == "Slide_Big" or self.state == "Jump_Big":
            if self.big_time + 100 < self.total_frames:
                self.state = "Run"
                if self.big_time + 50 < self.total_frames:
                    self.big = False
                    self.big_time = 0

            if self.hp_time + 50 < self.total_frames:
                self.bool_hp = False
                self.hp_time = 0

        #elif self.state == "Collid":
            #self.power = True
            #if self.total_frames > self.total_frames + 10:
                #self.state = "Run"


    def get_bb(self):
        if self.state == "Run":
            return self.x - 43, self. y - 20, self.x + 35, self.y + 20
        elif self.state == "Slide":
            #return self.x - 20, self. y - 35, self.x + 20, self.y - 15
            return self.x - 15, self. y - 20, self.x + 35, self.y + 20
        elif self.state == "Jump":
            return self.x - 25, self. y - 20, self.x + 43, self.y + 20
        elif self.state == "Big":
            return self.x - 150, self. y - 130, self.x + 30, self.y + 130
        elif self.state == "Jump_Big":
            return self.x - 150, self. y - 130, self.x + 30, self.y + 130
        elif self.state == "Slide_Big":
            return self.x - 150, self. y - 130, self.x + 30, self.y + 130



        return self.x - 32, self. y - 43, self.x + 32, self.y + 43

    #def draw_bb(self):
        #draw_rectangle(*self.get_bb())


    def gravity(self):
        if (self.x - 45 - self.jump_gravity) < 515:
            self.jump_gravity -= 2
            self.x -= self.jump_gravity / 2
        else:
            self.x = 560
            self.jump_gravity = 0

    def draw(self):
        if self.state == "Run":
            self.run_cookie.clip_draw(0, self.frame * 75, 87, 75, self.x, self.y)
        elif self.state == "Slide":
            self.slide_image.draw(self.x + 17, self.y)
        elif self.state == "Jump":
            if self.jump % 2 == 1:
                self.jump_image_first.draw(self.x, self.y)
            elif self.jump % 2 == 0:
                self.jump_image_second.draw(self.x, self.y)


        elif self.state == "Big":
            self.run_cookie_big.clip_draw(0, self.frame * 300, 348, 300, self.x - 130, self.y)
            if self.big_time + 20 > self.total_frames:
                self.big_icon.draw(400, 400)

        elif self.state == "Slide_Big":
            self.slide_image_big.draw(self.x - 50, self.y)
            if self.big_time + 20 > self.total_frames:
                self.big_icon.draw(400, 400)

        elif self.state == "Jump_Big":
            if self.jump % 2 == 1:
                self.jump_image_first_big.draw(self.x - 130, self.y)
                if self.big_time + 20 > self.total_frames:
                    self.big_icon.draw(400, 400)
            elif self.jump % 2 == 0:
                self.jump_image_second_big.draw(self.x - 130, self.y)
                if self.big_time + 20 > self.total_frames:
                    self.big_icon.draw(400, 400)

        elif self.state == "Collid":
            self.run_cookie_collid.clip_draw(0, self.frame * 53, 81, 53, self.x, self.y)

        elif self.state == "Dead":
            if self.frame >= 4:
                self.frame = 4
            self.dead_cookie.clip_draw(0, self.frame * 100, 100, 100, self.x, self.y + 10)



        if self.bool_dead == True and self.result_count == 0:
            self.bgm.stop()
            self.result_sound.play()
            self.result_count += 1
        if self.bool_dead == True:
            self.result.draw(400, 400)
            if self.mouse_x > 354 and self.mouse_x < 446 and self.mouse_y > 259 and self.mouse_y < 291:
                self.result_ok_click.draw(400, 275)
            else:
                self.result_ok.draw(400 ,275)

            if converter.player_money % 10 == 0:
                self.zero.rotate_draw(11, 460, 440)
            elif converter.player_money % 10 == 1:
                self.one.rotate_draw(11, 460, 440)
            elif converter.player_money % 10 == 2:
                self.two.rotate_draw(11, 460, 440)
            elif converter.player_money % 10 == 3:
                self.three.rotate_draw(11, 460, 440)
            elif converter.player_money % 10 == 4:
                self.four.rotate_draw(11, 460, 440)
            elif converter.player_money % 10 == 5:
                self.five.rotate_draw(11, 460, 440)
            elif converter.player_money % 10 == 6:
                self.six.rotate_draw(11, 460, 440)
            elif converter.player_money % 10 == 7:
                self.seven.rotate_draw(11, 460, 440)
            elif converter.player_money % 10 == 8:
                self.eight.rotate_draw(11, 460, 440)
            elif converter.player_money % 10 == 9:
                self.nine.rotate_draw(11, 460, 440)

            if int(converter.player_money / 10) % 10 == 0:
                self.zero.rotate_draw(11, 400, 440)
            elif int(converter.player_money / 10) % 10 == 1:
                self.one.rotate_draw(11, 400, 440)
            elif int(converter.player_money / 10) % 10 == 2:
                self.two.rotate_draw(11, 400, 440)
            elif int(converter.player_money / 10) % 10 == 3:
                self.three.rotate_draw(11, 400, 440)
            elif int(converter.player_money / 10) % 10 == 4:
                self.four.rotate_draw(11, 400, 440)
            elif int(converter.player_money / 10) % 10 == 5:
                self.five.rotate_draw(11, 400, 440)
            elif int(converter.player_money / 10) % 10 == 6:
                self.six.rotate_draw(11, 400, 440)
            elif int(converter.player_money / 10) % 10 == 7:
                self.seven.rotate_draw(11, 400, 440)
            elif int(converter.player_money / 10) % 10 == 8:
                self.eight.rotate_draw(11, 400, 440)
            elif int(converter.player_money / 10) % 10 == 9:
                self.nine.rotate_draw(11, 400, 440)

            if int(converter.player_money / 100) == 0:
                self.zero.rotate_draw(11, 340, 440)
            elif int(converter.player_money / 100) == 1:
                self.one.rotate_draw(11, 340, 440)
            elif int(converter.player_money / 100) == 2:
                self.two.rotate_draw(11, 340, 440)
            elif int(converter.player_money / 100) == 3:
                self.three.rotate_draw(11, 340, 440)
            elif int(converter.player_money / 100) == 4:
                self.four.rotate_draw(11, 340, 440)
            elif int(converter.player_money / 100) == 5:
                self.five.rotate_draw(11, 340, 440)
            elif int(converter.player_money / 100) == 6:
                self.six.rotate_draw(11, 340, 440)
            elif int(converter.player_money / 100) == 7:
                self.seven.rotate_draw(11, 340, 440)
            elif int(converter.player_money / 100) == 8:
                self.eight.rotate_draw(11, 340, 440)
            elif int(converter.player_money / 100) == 9:
                self.nine.rotate_draw(11, 340, 440)
            #self.bool_dead = False

        if self.bool_hp == True:
            if self.hp_time + 20 > self.total_frames:
                self.hp_icon.draw(400, 400)

        '''if self.state == 'Jump_Big' and self.y <= 251:
                             self.giant_jump_end_sound.play()'''


        ###score부분
        if converter.player_money % 10 == 0:
            self.zero.draw(50, 750)
        elif converter.player_money % 10 == 1:
            self.one.draw(50, 750)
        elif converter.player_money % 10 == 2:
            self.two.draw(50, 750)
        elif converter.player_money % 10 == 3:
            self.three.draw(50, 750)
        elif converter.player_money % 10 == 4:
            self.four.draw(50, 750)
        elif converter.player_money % 10 == 5:
            self.five.draw(50, 750)
        elif converter.player_money % 10 == 6:
            self.six.draw(50, 750)
        elif converter.player_money % 10 == 7:
            self.seven.draw(50, 750)
        elif converter.player_money % 10 == 8:
            self.eight.draw(50, 750)
        elif converter.player_money % 10 == 9:
            self.nine.draw(50, 750)

        if int(converter.player_money / 10) % 10 == 0:
            self.zero.draw(50, 717)
        elif int(converter.player_money / 10) % 10 == 1:
            self.one.draw(50, 717)
        elif int(converter.player_money / 10) % 10 == 2:
            self.two.draw(50, 717)
        elif int(converter.player_money / 10) % 10 == 3:
            self.three.draw(50, 717)
        elif int(converter.player_money / 10) % 10 == 4:
            self.four.draw(50, 717)
        elif int(converter.player_money / 10) % 10 == 5:
            self.five.draw(50, 717)
        elif int(converter.player_money / 10) % 10 == 6:
            self.six.draw(50, 717)
        elif int(converter.player_money / 10) % 10 == 7:
            self.seven.draw(50, 717)
        elif int(converter.player_money / 10) % 10 == 8:
            self.eight.draw(50, 717)
        elif int(converter.player_money / 10) % 10 == 9:
            self.nine.draw(50, 717)

        if int(converter.player_money / 100) == 0:
            self.zero.draw(50, 684)
        elif int(converter.player_money / 100) == 1:
             self.one.draw(50, 684)
        elif int(converter.player_money / 100) == 2:
            self.two.draw(50, 684)
        elif int(converter.player_money / 100) == 3:
            self.three.draw(50, 684)
        elif int(converter.player_money / 100) == 4:
            self.four.draw(50, 684)
        elif int(converter.player_money / 100) == 5:
            self.five.draw(50, 684)
        elif int(converter.player_money / 100) == 6:
            self.six.draw(50, 684)
        elif int(converter.player_money / 100) == 7:
            self.seven.draw(50, 684)
        elif int(converter.player_money / 100) == 8:
            self.eight.draw(50, 684)
        elif int(converter.player_money / 100) == 9:
            self.nine.draw(50, 684)

        self.jelly.draw(50, 651)


        #hp바 구현
        #self.hp.clip_draw(self.frame * 10, 0, 500 - int(self.hpsize), 36, 300 - int(self.hpsize / 2), 750)
        self.hp.clip_draw(0, self.frame * 10, 66, 500 - int(self.hpsize), 30, 300 - int(self.hpsize / 2))
        #self.run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y)
        #print(self.hpsize)
            #self.run_cookie_collid.draw(self.x, self.y)
        #self.run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y + 200, 500, 500)


    def handle_events(self, event):
            events = get_events()

            if event.type == SDL_QUIT:
                game_framework.quit()

            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = 800 - event.y


            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_DOWN:
                    self.slide_sound.play()
                    if self.state == "Big":
                        self.state = "Slide_Big"
                    else:
                        self.state = "Slide"

                elif event.key == SDLK_UP:
                    if self.state == "Big":
                        self.giant_jump_start_sound.play()
                        self.state = "Jump_Big"
                    else:
                        self.jump_sound.play()
                        self.state = "Jump"
                    self.jump += 1


                    if (self.x - 45) == 515:
                        self.jump_gravity = 35

                elif event.key == SDLK_1:
                    self.score += 100
                elif event.key == SDLK_3:
                    self.hpmove = 490


            elif event.type == SDL_KEYUP:
                if event.key == SDLK_DOWN:
                    if  self.state == "Slide_Big":
                        self.state = "Big"
                    else:
                        self.state = "Run"



class Player_third:
    Image_init = None
    TIME_PER_ACTION = 0.2
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self):
        self.x = 650
        self.y = 560
        self.sum_x = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.frame = 0.0
        self.total_frames = 0.0
        self.hp_frame = 0.0
        self.hpsize = 0.0
        self.hpmove = 0
        self.big_time = 0
        self.hp_time = 0
        self.dead_time = 0
        self.state = "Run"
        self.power = False
        self.big = False
        self.bool_hp = False
        self.bool_dead = False
        self.back_lobby = False
        self.score = 0
        self.dead_count = 0
        self.result_count = 0
        ######사운드#####
        self.bgm = load_music('Sound\\Stage3.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

        self.jump_sound = load_wav('Sound\\jump.wav')
        self.jump_sound.set_volume(64)

        self.slide_sound = load_wav('Sound\\slide.wav')
        self.slide_sound.set_volume(64)

        self.giant_jump_start_sound = load_wav('Sound\\g_giantjump.wav')
        self.giant_jump_start_sound.set_volume(64)

        self.giant_jump_end_sound = load_wav('Sound\\g_giantland.wav')
        self.giant_jump_end_sound.set_volume(128)

        self.dead_sound = load_wav('Sound\\g_end.wav')
        self.dead_sound.set_volume(128)

        self.result_sound = load_wav('Sound\\r_score.wav')
        self.result_sound.set_volume(128)

        if Player.Image_init == None:
            self.run_cookie = load_image('Image\\stage3_cookie\\cookie_run.png')
            self.slide_image = load_image('Image\\stage3_cookie\\cookie_run_slide.png')
            self.jump_image_first = load_image('Image\\stage3_cookie\\cookie_run_jump2.png')
            self.jump_image_second = load_image('Image\\stage3_cookie\\cookie_run_jump.png')
            self.run_cookie_collid = load_image('Image\\stage3_cookie\\cookie_run_collid2.png')
            self.run_cookie_big = load_image('Image\\stage3_cookie\\cookie_run_big.png')
            self.slide_image_big = load_image('Image\\stage3_cookie\\cookie_run_slide_big.png')
            self.jump_image_first_big = load_image('Image\\stage3_cookie\\cookie_run_jump2_big.png')
            self.jump_image_second_big = load_image('Image\\stage3_cookie\\cookie_run_jump_big.png')
            self.dead_cookie = load_image('Image\\stage3_cookie\\cookie_run_dead.png')
            self.big_icon = load_image('Image\\big_icon3.png')
            self.hp_icon = load_image('Image\\hp_icon3.png')
            #score 이미지 저장
            self.jelly = load_image('Image\\item_jelly3.png')
            self.one = load_image('Image\\Number\\1_3.png')
            self.two = load_image('Image\\Number\\2_3.png')
            self.three = load_image('Image\\Number\\3_3.png')
            self.four = load_image('Image\\Number\\4_3.png')
            self.five = load_image('Image\\Number\\5_3.png')
            self.six = load_image('Image\\Number\\6_3.png')
            self.seven = load_image('Image\\Number\\7_3.png')
            self.eight = load_image('Image\\Number\\8_3.png')
            self.nine = load_image('Image\\Number\\9_3.png')
            self.zero = load_image('Image\\Number\\0_3.png')
            self.result = load_image('image\\result.png')
            self.result_ok = load_image('image\\result_ok.png')
            self.result_ok_click = load_image('image\\result_ok_click.png')
            #체력 이미지 저장
            self.hp = load_image('Image\\hp_3.png')

        self.dir = "Right"
        self.jump = 0
        self.jump_gravity = 0

    def __del__(self):
        self.total_frames
        self.hp_frame
        self.hpsize
        self.hpmove

    def update(self, frame_time, hpsize):
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.hp_frame += self.total_frames / 3
        print(int((self.hp_frame) / 5000) + self.hpmove)
        self.hpsize = int((self.hp_frame) / 5000) + self.hpmove + hpsize
        self.frame = int(self.total_frames) % 6
        self.gravity()
        #print(self.total_frames)
        if self.hpsize >= 500:
            self.state = "Dead"
            self.frame = 0
            if self.dead_count == 0:
                self.dead_sound.play()
                self.dead_count += 1

        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Dead":
            if self.hpsize > 510:
                self.bool_dead = True
            self.frame = (self.frame +1) % 4
        elif self.state == "Jump" and self.state == "Slide":
            self.power = True
            self.frame = 0
        elif self.state == "Jump" and self.y >= 550:
            self.state = "Run"
        elif self.state == "Jump_Big" and self.y >= 550:
            self.giant_jump_end_sound.play()
            self.state = "Big"

        elif self.state == "Big" or self.state == "Slide_Big" or self.state == "Jump_Big":
            if self.big_time + 100 < self.total_frames:
                self.state = "Run"
                if self.big_time + 50 < self.total_frames:
                    self.big = False
                    self.big_time = 0

            if self.hp_time + 50 < self.total_frames:
                self.bool_hp = False
                self.hp_time = 0

        #elif self.state == "Collid":
            #self.power = True
            #if self.total_frames > self.total_frames + 10:
                #self.state = "Run"


    def get_bb(self):
        if self.state == "Run":
            return self.x - 20, self. y - 43, self.x + 20, self.y + 35
        elif self.state == "Slide":
            return self.x - 20, self. y - 15, self.x + 20, self.y + 35
        elif self.state == "Jump":
            return self.x - 20, self. y - 43, self.x + 20, self.y + 35
        elif self.state == "Big":
            return self.x - 130, self. y - 150, self.x + 130, self.y + 30
        elif self.state == "Jump_Big":
            return self.x - 130, self. y - 150, self.x + 130, self.y + 30
        elif self.state == "Slide_Big":
            return self.x - 130, self. y - 100, self.x + 130, self.y + 30

        '''if self.state == "Run":
            return self.x - 20, self. y - 35, self.x + 20, self.y + 43
        elif self.state == "Slide":
            return self.x - 20, self. y - 35, self.x + 20, self.y - 15
        elif self.state == "Jump":
            return self.x - 20, self. y - 35, self.x + 20, self.y + 43
        elif self.state == "Big":
            return self.x - 130, self. y - 30, self.x + 130, self.y + 150
        elif self.state == "Jump_Big":
            return self.x - 130, self. y - 30, self.x + 130, self.y + 150
        elif self.state == "Slide_Big":
            return self.x - 130, self. y - 30, self.x + 130, self.y + 100'''

        return self.x - 32, self. y - 43, self.x + 32, self.y + 43

    #def draw_bb(self):
        #draw_rectangle(*self.get_bb())


    def gravity(self):
        if (self.y + 45 + self.jump_gravity) < 605: #560
            self.jump_gravity += 2
            self.y += self.jump_gravity / 2


        #if (self.y - 45 - self.jump_gravity) > 195: #240
            #self.jump_gravity += 2
            #self.y -= self.jump_gravity / 2
        else:
            self.y = 560
            self.jump_gravity = 0

    def draw(self):
        if self.state == "Run":
            self.run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y)
        elif self.state == "Slide":
            self.slide_image.draw(self.x, self.y + 17)
        elif self.state == "Jump":
            if self.jump % 2 == 1:
                self.jump_image_first.draw(self.x, self.y)
            elif self.jump % 2 == 0:
                self.jump_image_second.draw(self.x, self.y)


        elif self.state == "Big":
            self.run_cookie_big.clip_draw(self.frame * 300, 0, 300, 348, self.x, self.y - 130)
            if self.big_time + 20 > self.total_frames:
                self.big_icon.draw(400, 400)

        elif self.state == "Slide_Big":
            self.slide_image_big.draw(self.x, self.y - 46)
            if self.big_time + 20 > self.total_frames:
                self.big_icon.draw(400, 400)

        elif self.state == "Jump_Big":
            if self.jump % 2 == 1:
                self.jump_image_first_big.draw(self.x, self.y - 126)
                if self.big_time + 20 > self.total_frames:
                    self.big_icon.draw(400, 400)
            elif self.jump % 2 == 0:
                self.jump_image_second_big.draw(self.x, self.y - 126)
                if self.big_time + 20 > self.total_frames:
                    self.big_icon.draw(400, 400)

        elif self.state == "Collid":
            self.run_cookie_collid.clip_draw(self.frame * 53, 0, 53, 81, self.x, self.y)

        elif self.state == "Dead":
            if self.frame >= 4:
                self.frame = 4
            self.dead_cookie.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y - 10)



        if self.bool_dead == True and self.result_count == 0:
            self.bgm.stop()
            self.result_sound.play()
            self.result_count += 1
        if self.bool_dead == True:
            self.result.draw(400, 400)
            if self.mouse_x > 354 and self.mouse_x < 446 and self.mouse_y > 259 and self.mouse_y < 291:
                self.result_ok_click.draw(400, 275)
            else:
                self.result_ok.draw(400 ,275)

            if converter.player_money % 10 == 0:
                self.zero.rotate_draw(22, 460, 440)
            elif converter.player_money % 10 == 1:
                self.one.rotate_draw(22, 460, 440)
            elif converter.player_money % 10 == 2:
                self.two.rotate_draw(22, 460, 440)
            elif converter.player_money % 10 == 3:
                self.three.rotate_draw(22, 460, 440)
            elif converter.player_money % 10 == 4:
                self.four.rotate_draw(22, 460, 440)
            elif converter.player_money % 10 == 5:
                self.five.rotate_draw(22, 460, 440)
            elif converter.player_money % 10 == 6:
                self.six.rotate_draw(22, 460, 440)
            elif converter.player_money % 10 == 7:
                self.seven.rotate_draw(22, 460, 440)
            elif converter.player_money % 10 == 8:
                self.eight.rotate_draw(22, 460, 440)
            elif converter.player_money % 10 == 9:
                self.nine.rotate_draw(22, 460, 440)

            if int(converter.player_money / 10) % 10 == 0:
                self.zero.rotate_draw(22, 400, 440)
            elif int(converter.player_money / 10) % 10 == 1:
                self.one.rotate_draw(22, 400, 440)
            elif int(converter.player_money / 10) % 10 == 2:
                self.two.rotate_draw(22, 400, 440)
            elif int(converter.player_money / 10) % 10 == 3:
                self.three.rotate_draw(22, 400, 440)
            elif int(converter.player_money / 10) % 10 == 4:
                self.four.rotate_draw(22, 400, 440)
            elif int(converter.player_money / 10) % 10 == 5:
                self.five.rotate_draw(22, 400, 440)
            elif int(converter.player_money / 10) % 10 == 6:
                self.six.rotate_draw(22, 400, 440)
            elif int(converter.player_money / 10) % 10 == 7:
                self.seven.rotate_draw(22, 400, 440)
            elif int(converter.player_money / 10) % 10 == 8:
                self.eight.rotate_draw(22, 400, 440)
            elif int(converter.player_money / 10) % 10 == 9:
                self.nine.rotate_draw(22, 400, 440)

            if int(converter.player_money / 100) == 0:
                self.zero.rotate_draw(22, 340, 440)
            elif int(converter.player_money / 100) == 1:
                self.one.rotate_draw(22, 340, 440)
            elif int(converter.player_money / 100) == 2:
                self.two.rotate_draw(22, 340, 440)
            elif int(converter.player_money / 100) == 3:
                self.three.rotate_draw(22, 340, 440)
            elif int(converter.player_money / 100) == 4:
                self.four.rotate_draw(22, 340, 440)
            elif int(converter.player_money / 100) == 5:
                self.five.rotate_draw(22, 340, 440)
            elif int(converter.player_money / 100) == 6:
                self.six.rotate_draw(22, 340, 440)
            elif int(converter.player_money / 100) == 7:
                self.seven.rotate_draw(22, 340, 440)
            elif int(converter.player_money / 100) == 8:
                self.eight.rotate_draw(22, 340, 440)
            elif int(converter.player_money / 100) == 9:
                self.nine.rotate_draw(22, 340, 440)
            #self.bool_dead = False

        if self.bool_hp == True:
            if self.hp_time + 20 > self.total_frames:
                self.hp_icon.draw(400, 400)

        '''if self.state == 'Jump_Big' and self.y <= 251:
                             self.giant_jump_end_sound.play()'''


        ###score부분
        if converter.player_money % 10 == 0:
            self.zero.draw(50, 50)
        elif converter.player_money % 10 == 1:
            self.one.draw(50, 50)
        elif converter.player_money % 10 == 2:
            self.two.draw(50, 50)
        elif converter.player_money % 10 == 3:
            self.three.draw(50, 50)
        elif converter.player_money % 10 == 4:
            self.four.draw(50, 50)
        elif converter.player_money % 10 == 5:
            self.five.draw(50, 50)
        elif converter.player_money % 10 == 6:
            self.six.draw(50, 50)
        elif converter.player_money % 10 == 7:
            self.seven.draw(50, 50)
        elif converter.player_money % 10 == 8:
            self.eight.draw(50, 50)
        elif converter.player_money % 10 == 9:
            self.nine.draw(50, 50)

        if int(converter.player_money / 10) % 10 == 0:
            self.zero.draw(83, 50)
        elif int(converter.player_money / 10) % 10 == 1:
            self.one.draw(83, 50)
        elif int(converter.player_money / 10) % 10 == 2:
            self.two.draw(83, 50)
        elif int(converter.player_money / 10) % 10 == 3:
            self.three.draw(83, 50)
        elif int(converter.player_money / 10) % 10 == 4:
            self.four.draw(83, 50)
        elif int(converter.player_money / 10) % 10 == 5:
            self.five.draw(83, 50)
        elif int(converter.player_money / 10) % 10 == 6:
            self.six.draw(83, 50)
        elif int(converter.player_money / 10) % 10 == 7:
            self.seven.draw(83, 50)
        elif int(converter.player_money / 10) % 10 == 8:
            self.eight.draw(83, 50)
        elif int(converter.player_money / 10) % 10 == 9:
            self.nine.draw(83, 50)

        if int(converter.player_money / 100) == 0:
            self.zero.draw(116, 50)
        elif int(converter.player_money / 100) == 1:
             self.one.draw(116, 50)
        elif int(converter.player_money / 100) == 2:
            self.two.draw(116, 50)
        elif int(converter.player_money / 100) == 3:
            self.three.draw(116, 50)
        elif int(converter.player_money / 100) == 4:
            self.four.draw(116, 50)
        elif int(converter.player_money / 100) == 5:
            self.five.draw(116, 50)
        elif int(converter.player_money / 100) == 6:
            self.six.draw(116, 50)
        elif int(converter.player_money / 100) == 7:
            self.seven.draw(116, 50)
        elif int(converter.player_money / 100) == 8:
            self.eight.draw(116, 50)
        elif int(converter.player_money / 100) == 9:
            self.nine.draw(116, 50)

        self.jelly.draw(149, 50)


        #hp바 구현
        self.hp.clip_draw(self.frame * 10, 0, 500 - int(self.hpsize), 60, 500 - int(self.hpsize / 2), 35)
        #self.run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y)
        #print(self.hpsize)
            #self.run_cookie_collid.draw(self.x, self.y)
        #self.run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y + 200, 500, 500)


    def handle_events(self, event):
            events = get_events()

            if event.type == SDL_QUIT:
                game_framework.quit()

            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = 800 - event.y


            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_DOWN:
                    self.slide_sound.play()
                    if self.state == "Big":
                        self.state = "Slide_Big"
                    else:
                        self.state = "Slide"

                elif event.key == SDLK_UP:
                    if self.state == "Big":
                        self.giant_jump_start_sound.play()
                        self.state = "Jump_Big"
                    else:
                        self.jump_sound.play()
                        self.state = "Jump"
                    self.jump += 1


                    if (self.y + 45) == 605:
                        self.jump_gravity = -35

                elif event.key == SDLK_1:
                    self.score += 100
                elif event.key == SDLK_3:
                    self.hpmove = 490


            elif event.type == SDL_KEYUP:
                if event.key == SDLK_DOWN:
                    if  self.state == "Slide_Big":
                        self.state = "Big"
                    else:
                        self.state = "Run"


class Player_four:
    Image_init = None
    TIME_PER_ACTION = 0.2
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    def __init__(self):
        self.x = 240
        self.y = 560
        self.sum_x = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.frame = 0.0
        self.total_frames = 0.0
        self.hp_frame = 0.0
        self.hpsize = 0.0
        self.hpmove = 0
        self.big_time = 0
        self.hp_time = 0
        self.dead_time = 0
        self.state = "Run"
        self.power = False
        self.big = False
        self.bool_hp = False
        self.bool_dead = False
        self.back_lobby = False
        self.score = 0
        self.dead_count = 0
        self.result_count = 0
        ######사운드#####
        self.bgm = load_music('Sound\\Stage4.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

        self.jump_sound = load_wav('Sound\\jump.wav')
        self.jump_sound.set_volume(64)

        self.slide_sound = load_wav('Sound\\slide.wav')
        self.slide_sound.set_volume(64)

        self.giant_jump_start_sound = load_wav('Sound\\g_giantjump.wav')
        self.giant_jump_start_sound.set_volume(64)

        self.giant_jump_end_sound = load_wav('Sound\\g_giantland.wav')
        self.giant_jump_end_sound.set_volume(128)

        self.dead_sound = load_wav('Sound\\g_end.wav')
        self.dead_sound.set_volume(128)

        self.result_sound = load_wav('Sound\\r_score.wav')
        self.result_sound.set_volume(128)

        if Player.Image_init == None:
            self.run_cookie = load_image('Image\\stage4_cookie\\cookie_run.png')
            self.slide_image = load_image('Image\\stage4_cookie\\cookie_run_slide.png')
            self.jump_image_first = load_image('Image\\stage4_cookie\\cookie_run_jump2.png')
            self.jump_image_second = load_image('Image\\stage4_cookie\\cookie_run_jump.png')
            self.run_cookie_collid = load_image('Image\\stage4_cookie\\cookie_run_collid2.png')
            self.run_cookie_big = load_image('Image\\stage4_cookie\\cookie_run_big.png')
            self.slide_image_big = load_image('Image\\stage4_cookie\\cookie_run_slide_big.png')
            self.jump_image_first_big = load_image('Image\\stage4_cookie\\cookie_run_jump2_big.png')
            self.jump_image_second_big = load_image('Image\\stage4_cookie\\cookie_run_jump_big.png')
            self.dead_cookie = load_image('Image\\stage4_cookie\\cookie_run_dead.png')
            self.big_icon = load_image('Image\\big_icon4.png')
            self.hp_icon = load_image('Image\\hp_icon4.png')
            #score 이미지 저장
            self.jelly = load_image('Image\\item_jelly4.png')
            self.one = load_image('Image\\Number\\1_4.png')
            self.two = load_image('Image\\Number\\2_4.png')
            self.three = load_image('Image\\Number\\3_4.png')
            self.four = load_image('Image\\Number\\4_4.png')
            self.five = load_image('Image\\Number\\5_4.png')
            self.six = load_image('Image\\Number\\6_4.png')
            self.seven = load_image('Image\\Number\\7_4.png')
            self.eight = load_image('Image\\Number\\8_4.png')
            self.nine = load_image('Image\\Number\\9_4.png')
            self.zero = load_image('Image\\Number\\0_4.png')
            self.result = load_image('image\\result.png')
            self.result_ok = load_image('image\\result_ok.png')
            self.result_ok_click = load_image('image\\result_ok_click.png')
            #체력 이미지 저장
            self.hp = load_image('Image\\hp_4.png')

        self.dir = "Right"
        self.jump = 0
        self.jump_gravity = 0

    def __del__(self):
        self.total_frames
        self.hp_frame
        self.hpsize
        self.hpmove

    def update(self, frame_time, hpsize):
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.hp_frame += self.total_frames / 4
        print(int((self.hp_frame) / 5000) + self.hpmove)
        self.hpsize = int((self.hp_frame) / 5000) + self.hpmove + hpsize
        self.frame = int(self.total_frames) % 6
        self.gravity()
        #print(self.total_frames)
        if self.hpsize >= 500:
            self.state = "Dead"
            self.frame = 0
            if self.dead_count == 0:
                self.dead_sound.play()
                self.dead_count += 1

        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Dead":
            if self.hpsize > 510:
                self.bool_dead = True
            self.frame = (self.frame +1) % 4
        elif self.state == "Jump" and self.state == "Slide":
            self.power = True
            self.frame = 0
        elif self.state == "Jump" and self.x <= 250:
            self.state = "Run"
        elif self.state == "Jump_Big" and self.x <= 250:
            self.giant_jump_end_sound.play()
            self.state = "Big"

        elif self.state == "Big" or self.state == "Slide_Big" or self.state == "Jump_Big":
            if self.big_time + 100 < self.total_frames:
                self.state = "Run"
                if self.big_time + 50 < self.total_frames:
                    self.big = False
                    self.big_time = 0

            if self.hp_time + 50 < self.total_frames:
                self.bool_hp = False
                self.hp_time = 0

        #elif self.state == "Collid":
            #self.power = True
            #if self.total_frames > self.total_frames + 10:
                #self.state = "Run"


    def get_bb(self):
        if self.state == "Run":
            return self.x - 35, self. y - 20, self.x + 43, self.y + 20
        elif self.state == "Slide":
            #return self.x - 20, self. y - 35, self.x + 20, self.y - 15
            return self.x - 35, self. y - 20, self.x + 15, self.y + 20
        elif self.state == "Jump":
            return self.x - 43, self. y - 20, self.x + 25, self.y + 20
        elif self.state == "Big":
            return self.x - 30, self. y - 130, self.x + 150, self.y + 130
        elif self.state == "Jump_Big":
            return self.x - 30, self. y - 130, self.x + 150, self.y + 130
        elif self.state == "Slide_Big":
            return self.x - 30, self. y - 130, self.x + 150, self.y + 130

        return self.x - 32, self. y - 43, self.x + 32, self.y + 43

    #def draw_bb(self):
        #draw_rectangle(*self.get_bb())


    def gravity(self):
        if (self.x + 45 + self.jump_gravity) > 285:
            self.jump_gravity -= 2
            self.x += self.jump_gravity / 2
        else:
            self.x = 240
            self.jump_gravity = 0

    def draw(self):
        if self.state == "Run":
            self.run_cookie.clip_draw(0, self.frame * 75, 87, 75, self.x, self.y)
        elif self.state == "Slide":
            self.slide_image.draw(self.x - 17, self.y)
        elif self.state == "Jump":
            if self.jump % 2 == 1:
                self.jump_image_first.draw(self.x, self.y)
            elif self.jump % 2 == 0:
                self.jump_image_second.draw(self.x, self.y)


        elif self.state == "Big":
            self.run_cookie_big.clip_draw(0, self.frame * 300, 348, 300, self.x + 130, self.y)
            if self.big_time + 20 > self.total_frames:
                self.big_icon.draw(400, 400)

        elif self.state == "Slide_Big":
            self.slide_image_big.draw(self.x + 50, self.y)
            if self.big_time + 20 > self.total_frames:
                self.big_icon.draw(400, 400)

        elif self.state == "Jump_Big":
            if self.jump % 2 == 1:
                self.jump_image_first_big.draw(self.x + 130, self.y)
                if self.big_time + 20 > self.total_frames:
                    self.big_icon.draw(400, 400)
            elif self.jump % 2 == 0:
                self.jump_image_second_big.draw(self.x + 130, self.y)
                if self.big_time + 20 > self.total_frames:
                    self.big_icon.draw(400, 400)

        elif self.state == "Collid":
            self.run_cookie_collid.clip_draw(0, self.frame * 53, 81, 53, self.x, self.y)

        elif self.state == "Dead":
            if self.frame >= 4:
                self.frame = 4
            self.dead_cookie.clip_draw(0, self.frame * 100, 100, 100, self.x, self.y + 10)



        if self.bool_dead == True and self.result_count == 0:
            self.bgm.stop()
            self.result_sound.play()
            self.result_count += 1
        if self.bool_dead == True:
            self.result.draw(400, 400)
            if self.mouse_x > 354 and self.mouse_x < 446 and self.mouse_y > 259 and self.mouse_y < 291:
                self.result_ok_click.draw(400, 275)
            else:
                self.result_ok.draw(400 ,275)

            if converter.player_money % 10 == 0:
                self.zero.rotate_draw(33, 460, 440)
            elif converter.player_money % 10 == 1:
                self.one.rotate_draw(33, 460, 440)
            elif converter.player_money % 10 == 2:
                self.two.rotate_draw(33, 460, 440)
            elif converter.player_money % 10 == 3:
                self.three.rotate_draw(33, 460, 440)
            elif converter.player_money % 10 == 4:
                self.four.rotate_draw(33, 460, 440)
            elif converter.player_money % 10 == 5:
                self.five.rotate_draw(33, 460, 440)
            elif converter.player_money % 10 == 6:
                self.six.rotate_draw(33, 460, 440)
            elif converter.player_money % 10 == 7:
                self.seven.rotate_draw(33, 460, 440)
            elif converter.player_money % 10 == 8:
                self.eight.rotate_draw(33, 460, 440)
            elif converter.player_money % 10 == 9:
                self.nine.rotate_draw(33, 460, 440)

            if int(converter.player_money / 10) % 10 == 0:
                self.zero.rotate_draw(33, 400, 440)
            elif int(converter.player_money / 10) % 10 == 1:
                self.one.rotate_draw(33, 400, 440)
            elif int(converter.player_money / 10) % 10 == 2:
                self.two.rotate_draw(33, 400, 440)
            elif int(converter.player_money / 10) % 10 == 3:
                self.three.rotate_draw(33, 400, 440)
            elif int(converter.player_money / 10) % 10 == 4:
                self.four.rotate_draw(33, 400, 440)
            elif int(converter.player_money / 10) % 10 == 5:
                self.five.rotate_draw(33, 400, 440)
            elif int(converter.player_money / 10) % 10 == 6:
                self.six.rotate_draw(33, 400, 440)
            elif int(converter.player_money / 10) % 10 == 7:
                self.seven.rotate_draw(33, 400, 440)
            elif int(converter.player_money / 10) % 10 == 8:
                self.eight.rotate_draw(33, 400, 440)
            elif int(converter.player_money / 10) % 10 == 9:
                self.nine.rotate_draw(33, 400, 440)

            if int(converter.player_money / 100) == 0:
                self.zero.rotate_draw(33, 340, 440)
            elif int(converter.player_money / 100) == 1:
                self.one.rotate_draw(33, 340, 440)
            elif int(converter.player_money / 100) == 2:
                self.two.rotate_draw(33, 340, 440)
            elif int(converter.player_money / 100) == 3:
                self.three.rotate_draw(33, 340, 440)
            elif int(converter.player_money / 100) == 4:
                self.four.rotate_draw(33, 340, 440)
            elif int(converter.player_money / 100) == 5:
                self.five.rotate_draw(33, 340, 440)
            elif int(converter.player_money / 100) == 6:
                self.six.rotate_draw(33, 340, 440)
            elif int(converter.player_money / 100) == 7:
                self.seven.rotate_draw(33, 340, 440)
            elif int(converter.player_money / 100) == 8:
                self.eight.rotate_draw(33, 340, 440)
            elif int(converter.player_money / 100) == 9:
                self.nine.rotate_draw(33, 340, 440)
            #self.bool_dead = False

        if self.bool_hp == True:
            if self.hp_time + 20 > self.total_frames:
                self.hp_icon.draw(400, 400)

        '''if self.state == 'Jump_Big' and self.y <= 251:
                             self.giant_jump_end_sound.play()'''


        ###score부분
        if converter.player_money % 10 == 0:
            self.zero.draw(750, 50)
        elif converter.player_money % 10 == 1:
            self.one.draw(750, 50)
        elif converter.player_money % 10 == 2:
            self.two.draw(750, 50)
        elif converter.player_money % 10 == 3:
            self.three.draw(750, 50)
        elif converter.player_money % 10 == 4:
            self.four.draw(750, 50)
        elif converter.player_money % 10 == 5:
            self.five.draw(750, 50)
        elif converter.player_money % 10 == 6:
            self.six.draw(750, 50)
        elif converter.player_money % 10 == 7:
            self.seven.draw(750, 50)
        elif converter.player_money % 10 == 8:
            self.eight.draw(750, 50)
        elif converter.player_money % 10 == 9:
            self.nine.draw(750, 50)

        if int(converter.player_money / 10) % 10 == 0:
            self.zero.draw(750, 83)
        elif int(converter.player_money / 10) % 10 == 1:
            self.one.draw(750, 83)
        elif int(converter.player_money / 10) % 10 == 2:
            self.two.draw(750, 83)
        elif int(converter.player_money / 10) % 10 == 3:
            self.three.draw(750, 83)
        elif int(converter.player_money / 10) % 10 == 4:
            self.four.draw(750, 83)
        elif int(converter.player_money / 10) % 10 == 5:
            self.five.draw(750, 83)
        elif int(converter.player_money / 10) % 10 == 6:
            self.six.draw(750, 83)
        elif int(converter.player_money / 10) % 10 == 7:
            self.seven.draw(750, 83)
        elif int(converter.player_money / 10) % 10 == 8:
            self.eight.draw(750, 83)
        elif int(converter.player_money / 10) % 10 == 9:
            self.nine.draw(750, 83)

        if int(converter.player_money / 100) == 0:
            self.zero.draw(750, 116)
        elif int(converter.player_money / 100) == 1:
             self.one.draw(750, 116)
        elif int(converter.player_money / 100) == 2:
            self.two.draw(750, 116)
        elif int(converter.player_money / 100) == 3:
            self.three.draw(750, 116)
        elif int(converter.player_money / 100) == 4:
            self.four.draw(750, 116)
        elif int(converter.player_money / 100) == 5:
            self.five.draw(750, 116)
        elif int(converter.player_money / 100) == 6:
            self.six.draw(750, 116)
        elif int(converter.player_money / 100) == 7:
            self.seven.draw(750, 116)
        elif int(converter.player_money / 100) == 8:
            self.eight.draw(750, 116)
        elif int(converter.player_money / 100) == 9:
            self.nine.draw(750, 116)

        self.jelly.draw(750, 149)


        #hp바 구현
        #self.hp.clip_draw(self.frame * 10, 0, 500 - int(self.hpsize), 36, 300 - int(self.hpsize / 2), 750)
        self.hp.clip_draw(0, self.frame * 10, 66, 500 - int(self.hpsize), 770, 500 - int(self.hpsize / 2))
        #self.run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y)
        #print(self.hpsize)
            #self.run_cookie_collid.draw(self.x, self.y)
        #self.run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y + 200, 500, 500)


    def handle_events(self, event):
            events = get_events()

            if event.type == SDL_QUIT:
                game_framework.quit()

            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = 800 - event.y


            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_DOWN:
                    self.slide_sound.play()
                    if self.state == "Big":
                        self.state = "Slide_Big"
                    else:
                        self.state = "Slide"

                elif event.key == SDLK_UP:
                    if self.state == "Big":
                        self.giant_jump_start_sound.play()
                        self.state = "Jump_Big"
                    else:
                        self.jump_sound.play()
                        self.state = "Jump"
                    self.jump += 1


                    if (self.x + 45) == 285:
                        self.jump_gravity = 35

                elif event.key == SDLK_1:
                    self.score += 100
                elif event.key == SDLK_3:
                    self.hpmove = 490


            elif event.type == SDL_KEYUP:
                if event.key == SDLK_DOWN:
                    if  self.state == "Slide_Big":
                        self.state = "Big"
                    else:
                        self.state = "Run"