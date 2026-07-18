'''
4.Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13  5  45  7
4
56
5
34
2
5
65
Element to search : 5
Output : 3
'''

def Frequency(Arr,iFreq):

    freq = 0

    for i in range(len(Arr)):

        if(Arr[i] == iFreq):
            freq = freq + 1
    return(freq)
    

def main():

    Arr = []
    iNo = 0
    iRet = 0
    iFreq = 0

    iNo = int(input("Emter the Number of Element in the List : "))
   
    iFreq = int(input("Enter the Number to find : "))


    for i in range(0,iNo):

        num = int(input())
        Arr.append(num)

    print(Arr)

    iRet = Frequency(Arr,iFreq)
    print("Frequency of the Element is : ",iRet)

if __name__ == "__main__":
    main()