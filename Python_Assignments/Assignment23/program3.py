'''
3: Write a Python program to implement a class named Numbers with the following
specifications:

The class should contain one instance variable:

                ◦Value

•Define a constructor (__init__) that accepts a number from the user and initializes Value.

•Implement the following instance methods:

◦ChkPrime() - returns True if the number is prime, otherwise returns False

◦ChkPerfect() - returns True if the number is perfect, otherwise returns False

◦Factors() - displays all factors of the number
             returns the sum of all factors

(You may use this method as a helper in ChkPerfect() if required)

Create multiple objects and call all methods.
'''

class Numbers:
        
        NoOfBooks = 0

        def __init__(self):
                
                self.Value = 0
                

        def Accept(self):

                self.Value = int(input("Enter the Number : "))

        def Factors(self):

                Sum = 0
                for i in range(1,self.Value):

                        if(self.Value % i == 0):
                                
                                print(i)

                                Sum = Sum + i
                print("Sum of factors are : ",Sum)
                return Sum
                
        def ChkPerfect(self,Sum):

                if(Sum == self.Value):
                        print("The Number is Perfect")
                else:
                        print("The Number is Not Perfect")

        def ChkPrime(self):
                
                icount = 0
                for i in range(1,self.Value):
                        
                        if(self.Value < 2):
                                return

                        elif(self.Value % i == 0):

                                icount = icount + 1

                if(icount <= 2):
                        return True
                else:
                        return False



obj1 = Numbers()
obj1.Accept()
sum = obj1.Factors()
obj1.ChkPerfect(sum)
Bret = obj1.ChkPrime()
if(Bret == True):
        print("It is Prime Number")
else:
        print("It is Not a Prime Number")


obj2 = Numbers()
obj2.Accept()
sum = obj2.Factors()
obj2.ChkPerfect(sum)
Bret = obj2.ChkPrime()
if(Bret == True):
        print("It is Prime Number")
else:
        print("It is Not a Prime Number")

