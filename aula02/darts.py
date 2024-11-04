# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard


import math
print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))

# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)


if 0 <= math.hypot(x,y) < 6.35 : score = 50
elif 6.35 <= math.hypot(x,y) < 16 : score = 25
elif math.hypot(x,y) > 170 : score = 0
else: 
    if y == 0:
        if x> 0: score = 6
        else: score = 11
    else: 
        angle = math.atan2(y,x) * 360*2 /math.pi
        score = POINTS[angle]


if 99 <= math.hypot(x,y) < 107 : score = 3*score
if 162 <= math.hypot(x,y) < 170: score = 2*score
print(score)
