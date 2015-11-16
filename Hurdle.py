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

#####################################################################

hurdle_data_file2 = open('MapData\\FirstMap_hurdle2.txt', 'r')
hurdle_data2 = json.load(hurdle_data_file2)
hurdle_data_file2.close()

hurdle_len_file2 = open('MapData\\TypeOfHurdle2.txt', 'r')
len_data2 = json.load(hurdle_len_file2)
hurdle_len_file2.close()

Hurdle_Start = False

class Hurdle:
    global hurdle_data
    PIXEL_PER_METER = (10.0 / 0.08)                  #10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    #Image_init = None
    STAND = 0

    def hurdle_move(self, frame_time):

        if Hurdle.RUN_SPEED_PPS * frame_time > 13:
            self.distance = 12
        else:
            self.distance = Hurdle.RUN_SPEED_PPS * frame_time

            self.x -= self.distance

    hurdle_state = {
        STAND: hurdle_move
    }
    def __init__(self, HurdleType, num):
        self.x = hurdle_data[HurdleType][num * 2]
        self.y = hurdle_data[HurdleType][num * 2 + 1]
        self.speed = 10
        self.distance = 0
        self.name = 'noname'
        self.image = None

        if HurdleType == len_data['PORK']['num'] :
            self.image = load_image(len_data['PORK']['dir'])
        elif HurdleType == len_data['THORN']['num']:
            self.image = load_image(len_data['THORN']['dir'])

    def create(self, num):

        hurdle = []
        for i in range(2):
            self.name = "택수"
            self.x = hurdle_data[i]['x']
            self.y = hurdle_data[i]['y']
            hurdle.append(self)

        return hurdle


    def update(self, frame_time, Count):
        global Hurdle_Start
        #print(self.x)
        if Count >= 1:
            Hurdle_Start = True

        if Hurdle_Start == True:
            self.hurdle_move(frame_time)

    def draw(self):
        if Hurdle_Start == True:
            self.image.draw(self.x, self.y)


class Hurdle2:
    global hurdle_data2
    PIXEL_PER_METER = (10.0 / 0.3)                  #10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    #Image_init = None
    STAND = 0

    def hurdle_move(self):
        self.x -= self.speed

    hurdle_state = {
        STAND: hurdle_move
    }
    def __init__(self, HurdleType, num):
        self.x = hurdle_data2[HurdleType][num * 2]
        self.y = hurdle_data2[HurdleType][num * 2 + 1]
        self.speed = 10
        self.name = 'noname'
        self.image = None

        if HurdleType == len_data2['PORK']['num'] :
            self.image = load_image(len_data2['PORK']['dir'])

    def create(self, num):

        hurdle2 = []
        for i in range(2):
            self.name = "택수"
            self.x = hurdle_data2[i]['x']
            self.y = hurdle_data2[i]['y']
            hurdle2.append(self)

        return hurdle2


    def update(self):
        pass
        #self.hurdle_move()

    def draw(self):
        self.image.draw(self.x, self.y)
