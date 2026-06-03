
# write a program to demonstrate the for() loop

def Function(No):
    
    for i in range(1,No+1):
        print(i)

def main():

    Value = int(input("Enter the Number:"))

    Function(Value)
    


if __name__ == "__main__":
    main()