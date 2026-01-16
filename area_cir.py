import sys
import math


if len(sys.argv) > 1:
    radius = float(sys.argv[1])  
else:
    
    radius = float(input("Enter the radius: "))

area = math.pi * radius * radius
print(f"Area of circle with radius {radius} is {area}")
