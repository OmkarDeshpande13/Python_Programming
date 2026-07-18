'''
3.Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List.
Input : Number of elements : 4

Input Elements : 13   5   45    7

Output : 5

'''


def Minimun(Arr):

    Min = 0

    for i in range(len(Arr)):

        Min = min(Arr)
    return Min

def main():

    iNo = 0
    iRet = 0
    Arr = []

    print("Enter the Number of Element in List : ")
    iNo = int(input())

    for i in range(0,iNo):

        Num = int(input())
        Arr.append(Num)

    iRet = Minimun(Arr)    
    print("Minimun Element in the List is : ",iRet  )

if __name__ == "__main__":
    main()