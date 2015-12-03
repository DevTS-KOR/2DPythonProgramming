import game_framework
import main_state
import shop
import converter
from pico2d import *



#name = "TitleState"
background = None
game_start = None
gmae_start_click = None
pet = None
pet_click = None
time = False
chestnut = False
dog = False
wafer = False
bgm = None
bgm_re = True
go_shop = None
go_shop_click = False
x, y = 0, 0
score = 0
sum_score = 0
all_score = 0


one = None
two = None
three = None
four = None
five = None
six = None
seven = None
eight = None
nine = None
zero = None


def enter():
    #print(1)
    global background, game_start, gmae_start_click, pet, pet_click, chestnut, dog, wafer, bgm, go_shop
    global one, two, three, four , five, six, seven, eight, nine, zero, score, sum_score, all_score

    converter.lobby_money += converter.player_money
    converter.player_money = 0

    background = load_image('Image\\Lobby\\lobby_background2.png')
    game_start = load_image('Image\\Lobby\\game_start_button.png')
    gmae_start_click = load_image('Image\\Lobby\\game_start_button_click.png')
    pet = load_image('Image\\Lobby\\pet_button.png')
    pet_click = load_image('Image\\Lobby\\pet_button_click.png')
    chestnut = load_image('Image\\Lobby\\chestnut_pet.png')
    dog = load_image('Image\\Lobby\\dog_pet.png')
    wafer = load_image('Image\\Lobby\\wafer_pet.png')

    #score 이미지 저장
    one = load_image('Image\\Number\\1.png')
    two = load_image('Image\\Number\\2.png')
    three = load_image('Image\\Number\\3.png')
    four = load_image('Image\\Number\\4.png')
    five = load_image('Image\\Number\\5.png')
    six = load_image('Image\\Number\\6.png')
    seven = load_image('Image\\Number\\7.png')
    eight = load_image('Image\\Number\\8.png')
    nine = load_image('Image\\Number\\9.png')
    zero = load_image('Image\\Number\\0.png')


    #배경 bgm
    if bgm_re == True:
        bgm = load_music('Sound\\Start.mp3')
        bgm.set_volume(4)
        bgm.repeat_play()

    if go_shop == None:
        go_shop = load_wav('Sound\\ui_1.wav')
        go_shop.set_volume(128)

def exit():
    global background, game_start, gmae_start_click, pet, pet_click
    del(background)
    del(game_start)
    del(gmae_start_click)
    del(pet)
    del(pet_click)


def handle_events():
    global time, go_shop, go_shop_click, bgm, sum_score
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 800 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 800 - event.y
            if x > 485 and x < 735 and y > 195 and y < 255:
                go_shop.play()
                bgm.stop()
                game_framework.change_state(main_state)

            if x > 470 and x < 540 and y > 264 and y < 320:
                go_shop.play()
                game_framework.push_state(shop)

        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

            elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
                sum_score += 100
            #elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                #time = True
                #game_framework.change_state(main_state)




def draw():
    global x, y, bgm_re
    global one, two, three, four , five, six, seven, eight, nine, zero, score, sum_score
    clear_canvas()
    background.draw(400, 400)

    if x > 470 and x < 540 and y > 264 and y < 320:
        pet_click.draw(505, 292)
    else:
        pet.draw(505, 292)

    if x > 485 and x < 735 and y > 195 and y < 255:
        gmae_start_click.draw(610, 225)
    else:
        game_start.draw(610, 225)

    if shop.pet == "chestnut":
        bgm_re = True
        chestnut.draw(550, 410)
    elif shop.pet == "dog":
        bgm_re = True
        dog.draw(550, 410)
    elif shop.pet == "wafer":
        bgm_re = True
        wafer.draw(550, 410)

    if converter.lobby_money % 10 == 0:
        zero.draw(385, 600)
    elif converter.lobby_money % 10 == 1:
        one.draw(385, 600)
    elif converter.lobby_money % 10 == 2:
        two.draw(385, 600)
    elif converter.lobby_money % 10 == 3:
        three.draw(385, 600)
    elif converter.lobby_money % 10 == 4:
        four.draw(385, 600)
    elif converter.lobby_money % 10 == 5:
        five.draw(385, 600)
    elif converter.lobby_money % 10 == 6:
        six.draw(385, 600)
    elif converter.lobby_money % 10 == 7:
        seven.draw(385, 600)
    elif converter.lobby_money % 10 == 8:
        eight.draw(385, 600)
    elif converter.lobby_money % 10 == 9:
        nine.draw(385, 600)

    if int(converter.lobby_money / 10) % 10 == 0:
        zero.draw(355, 600)
    elif int(converter.lobby_money / 10) % 10 == 1:
        one.draw(355, 600)
    elif int(converter.lobby_money / 10) % 10 == 2:
         two.draw(355, 600)
    elif int(converter.lobby_money / 10) % 10 == 3:
        three.draw(355, 600)
    elif int(converter.lobby_money / 10) % 10 == 4:
        four.draw(355, 600)
    elif int(converter.lobby_money / 10) % 10 == 5:
        five.draw(355, 600)
    elif int(converter.lobby_money / 10) % 10 == 6:
        six.draw(355, 600)
    elif int(converter.lobby_money / 10) % 10 == 7:
        seven.draw(355, 600)
    elif int(converter.lobby_money / 10) % 10 == 8:
        eight.draw(355, 600)
    elif int(converter.lobby_money / 10) % 10 == 9:
        nine.draw(355, 600)

    if int(converter.lobby_money / 100) == 0:
        zero.draw(325, 600)
    elif int(converter.lobby_money / 100) == 1:
        one.draw(325, 600)
    elif int(converter.lobby_money / 100) == 2:
        two.draw(325, 600)
    elif int(converter.lobby_money / 100) == 3:
        three.draw(325, 600)
    elif int(converter.lobby_money / 100) == 4:
        four.draw(325, 600)
    elif int(converter.lobby_money / 100) == 5:
        five.draw(325, 600)
    elif int(converter.lobby_money / 100) == 6:
        six.draw(325, 600)
    elif int(converter.lobby_money / 100) == 7:
        seven.draw(325, 600)
    elif int(converter.lobby_money / 100) == 8:
        eight.draw(325, 600)
    elif int(converter.lobby_money / 100) == 9:
        nine.draw(325, 600)

    update_canvas()

def effect_sound():
    pass

def update():
    pass


def pause():
    pass


def resume():
    pass






