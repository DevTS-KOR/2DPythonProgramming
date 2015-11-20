from pico2d import *
import json


hurdle_data_file = open('MapData\\FirstMap_hurdle1.txt', 'r')
hurdle_data = json.load(hurdle_data_file)
hurdle_data_file.close()

hurdle_len_file = open('MapData\\TypeOfHurdle1.txt', 'r')
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
    nn = 0

    def hurdle_move(self, frame_time):

        if Hurdle.RUN_SPEED_PPS * frame_time > 13:
            self.distance = 5
        else:
            self.distance = Hurdle.RUN_SPEED_PPS * frame_time
            #self.distance += (Hurdle.RUN_SPEED_PPS / 10) * (frame_time / 10000)
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
        self.sum = 0
        self.width = 0
        self.height = 0
        self.arr = None
        self.rotate = False
        self.Hurdle_Start1 = False
        Hurdle.nn += 1
        self.state = "None"
        print(self.x)
        if HurdleType == len_data['Stage1_Fork']['num']:
            self.arr = len_data['Stage1_Fork']
        elif HurdleType == len_data['Stage1_Fork2']['num']:
            self.arr = len_data['Stage1_Fork2']
        elif HurdleType == len_data['Stage1_thorn']['num']:
            self.arr = len_data['Stage1_thorn']
        elif HurdleType == len_data['big_jelly']['num']:
            self.arr = len_data['big_jelly']
        elif HurdleType == len_data['item_jelly']['num']:
            self.arr = len_data['item_jelly']

        self.image = load_image(self.arr['dir'])
        self.width = self.arr['width']
        self.height = self.arr['height']

    def __del__(self):
        pass

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
            self.Hurdle_Start1 = True

        if self.Hurdle_Start1 == True and self.state != "Collid":
            self.hurdle_move(frame_time)
            self.sum = 0

        elif self.Hurdle_Start1 == True and self.state == "Collid":
            if self.sum < 30:

                self.sum += 10
                for i in range(2):
                    if self.x > 150:
                        self.x += 20
                    else:
                        self.x -= 20

    def get_bb(self):
        return self.x - self.width/2, self. y - self.height/2, self.x + self.width/2, self.y + self.height/2
           #return self.x + 50 , self.y + 50, self.x - 50, self.y - 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        if self.Hurdle_Start1 == True:
            self.image.draw(self.x, self.y)


class Hurdle2:
    global hurdle_data2
    PIXEL_PER_METER = (10.0 / 0.08)                  #10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    #state = "None"
    STAND = 0
    nn = 0

    def hurdle_move(self, frame_time):

        if Hurdle2.RUN_SPEED_PPS * frame_time > 13:
            self.distance = 5
        else:
            self.distance = Hurdle2.RUN_SPEED_PPS * frame_time
            #self.distance += (Hurdle2.RUN_SPEED_PPS / 10) * (frame_time / 10000)
            self.x -= self.distance


    hurdle_state = {
        STAND: hurdle_move
    }

    def __init__(self, HurdleType, num):
        self.x = hurdle_data2[HurdleType][num * 2]
        self.y = hurdle_data2[HurdleType][num * 2 + 1]
        self.speed = 10
        self.name = 'noname'
        self.image = None
        self.distance = 0
        self.sum = 0
        self.width = 0
        self.height = 0
        self.arr = None
        self.state = "None"
        self.Hurdle_Start2 = False
        Hurdle2.nn += 1
        if HurdleType == len_data2['Stage1_Fork']['num']:
            self.arr = len_data2['Stage1_Fork']
        elif HurdleType == len_data2['Stage1_thorn4']['num']:
            self.arr = len_data2['Stage1_thorn4']
        elif HurdleType == len_data2['Stage1_thorn5']['num']:
            self.arr = len_data2['Stage1_thorn5']
        elif HurdleType == len_data2['item_jelly']['num']:
            self.arr = len_data2['item_jelly']

        self.image = load_image(self.arr['dir'])
        self.width = self.arr['width']
        self.height = self.arr['height']

    def __del__(self):
        pass

    def create(self, num):
        hurdle2 = []
        for i in range(2):
            self.name = "택수"
            self.x = hurdle_data2[i]['x']
            self.y = hurdle_data2[i]['y']
            hurdle2.append(self)

        return hurdle2


    def update(self, frame_time, Count_copy):
        global Hurdle_Start2, random_draw2

        if Count_copy >= 2:
            self.Hurdle_Start2 = True

        if self.Hurdle_Start2 == True and self.state != "Collid":
            self.hurdle_move(frame_time)
            self.sum = 0

        elif self.Hurdle_Start2 == True and self.state == "Collid":
            if self.sum < 30:
                self.sum += 10
                for i in range(2):
                    if self.x > 150:
                        self.x += 20
                    else:
                        self.x -= 20

    def draw(self):
        if self.Hurdle_Start2 == True:
            self.image.draw(self.x, self.y)


    def get_bb(self):
            return self.x - self.width/2, self. y - self.height/2, self.x + self.width/2, self.y + self.height/2
            #return self.x + 50 , self.y + 50, self.x - 50, self.y - 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Hurdle3:
    global hurdle_data3
    PIXEL_PER_METER = (10.0 / 0.08)                  #10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    state = "None"
    STAND = 0

    def hurdle_move(self, frame_time):

        if Hurdle3.RUN_SPEED_PPS * frame_time > 13:
            self.distance = 5
        else:
            self.distance = Hurdle3.RUN_SPEED_PPS * frame_time
            #self.distance += (Hurdle3.RUN_SPEED_PPS / 10) * (frame_time / 10000)
            self.x -= self.distance

    hurdle_state = {
        STAND: hurdle_move
    }

    def __init__(self, HurdleType, num):
        self.x = hurdle_data3[HurdleType][num * 2]
        self.y = hurdle_data3[HurdleType][num * 2 + 1]
        self.speed = 10
        self.name = 'noname'
        self.image = None
        self.distance = 0
        self.sum = 0
        self.width = 0
        self.height = 0
        self.arr = None
        self.Hurdle_Start3 = False


        if HurdleType == len_data3['Stage1_Fork']['num']:
            self.arr = len_data3['Stage1_Fork']
        elif HurdleType == len_data3['Stage1_Fork2']['num']:
            self.arr = len_data3['Stage1_Fork2']
        elif HurdleType == len_data3['Stage1_thorn4']['num']:
            self.arr = len_data3['Stage1_thorn4']
        elif HurdleType == len_data3['item_jelly']['num']:
            self.arr = len_data3['item_jelly']

        self.image = load_image(self.arr['dir'])
        self.width = self.arr['width']
        self.height = self.arr['height']

    def create(self, num):
        hurdle3 = []
        for i in range(2):
            self.name = "택수"
            self.x = hurdle_data3[i]['x']
            self.y = hurdle_data3[i]['y']
            hurdle3.append(self)

        return hurdle3


    def update(self, frame_time, Count_copy):
        global Hurdle_Start3

        if Count_copy >= 3:
            self.Hurdle_Start3 = True

        if self.Hurdle_Start3 == True and self.state != "Collid":
            self.hurdle_move(frame_time)
            self.sum = 0

        elif self.Hurdle_Start3 == True and self.state == "Collid":
            if self.sum < 30:
                self.sum += 10
                for i in range(2):
                    if self.x > 150:
                        self.x += 20
                    else:
                        self.x -= 20

    def draw(self):
        if self.Hurdle_Start3 == True:
            self.image.draw(self.x, self.y)


    def get_bb(self):
            return self.x - self.width/2, self. y - self.height/2, self.x + self.width/2, self.y + self.height/2
            #return self.x + 50 , self.y + 50, self.x - 50, self.y - 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Hurdle4:
    global hurdle_dat4
    PIXEL_PER_METER = (10.0 / 0.08)                  #10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    state = "None"
    STAND = 0

    def hurdle_move(self, frame_time):

        if Hurdle4.RUN_SPEED_PPS * frame_time > 13:
            self.distance = 5
        else:
            self.distance = Hurdle4.RUN_SPEED_PPS * frame_time
            #self.distance += (Hurdle4.RUN_SPEED_PPS / 10) * (frame_time / 10000)
            self.x -= self.distance

    hurdle_state = {
        STAND: hurdle_move
    }

    def __init__(self, HurdleType, num):
        self.x = hurdle_data4[HurdleType][num * 2]
        self.y = hurdle_data4[HurdleType][num * 2 + 1]
        self.speed = 10
        self.name = 'noname'
        self.image = None
        self.distance = 0
        self.sum = 0
        self.width = 0
        self.height = 0
        self.arr = None
        self.Hurdle_Start4 = False

        if HurdleType == len_data4['Stage1_Fork']['num']:
            self.arr = len_data4['Stage1_Fork']
        elif HurdleType == len_data4['Stage1_Fork2']['num']:
            self.arr = len_data4['Stage1_Fork2']
        elif HurdleType == len_data4['Stage1_thorn']['num']:
            self.arr = len_data4['Stage1_thorn']
        elif HurdleType == len_data4['Stage1_thorn4']['num']:
            self.arr = len_data4['Stage1_thorn4']
        elif HurdleType == len_data4['Stage1_thorn5']['num']:
            self.arr = len_data4['Stage1_thorn5']
        elif HurdleType == len_data4['item_jelly']['num']:
            self.arr = len_data4['item_jelly']

        self.image = load_image(self.arr['dir'])
        self.width = self.arr['width']
        self.height = self.arr['height']

    def create(self, num):
        hurdle4 = []
        for i in range(2):
            self.name = "택수"
            self.x = hurdle_data4[i]['x']
            self.y = hurdle_data4[i]['y']
            hurdle4.append(self)

        return hurdle4


    def update(self, frame_time, Count_copy):
        global Hurdle_Start4

        if Count_copy >= 4:
            self.Hurdle_Start4 = True

        if self.Hurdle_Start4 == True and self.state != "Collid":
            self.hurdle_move(frame_time)
            self.sum = 0

        elif self.Hurdle_Start4 == True and self.state == "Collid":
            if self.sum < 30:
                self.sum += 10
                for i in range(2):
                    if self.x > 150:
                        self.x += 20
                    else:
                        self.x -= 20


    def draw(self):
        if self.Hurdle_Start4 == True:
            self.image.draw(self.x, self.y)


    def get_bb(self):
        return self.x - self.width/2, self. y - self.height/2, self.x + self.width/2, self.y + self.height/2
           #return self.x + 50 , self.y + 50, self.x - 50, self.y - 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Hurdle5:
    global hurdle_dat5
    PIXEL_PER_METER = (10.0 / 0.08)                  #10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    state = "None"
    #Image_init = None
    STAND = 0

    def hurdle_move(self, frame_time):

        if Hurdle5.RUN_SPEED_PPS * frame_time > 13:
            self.distance = 5
        else:
            self.distance = Hurdle5.RUN_SPEED_PPS * frame_time
            #self.distance += (Hurdle5.RUN_SPEED_PPS / 10) * (frame_time / 10000)
            self.x -= self.distance

    hurdle_state = {
        STAND: hurdle_move
    }

    def __init__(self, HurdleType, num):
        self.x = hurdle_data5[HurdleType][num * 2]
        self.y = hurdle_data5[HurdleType][num * 2 + 1]
        self.speed = 10
        self.name = 'noname'
        self.image = None
        self.distance = 0
        self.sum = 0
        self.width = 0
        self.height = 0
        self.arr = None
        self.Hurdle_Start5 = False

        if HurdleType == len_data5['Stage1_Fork']['num']:
            self.arr = len_data5['Stage1_Fork']
        elif HurdleType == len_data5['Stage1_Fork2']['num']:
            self.arr = len_data5['Stage1_Fork2']
        elif HurdleType == len_data5['Stage1_thorn4']['num']:
            self.arr = len_data5['Stage1_thorn4']
        elif HurdleType == len_data5['Stage1_thorn5']['num']:
            self.arr = len_data5['Stage1_thorn5']
        elif HurdleType == len_data5['item_jelly']['num']:
            self.arr = len_data5['item_jelly']
        elif HurdleType == len_data5['hp_jelly']['num']:
            self.arr = len_data5['hp_jelly']

        self.image = load_image(self.arr['dir'])
        self.width = self.arr['width']
        self.height = self.arr['height']

    def create(self, num):
        hurdle5 = []
        for i in range(2):
            self.name = "택수"
            self.x = hurdle_data5[i]['x']
            self.y = hurdle_data5[i]['y']
            hurdle5.append(self)

        return hurdle5


    def update(self, frame_time, Count_copy):
        global Hurdle_Start5

        if Count_copy >= 5:
            self.Hurdle_Start5 = True

        if self.Hurdle_Start5 == True and self.state != "Collid":
            self.hurdle_move(frame_time)
            self.sum = 0

        elif self.Hurdle_Start5 == True and self.state == "Collid":
            if self.sum < 30:
                self.sum += 10
                for i in range(2):
                    if self.x > 150:
                        self.x += 20
                    else:
                        self.x -= 20

    def draw(self):
        if self.Hurdle_Start5 == True:
            self.image.draw(self.x, self.y)


    def get_bb(self):
        return self.x - self.width/2, self. y - self.height/2, self.x + self.width/2, self.y + self.height/2
           #return self.x + 50 , self.y + 50, self.x - 50, self.y - 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Hurdle_second:
    global hurdle_data
    PIXEL_PER_METER = (10.0 / 0.08)                  #10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    STAND = 0

    def hurdle_move(self, frame_time):

        if Hurdle_second.RUN_SPEED_PPS * frame_time > 13:
            self.distance = 12
        else:
            self.distance = Hurdle_second.RUN_SPEED_PPS * frame_time

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
