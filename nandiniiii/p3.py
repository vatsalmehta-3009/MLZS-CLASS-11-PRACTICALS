#programming a calculator

s = int(input('Enter number 01 : '))
i = int(input('Enter number 02 : '))


a = (input('add to add, sub to subtract, multi to multiply, div to divide'))

if(a == 'add'):  
   print(s+i)
   
if(a == 'sub'):
   print(s-i)

if(a == 'div'):
   print(s/i)

if(a == 'multi' ):
   print(s*i) 
