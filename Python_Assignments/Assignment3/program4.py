
# Write a Program which take Number and convert it into a Binary Nnumber

import math

def Binary(No):

    Binary_No = bin(No)

    return Binary_No


def main():

    Value = int(input("Enter the Number:"))
    iret = 0

    iret = Binary(Value)

    print("Binary is :",iret)

if __name__ == "__main__":
    main()