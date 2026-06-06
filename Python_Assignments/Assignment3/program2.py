
# Write a Program to calculate area of a circle

import math

def Area(No):

    Area = math.pi * No * No

    return Area


def main():

    Value = int(input("Enter the Radius:"))
    iret = 0

    iret = Area(Value)

    print("Area of Circle is :",iret)

if __name__ == "__main__":
    main()