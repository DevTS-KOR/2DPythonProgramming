from pico2d import *

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
        self.sum = 0
        self.distance = 0
        self.Count = 0
        self.Count_copy = 0
        self.dir = 1
        self.total_frames = 0.0
        self.sum_first_distance = 0.0
        self.sum_second_distance = 0.0
        if Background.Image_init == None:
            self.background_first = load_image('Image\\First_Background.png')
            self.background_second = load_image('Image\\First_Background.png')
            self.background_rotate = load_image('Image\\Rotate\\First_Background_Rotate.png')

        self.frame = 0
        self.speed = 5

    def update(self, frame_time, state):
        if Background.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 6.5
        else:
            self.distance = Background.RUN_SPEED_PPS * frame_time

        if state == "Collid":
            self.distance = 0
            if self.sum < 30:
                self.first_x += 20
                self.second_x += 20
                self.sum += 10
        else:
            self.first_x -= self.distance
            self.second_x -= self.distance
            self.sum = 0

        if self.second_x < -400:
            self.sum_second_distance = 0
            self.first_move = True
            self.second_move = False
            self.Count += 1
            self.Count_copy += 1
            self.second_x = 1190

        if self.first_x < -400:
            self.sum_first_distance = 0
            self.first_move = False
            self.second_move = True
            self.Count += 1
            self.Count_copy += 1
            self.first_x = 1190

        if self.Count >= 7:
            self.first_x = 400
            self.first_y = 400


            if self.frame == 8:
                self.frame = 8

            else:
                self.frame = (self.frame + 1) % 9


    def draw(self):
        if self.Count >= 7:
           self.background_rotate.clip_draw(self.frame * 800, 0, 800, 800, self.first_x, self.first_y)
           delay(0.05)
        else:
            self.background_first.draw(self.first_x, self.first_y)
            self.background_second.draw(self.second_x, self.second_y)



class Background_second:
    Image_init = None
    PIXEL_PER_METER = (10.0 / 0.3)                  #10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.first_x = 400
        self.first_y = 400
        self.second_x = 400
        self.second_y = 1200
        self.distance = 0
        self.Count = 0
        self.Count_copy = 0
        self.dir = 1
        self.total_frames = 0.0
        self.sum_first_distance = 0.0
        self.sum_second_distance = 0.0
        if Background_second.Image_init == None:
            self.background_first = load_image('Image\\Second_Background.png')
            self.background_second = load_image('Image\\Second_Background2.png')
            self.background_rotate = load_image('Image\\Rotate\\Second_Background_Rotate.png')

        self.frame = 0
        self.speed = 5

    def update(self, frame_time):
        if Background_second.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 6.5
        else:
            self.distance = Background_second.RUN_SPEED_PPS * frame_time

        self.first_y -= self.distance
        self.second_y -= self.distance

        if self.second_y < -400:
            self.sum_second_distance = 0
            self.first_move = True
            self.second_move = False
            self.Count += 1
            self.Count_copy += 1
            self.second_y = 1190

        if self.first_y < -400:
            self.sum_first_distance = 0
            self.first_move = False
            self.second_move = True
            self.Count += 1
            self.Count_copy += 1
            self.first_y = 1190

        if self.Count >= 7:
            self.first_x = 400
            self.first_y = 400


            if self.frame == 8:
                self.frame = 8

            else:
                self.frame = (self.frame + 1) % 9


    def draw(self):
        if self.Count >= 7:
           self.background_rotate.clip_draw(self.frame * 800, 0, 800, 800, self.first_x, self.first_y)
           delay(0.05)
        else:
            self.background_first.draw(self.first_x, self.first_y)
            self.background_second.draw(self.second_x, self.second_y)