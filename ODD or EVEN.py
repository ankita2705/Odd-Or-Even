number=int(input("Enter the number: "))         #input() gives string so converted explicitly to integer
if(number%2==0):
    
    if(number%4==0):
        
        print("Definately Even")
else:
    num=int(input("Enter a number to divide check: "))

    if(number%num==0):
        print("Check completely divisible by num")
    else:
        print("Check not divisible by num")
        
    
    




