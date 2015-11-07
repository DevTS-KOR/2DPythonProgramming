import random
import json
import os

from pico2d import *
from Player import *
from Background import *
from Ground import *
from Hurdle import *

import game_framework
import title_state
#import Player

name = "MainState"

font = None
player = None
background = None
ground = None
hurdle = []
hurdle2 = []

def enter():
    global player, background, ground, hurdle, hurdle2
    player = Player()
    background = Background()
    ground = Ground()
    #for i in range(2):          # 장애물 종류
    #    for j in range(3):      # 물체 개수
    #        hurdle.append(Hurdle(i, j))

    for i in range(len_data['PORK']['Len']) :
        hurdle.append(Hurdle(len_data['PORK']['num'], i))
    for i in range(len_data['THORN']['Len']):
        hurdle.append(Hurdle(len_data['THORN']['num'], i))

    for i in range(len_data2['PORK']['Len']) :
        hurdle2.append(Hurdle2(len_data2['PORK']['num'], i))


def exit():
    global player, background, ground, hurdle, hurdle2
    del(player)
    del(background)
    del(ground)
    del(hurdle)
    del(hurdle2)

def pause():
    pass


def resume():
    pass


def handle_events():
    global player

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)

            else:
                player.handle_events(event)


def update():
    global player, background, ground, hurdle, hurdle2
    background.update()
    ground.update()
    player.update()
    for i in hurdle:
        i.update()
    for i in hurdle2:
        i.update()


def draw():
    global player, background, hurdle, hurdle2
    #뒤부터 출력순서를 정한다.
    clear_canvas()
    background.draw()
    ground.draw()
    for i in hurdle:
        i.draw()
    for i in hurdle2:
        i.draw()

    player.draw()
    update_canvas()
    delay(0.03)





