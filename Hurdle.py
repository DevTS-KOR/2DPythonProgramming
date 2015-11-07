from pico2d import *

import random
import json
import os
import title_state

hurdle_data_file = open('MapData\\FirstMap_hurdle1.txt', 'r')
hurdle_data = json.load(hurdle_data_file)
hurdle_data_file.close()

hurdle_len_file = open('MapData\\TypeOfHurdle.txt', 'r')
len_data = json.load(hurdle_len_file)
hurdle_len_file.close()


class Hurdle:
    global hurdle_data

    #Image_init = None
    STAND = 0

    def hurdle_move(self):
        self.x -= self.speed

    hurdle_state = {
        STAND: hurdle_move
    }
    def __init__(self, HurdleType, num):
        self.x = hurdle_data[HurdleType][num * 2]
        self.y = hurdle_data[HurdleType][num * 2 + 1]
        self.speed = 10
        self.name = 'noname'
        self.image = None

        #if Hurdle.Image_init == None:
        if HurdleType == len_data['PORK']['num'] :
            self.image = load_image(len_data['PORK']['dir'])
        elif HurdleType == len_data['THORN']['num']:
            self.image = load_image(len_data['THORN']['dir'])


        #self.create(num)
        #self.state = self.STAND


    def create(self, num):

        #create_hurdle = {
        #    "STAND" : self.STAND
        #}



        hurdle = []
        for i in range(2):
            #player = Boy()

            self.name = "택수"
            self.x = hurdle_data[i]['x']
            self.y = hurdle_data[i]['y']
            #self.state = create_hurdle[hurdle_data[name]['StartState']]

            hurdle.append(self)

        return hurdle


    def update(self):
        self.hurdle_move()
        #self.hurdle_state[self.state](self)
        #self.x -= self.speed


    def draw(self):

        #self.create()
        self.image.draw(self.x, self.y)
