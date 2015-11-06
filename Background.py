from pico2d import *

import random
import json
import os
import title_state

class Background:
    Image_init = None

    def __init__(self):
        self.first_x = 400
        self.first_y = 400
        self.second_x = 1200
        self.second_y = 400
        if Background.Image_init == None:
            self.background_first = load_image('Image\\First_Background.png')
            self.background_second = load_image('Image\\First_Background.png')

        self.frame = 0
        self.speed = 5

    def update(self):
        self.first_x -= self.speed
        self.second_x -= self.speed
        self.frame = self.frame + 1
        '''
        if self.frame % 10 == 0:
            self.Speed += 0.1'''

        if self.second_x == 400:
            self.first_x = 1200

        if self.first_x == 400:
            self.second_x = 1200


    def draw(self):
        self.background_first.draw(self.first_x, self.first_y)
        self.background_second.draw(self.second_x, self.second_y)