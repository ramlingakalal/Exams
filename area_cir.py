import math
def Are_cirf(radius):
    Area=math.pi*radius*radius
    circle=2*math.pi*radius
    return Area,circle

if __name__=="__main__":
    radius=int(input("Enter the radius"))
    print(Are_cirf(radius))
