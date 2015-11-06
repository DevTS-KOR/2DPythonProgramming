import random
import json
import os

from pico2d import *
from Player import *
from Background import *

import game_framework
import title_state
#import Player


name = "MainState"

font = None
player = None
background = None

def enter():
    global player, background
    player = Player()
    background = Background()


def exit():
    global player, background
    del(player)
    del(background)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)


def update():
    global player, background
    background.update()
    player.update()


def draw():
    global player, background
    #뒤부터 출력순서를 정한다.
    clear_canvas()
    background.draw()
    player.draw()
    update_canvas()





