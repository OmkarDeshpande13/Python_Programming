'''
1: Design a Python application that creates two separate threads named Even and Odd.

•The Even thread should display the First 10 even numbers.

•The Odd thread should display the First 10 odd numbers.

•Both threads should execute independently using the threading module.

•Ensure proper thread creation and execution.
'''

import threading

def Even(ino):
    for i in range(ino+1):

        if(i % 2 == 0):

            print("Even Numbers are : ",i)

    print("\n")   

def Odd(ino):
    for i in range(0,ino):

        if(i % 2 != 0):

            print("Odd Numbers are : ",i)

def main():

    ino = 0

    ino = int(input("Enter the Number : "))

    thread1 = threading.Thread(target=Even,args=(ino,))

    thread2 = threading.Thread(target=Odd,args=(ino,))

    # Execute in parallel

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()