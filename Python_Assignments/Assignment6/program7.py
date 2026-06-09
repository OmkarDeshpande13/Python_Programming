
def Divisible(No):

    if(No % 5 == 0):
        print(True)
 
    else:
        print(False)

    

def main():

    Value = int(input("Enter the Number:"))

    Divisible(Value)

if __name__ == "__main__":
    main()