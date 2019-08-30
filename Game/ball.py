from Game.PPlay.sprite import *

class Ball:
    x_vel = -1
    y_vel = -1

    obj = None
    gui = None
    def __init__(self, img_path):
        self.obj = Sprite(img_path)

    def set_pos(self, x, y):
        self.obj.set_position(x, y)

    def draw(self, width, height):

        self.obj.x += self.x_vel
        self.obj.y += self.y_vel

        if self.obj.y >= height - self.obj.height or self.obj.y <= 0:
            self.y_vel = -self.y_vel

        if self.obj.x >= width - self.obj.width or self.obj.x <= 0:
            self.x_vel = -self.x_vel
        self.obj.draw()

