print('''Welcome!
This is a Calculator...
      ''')


def choice():
    print('''
1. Addition
2. Subtraction
3. Multiplication
4. Division
0. Exit
      ''')

    ch=int(input("Enter your choice:"))
    if ch==1:
        print(num1,"+",num2,"=", num1+num2,"\n")
        print("-"*30,"\n")
        if input("Wanna Continue? (y/n): ").lower()=="y":
            calc()
        else:
            print("-"*10,"Application Closed!","-"*10)
            exit
            
    elif ch==2:
        print(num1,"-",num2,"=", num1-num2)
        print("-"*30,"\n")
        if input("Wanna Continue? (y/n): ").lower()=="y":
            calc()
        else:
            print("-"*10,"Application Closed!","-"*10)
            exit
            
    elif ch==3:
        print(num1,"*",num2,"=", num1*num2)
        print("-"*30,"\n")
        if input("Wanna Continue? (y/n): ").lower()=="y":
            calc()
        else:
            print("-"*10,"Application Closed!","-"*10)
            exit
            
    elif ch==4:
        try:
            print(num1,"/",num2,"=", num1/num2)
            print("-"*30,"\n")
        except ZeroDivisionError:
            print("Can not divide by 0")
            print("-"*30,"\n")
        if input("Wanna Continue? (y/n): ").lower()=="y":
            calc()
        else:
            print("-"*10,"Application Closed!","-"*10)
            exit
            
    elif ch==0:
        print("-"*10,"Application Closed!","-"*10)
        exit
    else:
        print("Please make a valid Choice!")
        print("-"*30)
        choice()

def calc():
    global num1
    num1= eval(input("Enter first number: "))

    if (isinstance(num1,int)==False) and (isinstance(num1,float)==False):
        print("Please enter a numeric value!")
        calc()
    
    else:
        global num2
        num2= eval(input("Enter second number: "))
    
        if (isinstance(num2,int)==False) and (isinstance(num2,float)==False):
            print("Please enter a numeric value!")
            calc()
            
        else:
            choice()
            
calc()
