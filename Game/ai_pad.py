from Game.pad import *
from math import pow, sqrt, copysign

class AI_Pad:

    pad = None
    balls_address = None

    def __init__(self, pad, balls):
        self.pad = pad
        self.balls_address = balls

    def get_closest_ball(self, balls):
        record = -1
        ball = None
        for b in balls:
            dif = b.obj.x - self.pad.obj.x
            dist = abs(dif)
            if (dist < record and copysign(ball.x_vel, dif) == ball.x_vel) or ball is None:
                ball = b
                record = dist
        return ball


    @staticmethod
    def distance(x1, y1, x2, y2):
        return sqrt(pow(x1 + x2, 2) + pow(y1 + y2, 2))


    def move(self):
        ball = self.get_closest_ball(self.balls_address)
        if self.pad.obj.y < ball.obj.y - self.pad.obj.height / 2 - 80:
            self.pad.set_y_vel(1)
        elif self.pad.obj.y > ball.obj.y - self.pad.obj.height / 2 + 80:
            self.pad.set_y_vel(-1)
        else:
            self.pad.set_y_vel(0)