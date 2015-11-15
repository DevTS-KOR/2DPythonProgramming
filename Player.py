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
        self.frame = 0.0
        self.total_frames = 0.0
        self.state = "Run"

        if Player.Image_init == None:
            self.run_cookie = load_image('Image\\cookie_run.png')
            self.slide_image = load_image('Image\\cookie_run_slide.png')
            self.jump_image_first = load_image('Image\\cookie_run_jump2.png')
            self.jump_image_second = load_image('Image\\cookie_run_jump.png')

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
        elif self.state == "Jump" and self.y <= 250:
            self.state = "Run"





    def gravity(self):
        if (self.y - 45 - self.jump_gravity) > 195:
            self.jump_gravity += 2
            self.y -= self.jump_gravity / 2
            #delay(0.03)
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


                    if (self.y - 45) == 195:
                        self.jump_gravity = -35
                #elif event.key == SDLK_2:
                    #game_framework.change_state(main_state2)

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_DOWN:
                    self.state = "Run"

