#Homework #1
#Input the radius of a circle. The program has to calculate its circumference and area.(use the math.pi constant defined in the math module).

import math
r = int(input("Radius = "))
a = math.pi * r **2
c = 2 * math.pi * r
print("Area = ", a)
print("Circumference = ", c)