from pico2d import *

import random
import json
import os
import title_state

class Background:
    Image_init = None

    def __init__(self):
        self.x = 400
        self.y = 400
        if Background.Image_init == None:
            self.background = load_image('Image\\First_Background.png')

        self.speed = 0

    def update(self):
        self.x -= 10
        self.y -= 10


    def draw(self):
        self.background.draw(400, 400)