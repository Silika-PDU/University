#Input two integers. Write a program that calculate the arithmetic and geometric mean of the numbers.
import math
A = int(input("A = "))
B = int(input("B = "))
print("Arithemetric mean = ", (A + B)/2)
print("Geometric mean = ", math.sqrt(A * B))