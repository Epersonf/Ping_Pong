from Game.PPlay.sprite import *

class Ball:
    x_vel = -300
    y_vel = -300

    obj = None
    gui = None
    padders = None
    ap = None

    def __init__(self, img_path, g, pd):
        self.obj = Sprite(img_path)
        self.gui = g
        self.padders = pd
        self.ap = self.obj.height/30000

    def set_pos(self, x, y):
        self.obj.set_position(x, y)

    def draw(self, width, height, score):

        self.obj.x += self.x_vel * self.gui.delta_time()
        self.obj.y += self.y_vel * self.gui.delta_time()

        if self.obj.y < 0:
            self.obj.y = 0
            self.y_vel = abs(self.y_vel)
        elif self.obj.y > height - self.obj.height:
            self.obj.y = height - self.obj.height
            self.y_vel = -abs(self.y_vel)

        if self.obj.x > width - self.obj.width or self.obj.x < 0:
            if self.obj.x > width - self.obj.width:
                score[0] += 1
            if self.obj.x < 0:
                score[1] += 1
            self.obj.set_position(self.gui.width/2 - self.obj.width, self.gui.height/2 - self.obj.height)

        for i in self.padders:
            if self.obj.collided(i.obj):
                if self.obj.x + self.obj.width > i.obj.x + i.obj.width:
                    #direita
                    self.x_vel = abs(self.y_vel)
                    self.obj.x = i.obj.x + i.obj.width
                elif self.obj.x < i.obj.x:
                    #esquerda
                    self.x_vel = -abs(self.y_vel)
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
