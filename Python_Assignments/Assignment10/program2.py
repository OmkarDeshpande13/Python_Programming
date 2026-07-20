
# Write a program which gives sum of N Natural Numbers

def SumNatural(Value):
    sum = 0
    for i in range(1,Value+1):
        
        sum = sum + i
        
    return sum

def main():
    
    Value = int(input("Enter the Number:"))
    iRet = 0
    iRet = SumNatural(Value)

    print("Sum of Natural Number is :",iRet)


if __name__ == "__main__":
    main()