from pico2d import *

import random
import json
import os
import title_state

class Player:
    Image_init = None

    def __init__(self):
        self.x = 150
        self.y = 240
        self.frame = 0
        self.state = "Run"

        if Player.Image_init == None:
            self.Run_cookie = load_image('Image\\cookie_run.png')
            self.Slide_image = load_image('Image\\cookie_run_slide.png')
            self.Jump_image_frist = load_image('Image\\cookie_run_jump2.png')
            self.Jump_image_second = load_image('Image\\cookie_run_jump.png')

        self.dir = "Right"
        self.gravityY = 0

    def update(self):
        #self.gravity()
        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Jump" and self.state == "Slide":
            self.frame = 0
        elif self.state == "Jump" and self.y <= 250:
            self.state = "Run"


    def draw(self):
        if self.state == 'Run':
            self.Run_cookie.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y)
