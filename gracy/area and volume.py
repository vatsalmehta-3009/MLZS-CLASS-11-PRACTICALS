i=10
while(i==10):

    shape = (input('enter shape 1 for circle,  2 for cuboid , 3 for cylinder and 4 for triangle PRESS Q TO QUIT: ')).upper()
    if(shape=='1'):
        radius = float(input('enter radius:'))
        area = 4*3.14*radius**2
        volume = 4/3*3.14*radius**3
        print("the area is ", area,"the volume is", volume)

    elif(shape=='2'):
        l = float(input('enter lenght:'))
        b = float(input('enter breadth:'))
        h = float(input('enter height:'))
        volume2 = l*b*h
        print("the volume is", volume2)
    elif(shape=='3'):
        r = float(input('enter r:'))
        h = float(input('enter height:'))
        surfacearea = 2*3.14*r*h
        vol = 3.14*r**2*h
        print('surface area is', surfacearea, 'volume',vol)
    elif(shape=='4'):
    
        a = float(input('enter a:'))
        b = float(input('enter b:'))
        c = float(input('enter c:'))
        s= (a+b+c)/2
        areatriangle= (s*(s-a)*(s-b)*(s-c))**(1/2)
        print(areatriangle)

    elif(shape=='Q'):
        i = i + 1
        print("THE CODE ENDED")

    else:
        print("enter number correctly")

   









