'''
3: Write a Python program to implement a class named Arithmetic with the following
characteristics:

•The class should contain two instance variables: Value1 and Value2.

•De ne a constructor (__init__) that initializes all instance variables to 0.

•Implement the following instance methods:

◦Accept() - accepts values for Value1 and Value2 from the user.

◦Addition() - returns the addition of Value1 and Value2.

◦Subtraction() - returns the subtraction of Value1 and Value2.

◦Multiplication() - returns the multiplication of Value1 and Value2.

◦Division() - returns the division of Value1 and Value2 (handle division by zero
properly).

Create multiple objects of the Arithmetic class and invoke all the instance methods.
'''

class Arithmatic:

    PI = 3.14

    def __init__(self):

        self.value1 = 0
        self.value2 = 0


    def Accept(self):

        self.value1 = float(input("Enter the first Number : "))
        self.value2 = float(input("Enter the second Number : "))

    def Addition(self):

        return self.value1 + self.value2

    def Substraction(self):

        return self.value1 - self.value2
    
    def Multiplication(self):

        return self.value1 * self.value2
    
    #def Division(self):

    def Division(self):

        if(self.value1 <= 0):
            return
        if(self.value2 <=0):
            return
        else:
           return self.value1 / self.value2

      


obj1 = Arithmatic()
obj1.Accept()

Ans = obj1.Addition()
print("Addition is :",Ans)


obj2 = Arithmatic()
obj2.Accept()

Ans = obj2.Substraction()
print("Substraction is : ",Ans)


obj3 = Arithmatic()
obj3.Accept()

Ans = obj3.Multiplication()
print("Multiplication is : ",Ans)

obj4 =  Arithmatic()
obj4.Accept()

Ans = obj4.Division()
print("Division is : ",Ans)

        
