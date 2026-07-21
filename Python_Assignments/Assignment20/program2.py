'''
2: Design a Python application that creates two threads named EvenFactor and
OddFactor.

•Both threads should accept one integer number as a parameter.

•The EvenFactor thread should:

        ◦Identify all even factors of the given number.
        ◦Calculate and display the sum of even factors.

The OddFactor thread should:

        ◦Identify all odd factors of the given number.
        ◦Calculate and display the sum of odd factors.

After both threads complete execution, the main thread should display the message:

“Exit from main” 

'''

import threading

def EvenFactor(ino):
    print("Even Factors")

    isum = 0
    for i in range(1,ino+1):

        if((ino % i == 0) and (i % 2 == 0)):
            
            isum = isum + i
            print(i)
    print("Sum of Even Factors is :",isum)


def OddFactor(ino):

        print("Odd Factors")

        isum = 0
        for i in range(1,ino+1):
             
             if((ino % i == 0) and (i % 2 != 0)):
                  
                isum = isum + i
                print(i)
        print("Sum of Odd Factors is :",isum)



def main():

    ino = 0

    ino = int(input("Enter the Number : "))

    thread1 = threading.Thread(target=EvenFactor,args=(ino,))
    thread2 = threading.Thread(target=OddFactor,args=(ino,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    print("End of main..")

    

if __name__ == "__main__":
    main()