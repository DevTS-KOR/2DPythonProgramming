import random
from pico2d import *
import os
os.chdir("C:\\2DGAME\\project\\jpg")

class Map:
    global stageNum
    def __init__(self):
        self.bkframe = 0
        self.doubleX = 600
        self.groundX = 0
        self.groundY = 0
        self.groundH = 0
        self.SetStageData()
    def SetStageData(self):
        if stageNum == 1:
            self.background = load_image('background2.2.png')
            self.doublebackground = load_image('doublebackground2.2.png')
            self.ground = load_image('block.png')
            self.groundY = 200
            self.groundH = 400
        elif stageNum == 2:
            self.background = load_image('background1.2.png')
            self.doublebackground = load_image('doublebackground2.png')
            self.ground = load_image('grass.png')
            self.groundY = 600
            self.groundH = 1200
        elif stageNum == 3:
            self.background = load_image('background1.2.png')
            self.doublebackground = load_image('doublebackground.png')
            self.ground = load_image('grass.png')
            self.groundY = 600
            self.groundH = 1200
        elif stageNum == 4:
            self.background = load_image('background3.png')
            self.doublebackground = load_image('doublebackground2.png')
            self.ground = load_image('rock.png')
            self.groundY = 500
            self.groundH = 1050

    def update(self):
       self.doubleX = self.doubleX-5
       if self.doubleX == -600:
           self.doubleX = 600

       self.groundX = (self.groundX-20)
       if self.groundX == -600:
            self.groundX = 600

    def draw(self):
        self.doublebackground.draw(self.doubleX, 400, 1200, 800)
        self.doublebackground.draw(self.doubleX+1200, 400, 1200, 800)
        self.background.draw(self.groundX, 400, 1200, 800)
        self.background.draw(self.groundX+1200, 400, 1200, 800)
        self.ground.draw(self.groundX, self.groundY, 1200, self.groundH,)
        self.ground.draw(self.groundX+1200, self.groundY, 1200, self.groundH)

class TrapManager:
    global TrapList
    def __init__(self):
        self.x = 1500
    def SetStageTrap(self):
        for i in range(50):
            TrapList.append(Trap((i*500)+random.randint(-250,250)+1200, random.randint(1,3)))

    def updata(self):
        pass

class Trap:
    global stageNum
    def __init__(self, x, trapType):
        self.trapX = x   #?μ븷臾?x醫뚰몴媛?
        self.trapY = 0   #?μ븷臾?y醫뚰몴媛?
        self.frame = 0
        self.MaxFrame = 6
        self.type = trapType
        self.trap = None
        self.imageX = 0  #?대?吏 媛濡쒓만??
        self.imageY = 0  #?대?吏 ?몃줈湲몄씠
        self.width = 0
        self.height = 0
        self.SetTrapImage()


    def SetTrapImage(self):
        if stageNum == 1:
            if self.type == 1:
                self.trap = load_image('flower.png')
                self.MaxFrame = 6
                self.imageX = 141
                self.imageY = 141
                self.trapY = 195
                self.width = 100
                self.height = 135
            elif self.type == 2:
                self.trap = load_image('flower2.png')
                self.MaxFrame = 6
                self.imageX = 133
                self.imageY = 148
                self.trapY = 195
                self.width = 100
                self.height = 135
            elif self.type == 3:
                self.trap = load_image('Trap3.png')
                self.MaxFrame = 12
                self.imageX = 86
                self.imageY = 319
                self.trapY = 490
                self.width = 150
                self.height = 610
        if stageNum == 2:
            if self.type == 1:
                self.trap = load_image('shell.png')
                self.MaxFrame = 12
                self.imageX = 142
                self.imageY = 58
                self.trapY = 180
                self.width = 130
                self.height = 100
            elif self.type == 2:
                self.trap = load_image('swingNot.png')
                self.MaxFrame = 16
                self.imageX = 173
                self.imageY = 136
                self.trapY = 400
                self.width = 200
                self.height = 400
            elif self.type == 3:
                self.trap = load_image('flower2.png')
                self.MaxFrame = 6
                self.imageX = 133
                self.imageY = 148
                self.trapY = 195
                self.width = 100
                self.height = 135
        if stageNum == 3:
            if self.type == 1:
                self.trap = load_image('redFire.png')
                self.MaxFrame = 6
                self.imageX = 97
                self.imageY = 149
                self.trapY = 180
                self.width= 130
                self.height = 100
            elif self.type == 2:
                self.trap = load_image('greenFire.png')
                self.MaxFrame = 6
                self.imageX = 97
                self.imageY = 149
                self.trapY = 400
                self.width = 200
                self.height = 400
            elif self.type == 3:
                self.trap = load_image('Trap3.png')
                self.MaxFrame = 12
                self.imageX = 86
                self.imageY = 319
                self.trapY = 490
                self.width = 150
                self.height = 610
        if stageNum == 4:
            if self.type == 1:
                self.trap = load_image('Trap1.png')
                self.MaxFrame = 9
                self.imageX = 147
                self.imageY = 199
                self.trapY = 230
                self.width = 180
                self.height = 200
            elif self.type == 2:
                self.trap = load_image('Trap2.png')
                self.MaxFrame = 6
                self.imageX = 221
                self.imageY = 319
                self.trapY = 490
                self.width = 221
                self.height = 620
            elif self.type == 3:
                self.trap = load_image('Trap3.png')
                self.MaxFrame = 12
                self.imageX = 86
                self.imageY = 319
                self.trapY = 490
                self.width = 150
                self.height = 610
    def update(self):
        self.frame = (self.frame+1) % self.MaxFrame
        self.moving()
    def moving(self):
        self.trapX = (self.trapX-20)
    def draw(self):
        self.trap.clip_draw(self.frame * self.imageX, 0, self.imageX, self.imageY, self.trapX, self.trapY, self.width, self.height)

class Character:

    RUN, SLIDING, JUMP = 0, 1, 2

    def __init__(self):
        self.yellowY = 175
        self.frame = 0
        self.character = load_image('YlarvaRun.png')
        self.gravitySpeed = 0
        self.state = self.RUN
        self.MaxFrame = 5

    def gravity(self):
        if (self.yellowY-45-self.gravitySpeed) > 130:
            self.gravitySpeed += 4
            self.yellowY -=self.gravitySpeed
        else:
            self.yellowY = 130+45
            self.gravitySpeed = 0
             ##self.state = self.RUN

    def SetTCharacterImage(self):
        self.frame = 0
        if self.state == self.RUN:
            self.character = load_image('YlarvaRun.png')
            MaxFrame = 5
        elif self.state == self.SLIDING:
            self.character = load_image('YlarvaSlide.png')
            MaxFrame = 6
        elif self.state == self.JUMP:
            self.character = load_image('YlarvaJump.png')
            MaxFrame = 7

    def update(self):
        self.frame = (self.frame + 1) % self.MaxFrame
        self.gravity()

    def draw(self):
        self.character.clip_draw(self.frame * 90, 0, 90, 90, 400, self.yellowY)




def handle_events():
    global running
    global TitleSwitch
    global changeMap
    global yellow
    global stageNum
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                if (yellow.yellowY-45) == 130:
                    yellow.gravitySpeed = -35
                    yellow.state = yellow.JUMP
                yellow.SetTCharacterImage()
            if event.key == SDLK_DOWN:
                yellow.yellowY = 130+45
                yellow.gravitySpeed = 0
                yellow.state = yellow.SLIDING
                yellow.SetTCharacterImage()
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_a: #??댄? ?붾㈃ 醫낅즺
                TitleSwitch = False
            elif event.key == SDLK_b: #?ㅽ뀒?댁? 諛붽씀湲?
                stageNum += 1
                if stageNum == 5:
                    stageNum = 1
                stage.SetStageData()
                TrapList.clear()
                trapManager.SetStageTrap()
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                 yellow.state = yellow.RUN
                 yellow.SetTCharacterImage()
            if event.key == SDLK_UP:
                yellow.state = yellow.RUN
                yellow.SetTCharacterImage()

open_canvas(1200, 800)
Title = load_image('background0.png')
yellow = Character()
stageNum = 1
stage = Map()
TrapList = []
TitleSwitch = True
running = True
frame = 0
trapManager = TrapManager()
trapManager.SetStageTrap()
show_cursor()
while (running):
    handle_events()
    clear_canvas()
    if TitleSwitch == False:
        for trap in TrapList:
            trap.update()
        stage.update()
        yellow.update()

        stage.draw()
        yellow.draw()
        for trap in TrapList:
            trap.draw()
    else:
        Title.draw(600, 400, 1200, 800)
    update_canvas()
    delay(0.06)

close_canvas()
