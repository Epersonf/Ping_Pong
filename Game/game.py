from Game.PPlay.window import *
from Game.PPlay.gameimage import *
from Game.ball import *

gui = Window(1024, 768)
gui.set_title("Ping Pong")

bg = GameImage("Assets/Bg.png")
bg.set_position(0, 0)

ball = Ball("Assets/Ball.png")
ball.set_pos(gui.width/2, gui.height/2)

while True:
    bg.draw()
    ball.draw(gui.width, gui.height)
    gui.update()
