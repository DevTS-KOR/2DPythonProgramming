import game_framework
import lobby
import converter
from pico2d import *



name = "Shop"
image = None
exit = None
time = False
x, y = 0, 0

chestnut_buy = None
chestnut_select = None
chestnut_buy_click = None
chestnut_select_click = None
chestnut_money = 0

dog_buy = None
dog_select = None
dog_buy_click = None
dog_select_click = None
dog_money = 100

wafer_buy = None
wafer_select = None
wafer_buy_click = None
wafer_select_click = None
wafer_money = 100

chestnut_check = None
dog_check = None
wafer_check = None

dog_pet_buy = False
chestnut_pet_buy = False
wafer_pet_buy = False

chestnut_select_check = False
dog_select_check = False
wafer_select_check = False

pet = "None"
button = None
buy_score = 0

def enter():
    global image, exit, chestnut_buy, chestnut_select, chestnut_buy_click, chestnut_select_click, dog_pet_buy, dog_check, wafer_check, chestnut_check
    global dog_buy, dog_select, dog_buy_click, dog_select_click
    global wafer_buy, wafer_select, wafer_buy_click, wafer_select_click, button, buy_score
    image = load_image('Image\\Shop\\shop_main.png')
    exit = load_image('Image\\Shop\\exit_button.png')
    chestnut_buy = load_image('Image\\Shop\\buy_button.png')
    chestnut_buy_click = load_image('Image\\Shop\\buy_button_click.png')
    chestnut_select = load_image('Image\\Shop\\select_button.png')
    chestnut_select_click = load_image('Image\\Shop\\select_button_click.png')

    dog_buy = load_image('Image\\Shop\\buy_button.png')
    dog_buy_click = load_image('Image\\Shop\\buy_button_click.png')
    dog_select = load_image('Image\\Shop\\select_button.png')
    dog_select_click = load_image('Image\\Shop\\select_button_click.png')

    wafer_buy = load_image('Image\\Shop\\buy_button.png')
    wafer_buy_click = load_image('Image\\Shop\\buy_button_click.png')
    wafer_select = load_image('Image\\Shop\\select_button.png')
    wafer_select_click = load_image('Image\\Shop\\select_button_click.png')

    chestnut_check = load_image('Image\\Shop\\check_button_click.png')
    dog_check = load_image('Image\\Shop\\check_button_click.png')
    wafer_check = load_image('Image\\Shop\\check_button_click.png')

    #로비 bgm 이어서
    lobby.bgm_re = False

    if button == None:
        button = load_wav('Sound\\ui_1.wav')
        button.set_volume(128)

    if buy_score != 0:
        buy_score = 0

def exit():
    global image, exit, chestnut_buy, chestnut_select, chestnut_buy_click, chestnut_select_click
    global dog_buy, dog_select, dog_buy_click, dog_select_click, wafer_buy, wafer_select, wafer_buy_click, wafer_select_click
    global chestnut_check, dog_check, wafer_check
    del(image)
    del(exit)
    del(chestnut_buy)
    del(chestnut_select)
    del(chestnut_buy_click)
    del(chestnut_select_click)
    del(dog_buy)
    del(dog_select)
    del(dog_buy_click)
    del(dog_select_click)
    del(wafer_buy)
    del(wafer_select)
    del(wafer_buy_click)
    del(wafer_select_click)
    del(chestnut_check)
    del(dog_check)
    del(wafer_check)


def handle_events():
    global time, chestnut_pet_buy, x, y, dog_pet_buy, wafer_pet_buy
    global chestnut_select_check, dog_select_check, wafer_select_check, button, buy_score
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 800 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 800 - event.y
            if x > 104 and x < 196 and y > 204 and y < 236 and chestnut_pet_buy == True:
                button.play()
                chestnut_select_check = True
                dog_select_check = False
                wafer_select_check = False

            elif x > 344 and x < 436 and y > 204 and y < 236 and dog_pet_buy == True:
                button.play()
                chestnut_select_check = False
                dog_select_check = True
                wafer_select_check = False

            elif x > 584 and x < 676 and y > 204 and y < 236 and wafer_pet_buy == True:
                button.play()
                chestnut_select_check = False
                dog_select_check = False
                wafer_select_check = True

            elif x > 104 and x < 196 and y > 204 and y < 236:
                button.play()
                chestnut_pet_buy = True

            elif x > 344 and x < 436 and y > 204 and y < 236  and lobby.sum_score >= dog_money:
                button.play()
                lobby.sum_score -= dog_money
                buy_score += dog_money
                dog_pet_buy = True

            elif x > 584 and x < 676 and y > 204 and y < 236  and lobby.sum_score >= dog_money:
                button.play()
                lobby.sum_score -= wafer_money
                buy_score += wafer_money
                wafer_pet_buy = True

            elif x > 685 and x < 735 and y > 515 and y < 565:
                button.play()
                game_framework.push_state(lobby)


        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()


def draw():
    global x, y, pet
    clear_canvas()
    image.draw(400, 400)
    exit.draw(700, 540)
    if chestnut_pet_buy == False:
        chestnut_buy.draw(150, 220)

    elif chestnut_pet_buy == True:
        chestnut_select.draw(150, 220)

    if x > 104 and x < 196 and y > 204 and y < 236 and chestnut_pet_buy == False:
        chestnut_buy_click.draw(150, 220)

    if x > 104 and x < 196 and y > 204 and y < 236 and chestnut_pet_buy == True and chestnut_select_check == False:
        chestnut_select_click.draw(150, 220)

    elif chestnut_pet_buy == True and chestnut_select_check == True:
        chestnut_check.draw(150, 220)
        pet = "chestnut"
    #####################################################################
    #92 32 / 46 16
    if dog_pet_buy == False:
        chestnut_buy.draw(390, 220)

    elif dog_pet_buy == True:
        chestnut_select.draw(390, 220)

    if x > 344 and x < 436 and y > 204 and y < 236 and dog_pet_buy == False:
        dog_buy_click.draw(390, 220)

    if x > 344 and x < 436 and y > 204 and y < 236 and dog_pet_buy == True and dog_select_check == False:
        dog_select_click.draw(390, 220)

    elif dog_pet_buy == True and dog_select_check == True:
        dog_check.draw(390, 220)
        pet = "dog"
    #####################################################################
    #92 32 / 46 16
    if wafer_pet_buy == False:
        chestnut_buy.draw(630, 220)

    elif wafer_pet_buy == True:
        chestnut_select.draw(630, 220)

    if x > 584 and x < 676 and y > 204 and y < 236 and wafer_pet_buy == False:
        wafer_buy_click.draw(630, 220)

    if x > 584 and x < 676 and y > 204 and y < 236 and wafer_pet_buy == True and wafer_select_check == False:
        wafer_select_click.draw(630, 220)

    elif wafer_pet_buy == True and wafer_select_check == True:
        wafer_check.draw(630, 220)
        pet = "wafer"


    if lobby.sum_score % 10 == 0:
        lobby.zero.draw(385, 600)
    elif lobby.sum_score % 10 == 1:
        lobby.one.draw(385, 600)
    elif lobby.sum_score % 10 == 2:
        lobby.two.draw(385, 600)
    elif lobby.sum_score % 10 == 3:
        lobby.three.draw(385, 600)
    elif lobby.sum_score % 10 == 4:
        lobby.four.draw(385, 600)
    elif lobby.sum_score % 10 == 5:
        lobby.five.draw(385, 600)
    elif lobby.sum_score % 10 == 6:
        lobby.six.draw(385, 600)
    elif lobby.sum_score % 10 == 7:
        lobby.seven.draw(385, 600)
    elif lobby.sum_score % 10 == 8:
        lobby.eight.draw(385, 600)
    elif lobby.sum_score % 10 == 9:
        lobby.nine.draw(385, 600)

    if int(lobby.sum_score / 10) % 10 == 0:
        lobby.zero.draw(355, 600)
    elif int(lobby.sum_score / 10) % 10 == 1:
        lobby.one.draw(355, 600)
    elif int(lobby.sum_score / 10) % 10 == 2:
         lobby.two.draw(355, 600)
    elif int(lobby.sum_score / 10) % 10 == 3:
        lobby.three.draw(355, 600)
    elif int(lobby.sum_score / 10) % 10 == 4:
        lobby.four.draw(355, 600)
    elif int(lobby.sum_score / 10) % 10 == 5:
        lobby.five.draw(355, 600)
    elif int(lobby.sum_score / 10) % 10 == 6:
        lobby.six.draw(355, 600)
    elif int(lobby.sum_score / 10) % 10 == 7:
        lobby.seven.draw(355, 600)
    elif int(lobby.sum_score / 10) % 10 == 8:
        lobby.eight.draw(355, 600)
    elif int(lobby.sum_score / 10) % 10 == 9:
        lobby.nine.draw(355, 600)

    if int(lobby.sum_score / 100) == 0:
        lobby.zero.draw(325, 600)
    elif int(lobby.sum_score / 100) == 1:
        lobby.one.draw(325, 600)
    elif int(lobby.sum_score / 100) == 2:
        lobby.two.draw(325, 600)
    elif int(lobby.sum_score / 100) == 3:
        lobby.three.draw(325, 600)
    elif int(lobby.sum_score / 100) == 4:
        lobby.four.draw(325, 600)
    elif int(lobby.sum_score / 100) == 5:
        lobby.five.draw(325, 600)
    elif int(lobby.sum_score / 100) == 6:
        lobby.six.draw(325, 600)
    elif int(lobby.sum_score / 100) == 7:
        lobby.seven.draw(325, 600)
    elif int(lobby.sum_score / 100) == 8:
        lobby.eight.draw(325, 600)
    elif int(lobby.sum_score / 100) == 9:
        lobby.nine.draw(325, 600)

    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






