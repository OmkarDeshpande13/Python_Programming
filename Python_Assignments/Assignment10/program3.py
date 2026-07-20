
# Write a program which gives a Factorial of a Number

def Factorial(Value):
    sum = 0
    fact = 1    
    for i in range(1,Value+1):
        
        fact = fact * i
        
    return fact

def main():
    
    Value = int(input("Enter the Number:"))
    iRet = 0
    iRet = Factorial(Value)

    print("Sum of Natural Number is :",iRet)


if __name__ == "__main__":
    main()