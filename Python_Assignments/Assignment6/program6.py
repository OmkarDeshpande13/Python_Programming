
def ChkNum(No):

    if(No > 0):
        print("Positive Number")
    elif(No < 0):
        print("Negative Number")
    else:
        print("Number is Zero")

    

def main():

    Value = int(input("Enter the Number:"))

    ChkNum(Value)

if __name__ == "__main__":
    main()