'''
1: Write a Python program to implement a class named Demo with the following
specifications:

•The class should contain two instance variables: no1 and no2.

•The class should contain one class variable named Value.

•Define a constructor (__init__) that accepts two parameters and initializes the instance variables.

•Implement two instance methods:

◦Fun() - displays the values of instance variables no1 and no2.
◦Gun() - displays the values of instance variables no1 and no2.

'''

class Demo:

    value = 0

    def __init__(self,no1,no2):

        self.i = no1
        self.j = no2

    
    def fun(self):

        print("Inside fun")
        print(self.i,self.j)

    def gun(self):

        print("Inside gun")
        print(self.i,self.j)

    

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()
        