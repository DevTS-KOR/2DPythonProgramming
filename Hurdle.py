from pico2d import *

import random
import json
import os
import title_state

class Hurdle:
    Image_init = None
    stand = 0

    def hurdle_move(self):
        self.x -= self.speed

    hurdle_state = {
        stand: hurdle_move
    }
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 10

        if Hurdle.Image_init == None:
            self.fork = load_image('Image\\Stage1_Fork.png')

        self.state = self.stand


    def create(self):

        create_hurdle = {
            "STAND" : self.state
        }

        hurdle_data_file = open('MapData\\FirstMap_hurdle1.txt', 'r')
        hurdle_data = json.load(hurdle_data_file)
        hurdle_data_file.close()

        hurdle = []
        for name in hurdle_data:
            #player = Boy()
            self.name = name
            self.x = hurdle_data[name]['x']
            self.y = hurdle_data[name]['y']
            self.state = create_hurdle[hurdle_data[name]['StartState']]
            hurdle.append(self)

        return hurdle


    def update(self):
        self.hurdle_state[self.state](self)
        self.create()
        #self.x -= self.speed


    def draw(self):
        #self.create()
        self.fork.draw(self.x, self.y)