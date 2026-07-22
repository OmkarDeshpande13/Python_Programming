'''
Design a Python application that creates two threads.

•Thread 1 should compute the sum of elements from a list.

•Thread 2 should compute the product of elements from the same list.


'''

import threading

def Sum(Arr):
                 
      isum = 0
      for i in range(1,len(Arr)):
            
            isum = isum + Arr[i]

      print(isum)          

def Product(Arr):

      
      iprod = 1
      for i in range(1,len(Arr)):
            
            iprod = iprod * Arr[i]

      print(iprod)           

def main():

    ino = 0
    Arr = []

    ino = int(input("Enter the Number of elements in list : "))

    for i in range(1,ino+1):

        ino1 = int(input()) 
        Arr.append(ino1)

    print(Arr)

    thread1 = threading.Thread(target=Sum,args=(Arr,))
    thread2 = threading.Thread(target=Product,args=(Arr,))

    thread1.start()
    iret = thread1.join()

    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()