from Game.PPlay.window import *
from Game.PPlay.gameimage import *
from Game.ball import *
from Game.pad import *
from Game.ai_pad import *

gui = Window(1024, 768)
gui.set_title("Ping Pong")

bg = GameImage("Assets/Bg.png")
bg.set_position(0, 0)


score = [0, 0]

padder1 = Pad("Assets/Pad.png", gui)
padder2 = Pad("Assets/Pad.png", gui)
padder1.set_location(gui.width/2 - gui.width/2.3, gui.height/2)
padder2.set_location(gui.width/2 + gui.width/2.3, gui.height/2)

players = [padder1, padder2]

balls = []


def spawn_ball(amount=1):
    amount -= 1
    balls.append(Ball("Assets/Ball.png", gui, players))
    if amount == 0:
        return
    else:
        spawn_ball(amount)


spawn_ball()


padder2.set_ia_controlled(True, AI_Pad(padder2, balls))

kbrd = gui.get_keyboard()
ms = gui.get_mouse()

while True:
    bg.draw()
    counter = 0
    for b in balls:
        counter += b.collided_counter
        b.draw(gui.width, gui.height, score, balls)
    if counter / (len(balls) * 3) > len(balls):
        spawn_ball(1)

    padder1.draw()
    padder2.draw()
    gui.draw_text(str(score[1]), gui.width/2 - 90, 50, 40)
    gui.draw_text(str(score[0]), gui.width/2 + 50, 50, 40)
    gui.update()
