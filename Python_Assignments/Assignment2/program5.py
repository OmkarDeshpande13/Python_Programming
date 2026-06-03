
# Write a program to travel the for() loop in Reverse order

def Function(No):
    
    for i in range(No,0,-1):
        print(i)

def main():

    Value = int(input("Enter the Number:"))

    Function(Value)
    


if __name__ == "__main__":
    main()