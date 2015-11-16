import game_framework
import main_state
import shop
from pico2d import *



name = "TitleState"
background = None
game_start = None
gmae_start_click = None
pet = None
pet_click = None
time = False
chestnut = False
dog = False
wafer = False
x, y = 0, 0

def enter():
    global background, game_start, gmae_start_click, pet, pet_click, chestnut, dog, wafer
    background = load_image('Image\\Lobby\\lobby_background2.png')
    game_start = load_image('Image\\Lobby\\game_start_button.png')
    gmae_start_click = load_image('Image\\Lobby\\game_start_button_click.png')
    pet = load_image('Image\\Lobby\\pet_button.png')
    pet_click = load_image('Image\\Lobby\\pet_button_click.png')
    chestnut = load_image('Image\\Lobby\\chestnut_pet.png')
    dog = load_image('Image\\Lobby\\dog_pet.png')
    wafer = load_image('Image\\Lobby\\wafer_pet.png')

def exit():
    global background, game_start, gmae_start_click, pet, pet_click
    del(background)
    del(game_start)
    del(gmae_start_click)
    del(pet)
    del(pet_click)


def handle_events():
    global time
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
                game_framework.change_state(main_state)

            if x > 470 and x < 540 and y > 264 and y < 320:
                game_framework.push_state(shop)
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            #elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                #time = True
                #game_framework.change_state(main_state)


def draw():
    global x, y
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
        chestnut.draw(550, 410)
    elif shop.pet == "dog":
        dog.draw(550, 410)
    elif shop.pet == "wafer":
        wafer.draw(550, 410)

    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






