
# Write a Program to get the Square of a Number

def Square(Value):

    Square = Value ** 2
    return Square


def main():

    Value = int(input("Enter The Number:"))
    iRet = 0

    iRet = Square(Value)

    print("Square is :",iRet)



if __name__ == "__main__":
    main()