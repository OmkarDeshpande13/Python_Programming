'''
5: Design a Python application that creates two threads named Thread1 and Thread2.

•Thread1 should display numbers from 1 to 50.

•Thread2 should display numbers from 50 to 1 in reverse order.

•Ensure that:

            ◦Thread2 starts execution only after Thread1 has completed.


Use appropriate thread synchronization
'''

import threading

def Thread1(ino):

    for i in range(1,ino+1):

        print(i)

def Thread2(ino):

    for i in range(ino,0,-1):
        
        print(i)

   
    
def main():

    ino = 0

    ino = int(input("Enter the Number : "))

    thread1 = threading.Thread(target=Thread1,args=(ino,))

    thread2 = threading.Thread(target=Thread2,args=(ino,))

    # Execute in parallel

    thread1.start()
    thread1.join()  # Thread 2 Wating

    print("\n")

    thread2.start()
    thread2.join()


if __name__ == "__main__":
    main()