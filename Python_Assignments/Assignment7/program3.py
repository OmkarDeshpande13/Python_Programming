def Factorial(No):
    fact = 1
    for i in range(1,No,1):
        fact = fact +(fact) * i
    return fact



def main():

    Value = int(input("Enter the Number : "))

    iret = 0

    iret = Factorial(Value)
    print("Factorial is : ",iret)



if __name__ == "__main__":
    main()