from pico2d import *

import random
import json
import os
import title_state

class Ground:
    Image_init = None

    def __init__(self):
        self.first_x = 400
        self.first_y = 400
        self.second_x = 1200
        self.second_y = 400
        self.speed = 10
        self.frame = 0
        if Ground.Image_init == None:
            self.ground_first = load_image('Image\\First_ground.png')
            self.ground_second = load_image('Image\\First_ground.png')


    def update(self):
        self.first_x -= self.speed
        self.second_x -= self.speed

        if self.first_x <= 400:
            self.second_x = self.first_x + 800

        if self.second_x <= 400:
            self.first_x = self.second_x + 800


    def draw(self):
        self.ground_first.draw(self.first_x, self.first_y)
        self.ground_second.draw(self.second_x, self.second_y)