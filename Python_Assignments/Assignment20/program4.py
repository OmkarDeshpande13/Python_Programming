'''
4: Design a Python application that creates three threads named Small, Capital, and
Digits.

•All threads should accept a string as input.

•The Small thread should count and display the number of lowercase characters.

•The Capital thread should count and display the number of uppercase characters.

•The Digits thread should count and display the number of numeric digits.

•Each thread must also display:

                 Thread ID
                 Thread Name

'''

import threading
import string

def Small(str):
        
        print("Small Character Thread : ",threading.get_ident())
        print("small character thread name : ",threading.current_thread())
        letters = ""
        count = 0
        for ch in str:
        
            if(ch.islower()):
                 
                letters = letters + ch + ""
                count = count + 1
                 
       
        print("Small Letters are : ",letters)
        print("Number of Small Letters are :",count)
       
def Capital(str):

        print("Capital Character Thread : ",threading.get_ident())
        print("Capital character thread name : ",threading.current_thread())

        letters = "" 
        count = 0

        for ch in str:
             
             if(ch.isupper()):
                  
                  letters = letters + ch +""
                  count = count + 1
        
        print("Capital Letters are : ",letters)
        print("Number of Capital Letters are :",count)

def Digits(str):
        
    print("Digit thread name : ",threading.current_thread())
    print("Digit : ",threading.get_ident())
    digits = ""
    count = 0

    for ch in str:
         if ch.isdigit():

              digits = digits + ch + ""
              count = count + 1

    print("Digits are : ",digits)
    print("Number of Digits are :",count)


def main():

    str = "abcd1234ABCD"

    thread1 = threading.Thread(target=Small,args=(str,))
    thread2 = threading.Thread(target=Capital,args=(str,))
    thread3 = threading.Thread(target=Digits,args=(str,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    thread3.start()
    thread3.join()
    

if __name__ == "__main__":
    main()