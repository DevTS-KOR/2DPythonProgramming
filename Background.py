from pico2d import *

import random
import json
import os
import title_state

class Background:
    Image_init = None
    PIXEL_PER_METER = (10.0 / 0.3)                  #10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.first_x = 400
        self.first_y = 400
        self.second_x = 1200
        self.second_y = 400
        self.distance = 0
        self.Count = 0
        self.dir = 1
        self.total_frames = 0.0
        self.sum_first_distance = 0.0
        self.sum_second_distance = 0.0
        #self.first_move = False
        #self.second_move = True
        if Background.Image_init == None:
            self.background_first = load_image('Image\\First_Background.png')
            self.background_second = load_image('Image\\First_Background.png')
            self.background_rotate = load_image('Image\\Rotate\\First_Background_Rotate.png')

        self.frame = 0
        self.speed = 5

    def update(self, frame_time):
        if Background.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 6.5
        else:
            self.distance = Background.RUN_SPEED_PPS * frame_time

        #print(Background.RUN_SPEED_PPS * frame_time)
       # print(self.first_x)
        #print(self.second_x)
        #if  self.first_move == True:
        self.first_x -= self.distance
            #self.sum_first_distance += self.distance
        #if  self.second_move == True:
        self.second_x -= self.distance
            #self.sum_second_distance += self.distance

        #self.first_x -= (self.dir * self.distance)
        #self.second_x -= (self.dir * self.distance)

        if self.second_x < -400:
            self.sum_second_distance = 0
            self.first_move = True
            self.second_move = False
            self.Count += 1
            self.second_x = 1190

        if self.first_x < -400:
            self.sum_first_distance = 0
            self.first_move = False
            self.second_move = True
            self.Count += 1
            self.first_x = 1190

        if self.Count >= 5:
            self.first_x = 400
            self.first_y = 400

            if self.frame == 8:
                self.frame = 8
            else:
                self.frame = (self.frame + 1) % 9
                #delay(0.1)


        print(self.Count)
                #game_framework.change_state(title_state)

        '''
         self.second_x += sin(angle * 3.14 / 180) * 100
         self.second_y -= cos(angle * 3.14 / 180) * 100

        x += sin(angle * 3.14 / 180) * 100
        y -= cos(angle * 3.14 / 180) * 100

        self.first_x -= self.speed
        self.second_x -= self.speed
        self.frame = self.frame + 1


        if self.frame % 10 == 0:
            self.Speed += 0.1


        if self.second_x == 400:
            self.first_x = 1200

        if self.first_x == 400:
            self.second_x = 1200
        '''



    def draw(self):
        if self.Count >= 5:
           self.background_rotate.clip_draw(self.frame * 800, 0, 800, 800, self.first_x, self.first_y)
           delay(0.05)
        else:
            self.background_first.draw(self.first_x, self.first_y)
            self.background_second.draw(self.second_x, self.second_y)