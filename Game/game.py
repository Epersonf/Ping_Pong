from Game.PPlay.window import *
from Game.PPlay.gameimage import *
from Game.ball import *
from Game.pad import *

gui = Window(1024, 768)
gui.set_title("Ping Pong")

bg = GameImage("Assets/Bg.png")
bg.set_position(0, 0)


score = [0, 0]

padder1 = Pad("Assets/Pad.png", gui)
padder2 = Pad("Assets/Pad.png", gui)

players = [padder1, padder2]

ball = Ball("Assets/Ball.png", gui, players)
ball.set_pos(gui.width/2, gui.height/2)


padder1.set_location(gui.width/2 - gui.width/2.3, gui.height/2)
padder2.set_location(gui.width/2 + gui.width/2.3, gui.height/2)

kbrd = gui.get_keyboard()
ms = gui.get_mouse()

while True:
    bg.draw()
    ball.draw(gui.width, gui.height)

    if kbrd.key_pressed("DOWN"):
        padder1.set_y_vel(1)
    elif kbrd.key_pressed("UP"):
        padder1.set_y_vel(-1)
    else:
        padder1.set_y_vel(0)

    if padder2.obj.y < ms.get_position()[1] - padder2.obj.height/2 - 3:
        padder2.set_y_vel(1)
    elif padder2.obj.y > ms.get_position()[1] - padder2.obj.height/2 + 3:
        padder2.set_y_vel(-1)
    else:
        padder2.set_y_vel(0)

    padder1.draw()
    padder2.draw()
    gui.update()
