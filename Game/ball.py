from Game.PPlay.sprite import *


class Ball:
    x_vel = -300
    y_vel = -300

    obj = None
    gui = None
    padders = None
    ap = None

    collided_counter = 0

    def __init__(self, img_path, gui, pd):
        self.obj = Sprite(img_path)
        self.gui = gui
        self.padders = pd
        self.ap = self.obj.height/30000
        self.set_pos(gui.width/2 - self.obj.width, gui.height/2 - self.obj.height)

    def set_pos(self, x, y):
        self.obj.set_position(x, y)

    def draw(self, width, height, score, balls):

        self.obj.x += self.x_vel * self.gui.delta_time()
        self.obj.y += self.y_vel * self.gui.delta_time()

        if self.obj.y < 0:
            self.obj.y = 0
            self.y_vel = abs(self.y_vel)
        elif self.obj.y > height - self.obj.height:
            self.obj.y = height - self.obj.height
            self.y_vel = -abs(self.y_vel)

        if self.obj.x > width - self.obj.width or self.obj.x < 0:
            self.collided_counter = 0
            if self.obj.x > width - self.obj.width:
                score[0] += 1
            if self.obj.x < 0:
                score[1] += 1
            if len(balls) > 1:
                balls.remove(self)
            self.obj.set_position(self.gui.width/2 - self.obj.width, self.gui.height/2 - self.obj.height)

        for i in self.padders:
            if self.obj.collided(i.obj):
                self.collided_counter += 1
                if self.obj.x + self.obj.width > i.obj.x + i.obj.width:
                    #direita
                    self.x_vel = abs(self.x_vel)
                    self.obj.x = i.obj.x + i.obj.width
                elif self.obj.x < i.obj.x:
                    #esquerda
                    self.x_vel = -abs(self.x_vel)
                    self.obj.x = i.obj.x - self.obj.width
                elif self.obj.y < i.obj.y - self.ap:
                    #cima
                    self.y_vel = -abs(self.y_vel)
                    self.obj.y = i.obj.y - self.obj.height
                elif self.obj.y + self.obj.height > i.obj.y + i.obj.height + self.ap:
                    #baixo
                    self.y_vel = abs(self.y_vel)
                    self.obj.y = i.obj.y + i.obj.height + self.obj.height
        self.obj.draw()
