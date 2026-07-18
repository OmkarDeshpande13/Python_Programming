'''
2. Write a program which accept N numbers from user and store it into List. Return Maximum
   number from that List.

Input : Number of elements : 7

Input Elements : 13     5    45   7    4     56      34

Output : 56 
'''


def Maximum(Arr):

    Max = 0

    for i in range(len(Arr)):

        Max = max(Arr)
    return Max

def main():

    iNo = 0
    iRet = 0
    Arr = []

    print("Enter the Number of Element in List : ")
    iNo = int(input())

    for i in range(0,iNo):

        Num = int(input())
        Arr.append(Num)

    iRet = Maximum(Arr)    
    print("Maximum Element in the List is : ",iRet)

if __name__ == "__main__":
    main()