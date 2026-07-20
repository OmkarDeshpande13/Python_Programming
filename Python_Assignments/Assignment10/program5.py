
# Write a program which gives Odd numbers

def DisplayOdd(Value):
    
    for i in range(1,Value+1):

        if(i % 2 != 0):

            print(i)

def main():
    
    Value = int(input("Enter the Number:"))
    DisplayOdd(Value)


if __name__ == "__main__":
    main()