import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
dev = None
logo_time = 0.0


def enter():
    global image, dev
    open_canvas()
    image = load_image('Image\\title_kakao.png')
    dev = load_image('Image\\title_CI.png')


def exit():
    global image, dev
    del(image)
    del(dev)
    close_canvas()


def update():
    global logo_time

    if (logo_time > 2.0):
        logo_time = 0
        # game_framework.quit() exit()함수를 호출한다.
        game_framework.push_state(title_state) #현재 상태를 유지하고 넘어간다.
    delay(0.01)
    logo_time += 0.01


def draw():
    global image, dev, logo_time
    clear_canvas()
    image.draw(400,400)
    if(logo_time > 1.0):
        dev.draw(400, 400)
    update_canvas()

def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass

