from Game.PPlay.sprite import *

class Pad:

    y_vel = 0
    obj = None
    gui = None
    ia_controlled = False

    def __init__(self, img_loc, jan):
        self.obj = Sprite(img_loc)
        self.gui = jan

    def set_ia_controlled(self, b):
        self.ia_controlled = b

    def set_y_vel(self, value):
        if value == 0:
            self.y_vel = 0
            return
        v = 800 * self.gui.delta_time()
        if value < 0:
            v = -v
        self.y_vel = v

    def set_location(self, new_x, new_y):
        self.obj.x = new_x
        self.obj.y = new_y

    def draw(self):
        if self.obj.y >= 0 and self.obj.y <= (self.gui.height - self.obj.height):
            self.obj.y += self.y_vel
            self.y_vel = 0
        else:
            if self.obj.y < 0:
                self.obj.y = 0
            else:
                self.obj.y = (self.gui.height - self.obj.height)

        self.obj.draw()
