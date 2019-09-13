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
padder2.ai_controlled = True

players = [padder1, padder2]

ball = Ball("Assets/Ball.png", gui, players)
ball.set_pos(gui.width/2 - ball.obj.width, gui.height/2 - ball.obj.height)


padder1.set_location(gui.width/2 - gui.width/2.3, gui.height/2)
padder2.set_location(gui.width/2 + gui.width/2.3, gui.height/2)

kbrd = gui.get_keyboard()
ms = gui.get_mouse()

while True:
    bg.draw()
    ball.draw(gui.width, gui.height, score)
    padder1.draw(ball)
    padder2.draw(ball)
    gui.draw_text(str(score[1]), gui.width/2 - 90, 50, 40)
    gui.draw_text(str(score[0]), gui.width/2 + 50, 50, 40)
    gui.update()
