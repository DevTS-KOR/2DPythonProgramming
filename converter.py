import game_framework
import lobby
import Player
import main_state
from pico2d import *

init = None
player_hpsize = 0
player_score = 0
player_hpframe = 0

def enter():
    global player_hpsize, player_score, player_hpframe
    if init == None:
        player_hpsize = 0
        player_score = 0
        player_hpframe = 0

def exit():
    pass


def handle_events():
    pass


def draw():
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






