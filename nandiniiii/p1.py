
shape = int(input("enter your choice"))


if(shape == 1):
#SPHERE
    r = float(input("enter radius"))
    print('The area is ',4*3.14*r**2)
    print('The volume is ' ,(4/3)*3.14*r**3)

if(shape == 2):
#CUBOID
    l = float(input("enter lenght"))
    b = float(input("enter breadth"))
    h = float(input("enter height"))
    print('the volume is ' ,l*b*h)
    print ('the area is ' , 2*l*b + b*h + h*l)

if(shape == 3):
#CYLINDER
    r = float(input("enter radius"))
    h = float(input("enter height"))
    print('The volume is ' ,3.14*r**2*h)
    print('The area is ' ,2*3.14*r*h)


