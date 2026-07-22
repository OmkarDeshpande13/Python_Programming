'''
2: Design a Python application that creates two threads.

•Thread 1 should calculate and display the maximum element from an list.

•Thread 2 should calculate and display the minimum element from the same list.

•The list should be accepted from the user. 

'''

import threading

def MaxElement(Arr):
        
        imax = 0
        for i in range(len(Arr)):
                if(Arr[i] > imax):
                        
                        imax = Arr[i]
        print("Maximum Element from List is : ",imax)

def MinElement(Arr):
      
      imin = Arr[0]
      for i in range(1,len(Arr)):
            
            if(Arr[i] < imin):
                  
                  imin = Arr[i]

      print("Minimum Element from List is : ",imin)            

def main():

    ino = 0
    Arr = []

    ino = int(input("Enter the Number of elements in list : "))

    for i in range(1,ino+1):

        ino1 = int(input()) 
        Arr.append(ino1)

    print(Arr)

    thread1 = threading.Thread(target=MaxElement,args=(Arr,))
    thread2 = threading.Thread(target=MinElement,args=(Arr,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()