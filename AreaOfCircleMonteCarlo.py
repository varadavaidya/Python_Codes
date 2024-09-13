import math
import random


def area(x, y):
    return math.sqrt(x * x + y * y)


count = 0
in_circle = 0

while count < 1e6:
    x_coord = random.uniform(0, 5)
    y_coord = random.uniform(0, 5)
    if area(x_coord, y_coord) < 5:
        in_circle += 1
    count += 1

print(count)
print(in_circle)

Area_of_circle = 100 * (in_circle / count)

print(Area_of_circle)
