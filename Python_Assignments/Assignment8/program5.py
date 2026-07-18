'''
5.Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().


'''

import ModuleNum

Prime_numbers = []


def ListPrimeNumbers(numbers):

    sum_prime = 0

    for num in numbers:

        if (ModuleNum.ChkPrime(num)):
            
            Prime_numbers.append(num)

            sum_prime = sum_prime + num
        
    print("Prime numbers in the List are : ",Prime_numbers)
    return sum_prime


def main():

    Arr = []
    iNo = 0
    iRet = 0

    iNo = int(input("Emter the Number of Element in the List : "))

    for i in range(0,iNo):

        num = int(input())
        Arr.append(num)

    print("Input List is : ",Arr)

    iRet = ListPrimeNumbers(Arr)
    print("Sum of Prime Numbers are : ",iRet)
   

if __name__ == "__main__":
    main()