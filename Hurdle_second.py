from pico2d import *

import json

hurdle_data_file = open('MapData\\SecondMap_hurdle1.txt', 'r')
hurdle_data = json.load(hurdle_data_file)
hurdle_data_file.close()

hurdle_len_file = open('MapData\\Second_TypeOfHurdle1.txt', 'r')
len_data = json.load(hurdle_len_file)
hurdle_len_file.close()

#####################################################################

hurdle_data_file2 = open('MapData\\FirstMap_hurdle2.txt', 'r')
hurdle_data2 = json.load(hurdle_data_file2)
hurdle_data_file2.close()

hurdle_len_file2 = open('MapData\\TypeOfHurdle2.txt', 'r')
len_data2 = json.load(hurdle_len_file2)
hurdle_len_file2.close()

#####################################################################

hurdle_data_file3 = open('MapData\\FirstMap_hurdle3.txt', 'r')
hurdle_data3 = json.load(hurdle_data_file3)
hurdle_data_file3.close()

hurdle_len_file3 = open('MapData\\TypeOfHurdle3.txt', 'r')
len_data3 = json.load(hurdle_len_file3)
hurdle_len_file3.close()

#####################################################################

hurdle_data_file4 = open('MapData\\FirstMap_hurdle4.txt', 'r')
hurdle_data4 = json.load(hurdle_data_file4)
hurdle_data_file4.close()

hurdle_len_file4 = open('MapData\\TypeOfHurdle4.txt', 'r')
len_data4 = json.load(hurdle_len_file4)
hurdle_len_file4.close()

######################################################################

hurdle_data_file5 = open('MapData\\FirstMap_hurdle5.txt', 'r')
hurdle_data5 = json.load(hurdle_data_file5)
hurdle_data_file5.close()

hurdle_len_file5 = open('MapData\\TypeOfHurdle5.txt', 'r')
len_data5 = json.load(hurdle_len_file5)
hurdle_len_file5.close()

Hurdle_Start1 = False
Hurdle_Start2 = False
Hurdle_Start3 = False
Hurdle_Start4 = False
Hurdle_Start5 = False
random_resource = [0, 1, 2, 3, 4, 5, 6, 7]
draw_count1 = 0
draw_count2 = 0

class Hurdle:
    global hurdle_data
    PIXEL_PER_METER = (10.0 / 0.08)                  #10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    STAND = 0

    def hurdle_move(self, frame_time):

        if Hurdle.RUN_SPEED_PPS * frame_time > 13:
            self.distance = 12
        else:
            self.distance = Hurdle.RUN_SPEED_PPS * frame_time

            self.y -= self.distance

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

        self.width = 0
        self.height = 0
        self.arr = None

        if HurdleType == len_data['Stage2_Spear']['num']:
            self.arr = len_data['Stage2_Spear']
        elif HurdleType == len_data['Stage2_thorn2']['num']:
            self.arr = len_data['Stage2_thorn2']
        elif HurdleType == len_data['Stage2_thorn3']['num']:
            self.arr = len_data['Stage2_thorn3']

        self.image = load_image(self.arr['dir'])
        self.width = self.arr['width']
        self.height = self.arr['height']


    def create(self, num):
        hurdle = []
        for i in range(2):
            self.name = "택수"
            self.x = hurdle_data[i]['x']
            self.y = hurdle_data[i]['y']
            hurdle.append(self)

        return hurdle


    def update(self, frame_time, Count_copy):
        global Hurdle_Start1, random_draw1

        if Count_copy >= 1:
            Hurdle_Start1 = True

        if Hurdle_Start1 == True:
            self.hurdle_move(frame_time)

    def get_bb(self):
        return self.x - self.width/2, self. y - self.height/2, self.x + self.width/2, self.y + self.height/2
           #return self.x + 50 , self.y + 50, self.x - 50, self.y - 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        if Hurdle_Start1 == True:
            self.image.draw(self.x, self.y)
