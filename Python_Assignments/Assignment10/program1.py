
# Write a program which gives Table of Number get the Number from User

def DisplayTable(Value):
    mul = 1
    for i in range(1,11):

        mul = Value * i
        print(mul)

def main():
    
    Value = int(input("Enter the Number:"))

    DisplayTable(Value)



if __name__ == "__main__":
    main()