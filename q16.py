import math

def ball_collide(ball1, ball2):
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    return math.dist((x1, y1), (x2, y2)) <= (r1 + r2)

print(ball_collide((0, 0, 3), (4, 0, 3)))  # True
