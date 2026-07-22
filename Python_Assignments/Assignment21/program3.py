'''
3: Design a Python application that creates two threads named EvenList and OddList.

•Both threads should accept a list of integers as input.

•The EvenList thread should:

                Extract all even elements from the list.

◦               Calculate and display their sum.

The OddList thread should:

◦               Extract all odd elements from the list.

◦               Calculate and display their sum.

Threads should run concurrently.
'''

import threading

def EvenList(ino):

    EvenList = []
    SumEven = 0

    for i in range(ino+1):

        if(i % 2 == 0):

            SumEven = SumEven + i
            EvenList.append(i)

    print("Even Elements are : ",EvenList)   
    print("Sum of Even Numbers are : ",SumEven)

def Odd(ino):

    sumOdd = 0
    OddList = []

    for i in range(0,ino):

        if(i % 2 != 0):

            sumOdd = sumOdd + i
            OddList.append(i)
    
    print("Odd Elements are : ",OddList)
    print("Sum of Odd elements are : ",sumOdd)
    
def main():


    ino = int(input("Enter the Number : "))


    thread1 = threading.Thread(target=EvenList,args=(ino,))

    thread2 = threading.Thread(target=Odd,args=(ino,))

    # Execute in parallel

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()