#PROGRAM TO LOWER CASE EVERY LETTER OF THE INPUT


operation=input("add: addition, sub:subtraction, mul:multiplication, div:division:")
output=operation.lower()
if(output == 'add'):
    x=float(input("enter the first digit:"))
    y=float(input("enter the second digit:"))
    addition= x+y
    print("sum is:", addition)

if(output == 'sub'):
    x=float(input("enter the first digit:"))
    y=float(input("enter the second digit:"))
    subtraction= x-y
    print("difference is:", subtraction)    

if(output == 'mul'):
    x=float(input("enter the first digit:"))
    y=float(input("enter the second digit:"))
    multiplication= x*y
    print("product is:", multiplication)

if(output == 'div'):
    x=float(input("enter the first digit:"))
    y=float(input("enter the second digit:"))
    division= x/y
    print("division is:", division)    
