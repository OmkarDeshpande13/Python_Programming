def SumFactors(No):
    sum = 0
    for i in range(1,No,1):

        if(No % i == 0):
            print(i)
            sum = sum +i

    return sum




def main():

    Value = int(input("Enter the Number : "))

    iret = 0

    iret = SumFactors(Value)
    print("Summation of Factors is : ",iret)



if __name__ == "__main__":
    main()