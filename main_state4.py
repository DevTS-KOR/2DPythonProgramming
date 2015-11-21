import random
import json
import os

from pico2d import *
from Player import *
from Background import *
from Ground import *
from Hurdle import *
from Pet import *
import game_framework
import title_state
#import main_state
import lobby
import main_state
import converter

name = "MainState2"

font = None
player = None
pet = None
background = None
ground = None
hurdle = None
current_time = 0.0
angle = 100
result_count = 0
hurdle_start = None
gaint_sound = None
collid_sound = None
jelly_sound = None
big_collid_sound = None
hp_sound = None
result_ok_sound = None
x, y = 0, 0

hpsize_of_main_state = None


def enter():
    global player, background, ground, hurdle, pet, hurdle_start
    global gaint_sound, collid_sound, jelly_sound, big_collid_sound, hp_sound, result_ok_sound
    #if title_state.time == True:
    hurdle = list()

    background = Background_four()
    ground = Ground_four()
    player = Player_four()
    player.score = converter.player_score
    pet = Pet_four()

    #Hurdle.__init__()
    #player.__init__()
    ground.__init__()

    Hurdle.Hurdle_Start1 = False
    Hurdle.Hurdle_Start2 = False
    Hurdle.Hurdle_Start3 = False
    Hurdle.Hurdle_Start4 = False
    Hurdle.Hurdle_Start5 = False

    ######사운드 관련#####

    #player.bgm.repeat_play()
    if gaint_sound == None:
        gaint_sound = load_wav('Sound\\i_giant.wav')
        gaint_sound.set_volume(128)

    if collid_sound == None:
        collid_sound = load_wav('Sound\\collide.wav')
        collid_sound.set_volume(64)

    if jelly_sound == None:
        jelly_sound = load_wav('Sound\\g_jelly.wav')
        jelly_sound.set_volume(32)

    if big_collid_sound == None:
        big_collid_sound = load_wav('Sound\\big_hit.wav')
        big_collid_sound.set_volume(128)

    if hp_sound == None:
        hp_sound = load_wav('Sound\\i_large_energy.wav')
        hp_sound.set_volume(128)

    if result_ok_sound == None:
        result_ok_sound = load_wav('Sound\\ui_2.wav')
        result_ok_sound.set_volume(128)

    #for i in range(2):          # 장애물 종류
    #    for j in range(3):      # 물체 개수
    #        hurdle.append(Hurdle(i, j))
    if hurdle_start == None:
        for i in range(len_data4_1['Stage4_Spear']['Len']):
            hurdle.append(Hurdle_four(len_data4_1['Stage4_Spear']['num'], i))
        for i in range(len_data4_1['Stage4_Spear2']['Len']):
            hurdle.append(Hurdle_four(len_data4_1['Stage4_Spear2']['num'], i))
        for i in range(len_data4_1['Stage4_thorn']['Len']):
            hurdle.append(Hurdle_four(len_data4_1['Stage4_thorn']['num'], i))
        for i in range(len_data4_1['Stage4_thorn2']['Len']):
            hurdle.append(Hurdle_four(len_data4_1['Stage4_thorn2']['num'], i))
        for i in range(len_data4_1['hp_jelly']['Len']):
            hurdle.append(Hurdle_four(len_data4_1['hp_jelly']['num'], i))

##############################################################################

    for i in range(len_data4_2['Stage4_Spear']['Len']):
        hurdle.append(Hurdle_four2(len_data4_2['Stage4_Spear']['num'], i))
    for i in range(len_data4_2['Stage4_thorn3']['Len']):
        hurdle.append(Hurdle_four2(len_data4_2['Stage4_thorn3']['num'], i))
    for i in range(len_data4_2['Stage4_thorn4']['Len']):
        hurdle.append(Hurdle_four2(len_data4_2['Stage4_thorn4']['num'], i))
    for i in range(len_data4_2['big_jelly']['Len']):
        hurdle.append(Hurdle_four2(len_data4_2['big_jelly']['num'], i))

################################################################################


    for i in range(len_data4_3['Stage4_Spear2']['Len']):
        hurdle.append(Hurdle_four3(len_data4_3['Stage4_Spear2']['num'], i))
    for i in range(len_data4_3['Stage4_thorn4']['Len']):
        hurdle.append(Hurdle_four3(len_data4_3['Stage4_thorn4']['num'], i))
    for i in range(len_data4_3['big_jelly']['Len']):
        hurdle.append(Hurdle_four3(len_data4_3['big_jelly']['num'], i))


################################################################################

    for i in range(len_data4_4['Stage4_Spear']['Len']):
        hurdle.append(Hurdle_four4(len_data4_4['Stage4_Spear']['num'], i))
    for i in range(len_data4_4['Stage4_thorn2']['Len']):
        hurdle.append(Hurdle_four4(len_data4_4['Stage4_thorn2']['num'], i))
    for i in range(len_data4_4['Stage4_thorn3']['Len']):
        hurdle.append(Hurdle_four4(len_data4_4['Stage4_thorn3']['num'], i))


##################################################################################

    for i in range(len_data4_5['Stage4_Spear2']['Len']):
        hurdle.append(Hurdle_four5(len_data4_5['Stage4_Spear2']['num'], i))
    for i in range(len_data4_5['Stage4_thorn3']['Len']):
        hurdle.append(Hurdle_four5(len_data4_5['Stage4_thorn3']['num'], i))
    for i in range(len_data4_5['Stage4_thorn4']['Len']):
        hurdle.append(Hurdle_four5(len_data4_5['Stage4_thorn4']['num'], i))
    for i in range(len_data4_5['hp_jelly']['Len']):
        hurdle.append(Hurdle_four5(len_data4_5['hp_jelly']['num'], i))



def exit():
    global player, background, ground, pet, hurdle, lobby
   # del(player)
    lobby.score = player.score
    del(background)
    del(ground)
    del(pet)

    for i in hurdle :
        hurdle.remove(i)
        del(i)
    del(hurdle)



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
    global player, background, x, y

    events = get_events()

    if background.frame >= 8:
        #print(background.frame)
        converter.player_hpsize = player.hpsize
        converter.player_score = player.score
        game_framework.change_state(main_state)

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if player.mouse_x > 354 and player.mouse_x < 446 and player.mouse_y > 259 and player.mouse_y < 291:
                result_ok_sound.play()
                game_framework.change_state(lobby)



        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                player.bgm.stop()
                game_framework.change_state(title_state)

            elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
                converter.player_hpsize = player.hpsize
                converter.player_score = player.score
                game_framework.change_state(main_state)

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
    global player, background, ground, hurdle, pet, angle, current_time, result_count
    global gaint_sound, collid_sound, jelly_sound, hp_sound
    frame_time = get_frame_time()
    if player.state == "Dead" and result_count == 0:
        player.dead_time = player.total_frames
        result_count += 1

    if player.hpsize < 500:
        background.update(frame_time, player.state)
        ground.update(frame_time, player.state)
        pet.update(frame_time)
    player.update(frame_time, converter.player_hpsize)

    if player.hpsize < 500:
        for i in hurdle:
            i.update(frame_time, background.Count_copy)
            if collide(player, i) and player.big == False:
                if i.arr['dir'] == 'Image\\big_jelly4.png':
                    gaint_sound.play()
                    if player.state == "Slide":
                        player.state = "Slide_Big"

                    else:
                        player.state = "Big"
                    player.big = True
                    player.big_time = player.total_frames
                #elif player.state == "Big":
                    #print(frame_time)
                elif i.arr['dir'] == 'Image\\item_jelly4.png':
                    jelly_sound.play()
                    player.score += 1
                    hurdle.remove(i)
                elif i.arr['dir'] == 'Image\\hp_jelly4.png':
                    hp_sound.play()
                    player.hp_time = player.total_frames
                    player.hpmove -= 300
                    player.bool_hp = True
                    hurdle.remove(i)
                else:
                    #print(i.arr['dir'])         #    Image\Stage1_Fork.png
                    player.state = "Collid"
                    collid_sound.play()
                    player.hpmove += 30
                    for i in hurdle:
                        i.state = "Collid"
            elif  player.state == "Run" or player.state == "Slide" or player.state == "Jump":
                for i in hurdle:
                    i.state = "None"
            elif collide(player, i) and player.big == True:
                    i.x += 800
                    if i.arr['dir'] == 'Image\\item_jelly2.png':
                        jelly_sound.play()
                        player.score += 1
                        hurdle.remove(i)
                    else:
                        big_collid_sound.play()
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






