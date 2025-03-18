import math

x1, y1 = map(int, input("Enter coordinates of first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter coordinates of second point (x2 y2): ").split())

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance between points:", distance)
