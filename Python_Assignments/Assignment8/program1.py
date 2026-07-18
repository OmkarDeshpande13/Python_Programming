'''
1.Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.

Input : Number of elements : 6

Input Elements : 13     7   4   56  5   45

Output : 130

'''

def Addition(Arr):
    
    
    Sum = 0

    for icnt in range(len(Arr)):
          
          Sum = Sum + Arr[icnt]
          
    return Sum      
    
    


def main():

    iNo = 0
    Arr = []
    iRet = 0

    print("Enter The Number of Element in List : ")
    iNo = int(input())

    for i in range(0,iNo):
          
        A = int(input())
        Arr.append(A)
 
    print(Arr)

    iRet = Addition(Arr)
    print("Sum of Elements in List is : ",iRet)

if __name__ == "__main__":
        main()