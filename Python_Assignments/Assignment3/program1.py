
# Write a Program to calculate area of a Rectangle

def RectArea(No1,No2):

    Area = No1 * No2

    return Area


def main():

    Value1 = int(input("Enter the Length:"))
    Value2 = int(input("Enter the Width: "))
    iret = 0

    iret = RectArea(Value1,Value2)

    print("Area of Rectangle is :",iret)

if __name__ == "__main__":
    main()