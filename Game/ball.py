from Game.PPlay.sprite import *

class Ball:
    x_vel = -300
    y_vel = -300

    obj = None
    gui = None
    padders = None


    def __init__(self, img_path, g, pd):
        self.obj = Sprite(img_path)
        self.gui = g
        self.padders = pd

    def set_pos(self, x, y):
        self.obj.set_position(x, y)

    def draw(self, width, height):

        self.obj.x += self.x_vel * self.gui.delta_time()
        self.obj.y += self.y_vel * self.gui.delta_time()

        if self.obj.y >= height - self.obj.height or self.obj.y <= 0:
            self.y_vel = -self.y_vel

        if self.obj.x >= width - self.obj.width or self.obj.x <= 0:
            self.obj.set_position(self.gui.width/2, self.gui.height/2)

        for i in self.padders:
            if not (i.obj.y < self.obj.y < i.obj.y + i.obj.height):
                if self.obj.collided(i.obj):
                    self.x_vel = -self.x_vel

        self.obj.draw()

