import random
import json
import os

from pico2d import *
from Player import *
from Background import *
from Ground import *

import game_framework
import title_state
#import Player


name = "MainState"

font = None
player = None
background = None
ground = None

def enter():
    global player, background, ground
    player = Player()
    background = Background()
    ground = Ground()


def exit():
    global player, background, ground
    del(player)
    del(background)
    del(ground)

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
    global player, background, ground
    background.update()
    ground.update()
    player.update()


def draw():
    global player, background
    #뒤부터 출력순서를 정한다.
    clear_canvas()
    background.draw()
    ground.draw()
    player.draw()
    update_canvas()
    delay(0.03)





