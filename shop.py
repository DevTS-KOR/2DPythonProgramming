import game_framework
import lobby
import main_state
from pico2d import *



name = "TitleState"
image = None
exit = None
time = False
x, y = 0, 0

chestnut_buy = None
chestnut_select = None
chestnut_buy_click = None
chestnut_select_click = None

dog_buy = None
dog_select = None
dog_buy_click = None
dog_select_click = None

wafer_buy = None
wafer_select = None
wafer_buy_click = None
wafer_select_click = None

dog_pet_buy = False
chestnut_pet_buy = False
wafer_pet_buy = False

pet = "None"

def enter():
    global image, exit, chestnut_buy, chestnut_select, chestnut_buy_click, chestnut_select_click
    global dog_buy, dog_select, dog_buy_click, dog_select_click
    global wafer_buy, wafer_select, wafer_buy_click, wafer_select_click
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

def exit():
    global image
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



def handle_events():
    global time, chestnut_pet_buy, x, y, dog_pet_buy, wafer_pet_buy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 800 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 800 - event.y
            if x > 685 and x < 735 and y > 515 and y < 565:
                game_framework.push_state(lobby)

            if x > 104 and x < 196 and y > 204 and y < 236:
                chestnut_pet_buy = True

            if x > 344 and x < 436 and y > 204 and y < 236:
                dog_pet_buy = True

            if x > 584 and x < 676 and y > 204 and y < 236:
                wafer_pet_buy = True

        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            #elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                #time = True
                #game_framework.change_state(lobby)


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

    elif x > 104 and x < 196 and y > 204 and y < 236 and chestnut_pet_buy == True:
        chestnut_select_click.draw(150, 220)
        pet = "chestnut"
    #####################################################################
    #92 32 / 46 16
    if dog_pet_buy == False:
        chestnut_buy.draw(390, 220)

    elif dog_pet_buy == True:
        chestnut_select.draw(390, 220)

    if x > 344 and x < 436 and y > 204 and y < 236 and dog_pet_buy == False:
        dog_buy_click.draw(390, 220)

    elif x > 344 and x < 436 and y > 204 and y < 236 and dog_pet_buy == True:
        dog_select_click.draw(390, 220)
        pet = "dog"
    #####################################################################
    #92 32 / 46 16
    if wafer_pet_buy == False:
        chestnut_buy.draw(630, 220)

    elif wafer_pet_buy == True:
        chestnut_select.draw(630, 220)

    if x > 584 and x < 676 and y > 204 and y < 236 and wafer_pet_buy == False:
        wafer_buy_click.draw(630, 220)

    elif x > 584 and x < 676 and y > 204 and y < 236 and wafer_pet_buy == True:
        wafer_select_click.draw(630, 220)
        pet = "wafer"
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






