from pico2d import *

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
        self.frame = 0.0
        self.total_frames = 0.0
        self.big_time = 0
        self.state = "Run"
        self.power = False
        self.big = False
        self.score = 0

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
            self.big_icon = load_image('Image\\big_icon.png')

        self.dir = "Right"
        self.jump = 0
        self.jump_gravity = 0

    def update(self, frame_time, score):
        print(score)
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6
        self.gravity()
        #print(self.total_frames)
        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Jump" and self.state == "Slide":
            self.power = True
            self.frame = 0
        elif self.state == "Jump" and self.y <= 250:
            self.state = "Run"
        elif self.state == "Jump_Big" and self.y <= 250:
            self.state = "Big"

        elif self.state == "Big" or self.state == "Slide_Big" or self.state == "Jump_Big":
            if self.big_time + 100 < self.total_frames:
                self.state = "Run"
                if self.big_time + 50 < self.total_frames:
                    self.big = False
                    self.big_time = 0
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

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


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
            #self.run_cookie_collid.draw(self.x, self.y)
        #self.run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y + 200, 500, 500)


    def handle_events(self, event):
            events = get_events()

            if event.type == SDL_QUIT:
                game_framework.quit()

            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_DOWN:
                    if self.state == "Big":
                        self.state = "Slide_Big"
                    else:
                        self.state = "Slide"

                elif event.key == SDLK_UP:
                    if self.state == "Big":
                        self.state = "Jump_Big"
                    else:
                        self.state = "Jump"
                    self.jump += 1


                    if (self.y - 45) == 195:
                        self.jump_gravity = -35


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
        self.frame = 0.0
        self.total_frames = 0.0
        self.state = "Run"

        if Player.Image_init == None:
            self.run_cookie = load_image('Image\\cookie_run2.png')
            self.slide_image = load_image('Image\\cookie_run_slide2.png')
            self.jump_image_first = load_image('Image\\cookie_run_jump_2.png')
            self.jump_image_second = load_image('Image\\cookie_run_jump2_2.png')

        self.dir = "Right"
        self.jump = 0
        self.jump_gravity = 0

    def update(self, frame_time):
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6
        self.gravity()


        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Jump" and self.state == "Slide":
            self.frame = 0
        elif self.state == "Jump" and self.x >= 550:
            self.state = "Run"


    def get_bb(self):
        if self.state == "Run":
            return self.x - 35, self. y - 20, self.x + 43, self.y + 20
        elif self.state == "Slide":
            return self.x + 35, self. y - 20, self.x + 15, self.y + 20
        elif self.state == "Jump":
            return self.x - 35, self. y - 20, self.x + 43, self.y + 20


        '''if self.state == "Run":
            return self.x - 32, self. y - 43, self.x + 32, self.y + 43
        elif self.state == "Slide":
            return self.x - 32, self. y - 43, self.x + 32, self.y
        elif self.state == "Jump":
            return self.x - 32, self. y - 43, self.x + 32, self.y + 43'''

        return self.x - 32, self. y - 43, self.x + 32, self.y + 43

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



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




    def handle_events(self, event):
            events = get_events()

            if event.type == SDL_QUIT:
                game_framework.quit()

            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_DOWN:
                    self.state = "Slide"
                elif event.key == SDLK_UP:
                    self.state = "Jump"
                    self.jump += 1


                    if (self.x - 45) == 515:
                        self.jump_gravity = +35


            elif event.type == SDL_KEYUP:
                if event.key == SDLK_DOWN:
                    self.state = "Run"

