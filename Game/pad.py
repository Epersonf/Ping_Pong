from Game.PPlay.sprite import *

class Pad:

    y_vel = 0
    obj = None
    gui = None
    kbrd = None
    ms = None
    ai_controlled = False
    mouse_controlled = False

    def __init__(self, img_loc, jan):
        self.obj = Sprite(img_loc)
        self.gui = jan
        self.kbrd = self.gui.get_keyboard()
        self.ms = self.gui.get_mouse()

    def set_ia_controlled(self, b):
        self.ai_controlled = b

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

    def draw(self, ball):

        if self.ai_controlled:
            if self.obj.y < ball.obj.y - self.obj.height / 2 - 80:
                self.set_y_vel(1)
            elif self.obj.y > ball.obj.y - self.obj.height / 2 + 80:
                self.set_y_vel(-1)
            else:
                self.set_y_vel(0)
        elif not self.mouse_controlled:
            if self.kbrd.key_pressed("DOWN"):
                self.set_y_vel(1)
            elif self.kbrd.key_pressed("UP"):
                self.set_y_vel(-1)
            else:
                self.set_y_vel(0)
        else:
            if self.obj.y < self.ms.get_position()[1] - self.obj.height / 2 - 3:
                self.set_y_vel(1)
            elif self.obj.y > self.get_position()[1] - self.obj.height / 2 + 3:
                self.set_y_vel(-1)
            else:
                self.set_y_vel(0)

        if 0 <= self.obj.y <= (self.gui.height - self.obj.height):
            self.obj.y += self.y_vel
            self.y_vel = 0
        else:
            if self.obj.y < 0:
                self.obj.y = 0
            else:
                self.obj.y = (self.gui.height - self.obj.height)

        self.obj.draw()
