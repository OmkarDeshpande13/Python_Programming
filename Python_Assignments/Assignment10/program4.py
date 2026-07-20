
# Write a program which gives Even Numbers 

def DispayEven(Value):
    
    for i in range(1,Value+1):

        if(i % 2 == 0):

            print(i)

def main():
    
    Value = int(input("Enter the Number:"))
    DispayEven(Value)


if __name__ == "__main__":
    main()