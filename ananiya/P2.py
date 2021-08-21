i=5
while(i==5):

#program to find the area and volume of any one of the below shapes
    shape=int(input("1: Sphere, 2: Cuboid:, 3: cylinder:"))

#program to find the area and volume of spheare
    if(shape == 1):
        radius = float(input("enter the radius:"))
        area= 4*3.14*radius**2
        print("area is:", area)
        volume=4/3*3.14**radius*radius
        print("volume is:", volume)
    
#program to find area and volume of cuboid
    if(shape == 2):
        length=float(input("enter the length:"))
        breath=float(input("enter the breath:"))
        height=float(input("enter the height:"))
        area=2*(length*breath+breath*height+height*length)
        print("area is:", area)
        volume = length*breath*height
        print("volume is:", volume)
    
#program to find area and volume of cylinder
    if(shape == 3):
        radius=float(input("enter the radius:"))
        height=float(input("enter the height:"))
        area= 2*3.14*radius*height
        print("area is:", area)
        volume = 3.14*radius*radius*height
        print("volume is:", volume)

    else:
        print("please enter the value correctly")



