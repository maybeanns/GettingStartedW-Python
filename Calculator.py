print("Welcome to My Calculator")




while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nEnter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\nEnter 5 for exit")
    
    sub = int(input())
    if(sub == 1):
        print(num1,"+",num2,"=",num1+num2)
    elif(sub == 2):
        print(num1,"-",num2,"=",num1-num2)
    
    elif(sub == 3):
        print(num1,"x",num2,"=",num1*num2)
    
    elif(sub == 4):
        if(num2==0):
            print("Can't do it,Sorry")
        else:    
            print(num1,"%",num2,"=",num1/num2)
    elif(sub == 5):
        break
       
    else:
        print("Please Consider Valid Input!")
        
print("Thanks for using My Calculator")    
