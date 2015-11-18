import random
import json
import os

from pico2d import *
from math import *
from Player import *
from Background import *
from Ground import *
from Hurdle import *
from Pet import *
import game_framework
import title_state
import main_state2

name = "MainState"

font = None
player = None
pet = None
background = None
ground = None
hurdle = []
current_time = 0.0
angle = 100


def enter():
    global player, background, ground, hurdle, pet
    #if title_state.time == True:
    player = Player()
    background = Background()
    ground = Ground()
    pet = Pet()
    #for i in range(2):          # 장애물 종류
    #    for j in range(3):      # 물체 개수
    #        hurdle.append(Hurdle(i, j))

    for i in range(len_data['Stage1_Fork']['Len']):
        hurdle.append(Hurdle(len_data['Stage1_Fork']['num'], i))
    for i in range(len_data['Stage1_Fork2']['Len']):
        hurdle.append(Hurdle(len_data['Stage1_Fork2']['num'], i))
    for i in range(len_data['Stage1_thorn']['Len']):
        hurdle.append(Hurdle(len_data['Stage1_thorn']['num'], i))
    for i in range(len_data['big_jelly']['Len']):
        hurdle.append(Hurdle(len_data['big_jelly']['num'], i))
    for i in range(len_data['item_jelly']['Len']):
        hurdle.append(Hurdle(len_data['item_jelly']['num'], i))

##############################################################################

    for i in range(len_data2['Stage1_Fork']['Len']):
        hurdle.append(Hurdle2(len_data2['Stage1_Fork']['num'], i))
    for i in range(len_data2['Stage1_thorn4']['Len']):
        hurdle.append(Hurdle2(len_data2['Stage1_thorn4']['num'], i))
    for i in range(len_data2['Stage1_thorn5']['Len']):
        hurdle.append(Hurdle2(len_data2['Stage1_thorn5']['num'], i))
    for i in range(len_data2['item_jelly']['Len']):
        hurdle.append(Hurdle2(len_data2['item_jelly']['num'], i))

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
    global player, background

    events = get_events()

    if background.frame >= 8:
        #print(background.frame)
        game_framework.change_state(main_state2)

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)

            elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
                game_framework.change_state(main_state2)

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
    global player, background, ground, hurdle, pet, angle, current_time


    frame_time = get_frame_time()
    background.update(frame_time, player.state)
    ground.update(frame_time, player.state)
    player.update(frame_time, player.score)
    pet.update(frame_time)

    for i in hurdle:
        i.update(frame_time, background.Count_copy)
        if collide(player, i) and player.big == False:
            if i.arr['dir'] == 'Image\\big_jelly.png':
                if player.state == "Slide":
                    player.state = "Slide_Big"

                else:
                    player.state = "Big"
                player.big = True
                player.big_time = player.total_frames
            #elif player.state == "Big":
                #print(frame_time)
            elif i.arr['dir'] == 'Image\\item_jelly.png':
                player.score += 1
                hurdle.remove(i)
            else:
                #print(i.arr['dir'])         #    Image\Stage1_Fork.png
                player.state = "Collid"
                for i in hurdle:
                    i.state = "Collid"
        elif  player.state == "Run" or player.state == "Slide" or player.state == "Jump":
            for i in hurdle:
                i.state = "None"
        elif collide(player, i) and player.big == True:
                i.y += 800
                if i.arr['dir'] == 'Image\\item_jelly.png':
                    player.score += 1
                    hurdle.remove(i)
                #i.x -= cos(angle * 3.14 / 180) * 100
                #i.y += sin(angle * 3.14 / 180) * 100
                #angle += 50
            #angle += 50
        #else:
            #player.state = "Run"
            #i.state = "None"
            #player.state = "Run"
            #background.distance = 0
            #ground.distance = 0



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

    #hurdle.draw_bb()
    player.draw()
    player.draw_bb()
    pet.draw(player.x, player.y, player.state)
    update_canvas()
    #delay(0.03)






