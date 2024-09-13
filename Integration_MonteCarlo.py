import math
import random

def function(x):
    return math.log(x)/x # we want to integrate log(x)/x over the interval 1 to 10

count=0
in_area=0

while count<1000000:
    x_coord=random.uniform(1,10)
    y_coord=random.uniform(0,(1/(math.e)))
    if function(x_coord)>y_coord:
        in_area+=1
    count +=1

print(count)
print(in_area)
area_of_uniform_dist=9/math.e
integral_value=(in_area/count)*(area_of_uniform_dist)
print(integral_value)