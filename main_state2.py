import random
import json
import os

from pico2d import *
from Player import *
from Background import *
from Ground import *
from Hurdle_second import *
from Pet import *
import game_framework
import title_state
#import Player

name = "MainState"

font = None
player = None
pet = None
background = None
ground = None
hurdle = []
current_time = 0.0


def enter():
    global player, background, ground, hurdle, pet
    #if title_state.time == True:
    player = Player_second()
    background = Background_second()
    ground = Ground_second()
    pet = Pet_second()
    #for i in range(2):          # 장애물 종류
    #    for j in range(3):      # 물체 개수
    #        hurdle.append(Hurdle(i, j))

    for i in range(len_data['Stage2_Spear']['Len']):
        hurdle.append(Hurdle(len_data['Stage2_Spear']['num'], i))
    for i in range(len_data['Stage2_thorn2']['Len']):
        hurdle.append(Hurdle(len_data['Stage2_thorn2']['num'], i))
    for i in range(len_data['Stage2_thorn3']['Len']):
        hurdle.append(Hurdle(len_data['Stage2_thorn3']['num'], i))

##############################################################################
'''
    for i in range(len_data2['Stage1_Fork']['Len']):
        hurdle.append(Hurdle2(len_data2['Stage1_Fork']['num'], i))
    for i in range(len_data2['Stage1_thorn4']['Len']):
        hurdle.append(Hurdle2(len_data2['Stage1_thorn4']['num'], i))
    for i in range(len_data2['Stage1_thorn5']['Len']):
        hurdle.append(Hurdle2(len_data2['Stage1_thorn5']['num'], i))

################################################################################

    for i in range(len_data3['Stage1_Fork']['Len']):
        hurdle.append(Hurdle3(len_data3['Stage1_Fork']['num'], i))
    for i in range(len_data3['Stage1_Fork2']['Len']):
        hurdle.append(Hurdle3(len_data3['Stage1_Fork2']['num'], i))
    for i in range(len_data3['Stage1_thorn4']['Len']):
        hurdle.append(Hurdle3(len_data3['Stage1_thorn4']['num'], i))


################################################################################

    for i in range(len_data4['Stage1_Fork']['Len']):
        hurdle.append(Hurdle4(len_data4['Stage1_Fork']['num'], i))
    for i in range(len_data4['Stage1_Fork2']['Len']):
        hurdle.append(Hurdle4(len_data4['Stage1_Fork2']['num'], i))
    for i in range(len_data4['Stage1_thorn']['Len']):
        hurdle.append(Hurdle4(len_data4['Stage1_thorn']['num'], i))
    for i in range(len_data4['Stage1_thorn4']['Len']):
        hurdle.append(Hurdle4(len_data4['Stage1_thorn4']['num'], i))
    for i in range(len_data4['Stage1_thorn5']['Len']):
        hurdle.append(Hurdle4(len_data4['Stage1_thorn5']['num'], i))

##################################################################################

    for i in range(len_data5['Stage1_Fork']['Len']):
        hurdle.append(Hurdle5(len_data5['Stage1_Fork']['num'], i))
    for i in range(len_data5['Stage1_Fork2']['Len']):
        hurdle.append(Hurdle5(len_data5['Stage1_Fork2']['num'], i))
    for i in range(len_data5['Stage1_thorn4']['Len']):
        hurdle.append(Hurdle5(len_data5['Stage1_thorn4']['num'], i))
    for i in range(len_data5['Stage1_thorn5']['Len']):
        hurdle.append(Hurdle5(len_data5['Stage1_thorn5']['num'], i))
'''

def exit():
    global player, background, ground, hurdle, pet
    del(player)
    del(background)
    del(ground)
    del(hurdle)
    del(pet)

def pause():
    pass


def resume():
    pass

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


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

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True


def update():
    global player, background, ground, hurdle, pet

    frame_time = get_frame_time()
    background.update(frame_time)
    ground.update(frame_time)
    player.update(frame_time)
    pet.update(frame_time)
    for i in hurdle:
        i.update(frame_time, background.Count_copy)
        if collide(player, i):
            print("충돌")
    #delay(0.03)

def draw():
    global player, background, hurdle, pet
    #뒤부터 출력순서를 정한다.
    clear_canvas()
    background.draw()

    if background.frame <= 1:
        ground.draw()

    for i in hurdle:
        i.draw()
        i.draw_bb()

    player.draw()
    player.draw_bb()
    pet.draw(player.x, player.y, player.state)
    update_canvas()
    #delay(0.03)





