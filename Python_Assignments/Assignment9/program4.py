
# Write a Program to get the Cube root of a Number

def Cube(Value):

    Cube = Value ** 3
    return Cube


def main():

    Value = int(input("Enter The Number:"))
    iRet = 0

    iRet = Cube(Value)

    print("Cube is :",iRet)



if __name__ == "__main__":
    main()