#CALCULATOR
i=10
while(i==10):

    print("ENTER ADD FOR ADDITION, SUB FOR SUBSTRACTION, MUL FOR MULTIPLICATION AND DIV FOR DIVISION")
    operation = input("enter the operation you want to do: ").upper()

    x = float(input("enter number: "))
    y = float(input("enter number: "))


                                   
    if(operation=="ADD"):
        print("the addition is: ", x+y)

    elif(operation=="SUB"):
        print("the substraction is: ", x-y)

    elif(operation=="MUL"):
        print("the multiplication is: ", x*y)

    elif(operation=="DIV"):
        print("the division is: ", x/y)

    else:
        print("Try Again!")
        

   
    
