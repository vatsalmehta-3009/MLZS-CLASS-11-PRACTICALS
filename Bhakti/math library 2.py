import math

i= 0
while i<10:
    angle = float(input("enter angle: "))
    rad = math.radians(angle)
    print (math.sin(rad)**2 + math.cos(rad)**2)
    i = i + 1

    y = input("are you satisfied? : ")
    if y == 'yes':
        break 
    
    
    
    
