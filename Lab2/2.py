import math

r = float(input("enter radius: "))
if r <= 0:
    print("radius can be positive only")
elif r > 0:
    area = math.pi * r**2
    print("the area is", area)
