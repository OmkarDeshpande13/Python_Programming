'''
1: Design a Python application that creates two threads named Prime and NonPrime.

•Both threads should accept a list of integers.

•The Prime thread should display all prime numbers from the list.

•The NonPrime thread should display all non-prime numbers from the list.

''' 
import threading


def Prime(Arr):
        Brr = []
         
        for num in Arr:
             
             icount = 0
             for i in range(1,num+1):
                  
                if(num % i == 0):
                  
                    icount = icount + 1

             if(icount == 2):
             
                Brr.append(num)
        
        print("Prime Number List : ",Brr)
             
def NonPrime(Arr):

    Crr = []

    for num in Arr:
        icount = 0
        
        for i in range(1,num+1):

            if(num % i == 0):

                icount = icount + 1
        if(icount != 2):

            Crr.append("Non Prime Numbers From List are :",num)
    print(Crr)
def main():

    ino = 0
    Arr = []
    

    ino = int(input("Enter the Number of elements in list : "))

    for i in range(1,ino+1):

        ino1 = int(input()) 
        Arr.append(ino1)

    print(Arr)

    thread1 = threading.Thread(target=Prime,args=(Arr,))
    thread2 = threading.Thread(target=NonPrime,args=(Arr,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()