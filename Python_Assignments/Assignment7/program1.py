import Arithematic

def main():

    Value1 = int(input("Enter the First Number : "))
    Value2 = int(input("Enter the First Number : "))

    iret = 0

    iret = Arithematic.Add(Value1,Value2)
    print("Addition is : ",iret)

    iret = Arithematic.sub(Value1,Value2)
    print("Substraction is : ",iret)

    iret = Arithematic.mul(Value1,Value2)
    print("Multiplication is : ",iret)

    iret = Arithematic.div(Value1,Value2)
    print("Division is : ",iret)


if __name__ == "__main__":
    main()