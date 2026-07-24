'''2: Write a Python program to implement a class named BankAccount with the following
requirements:

The class should contain two instance variables:

◦Name (Account holder name)
◦Amount (Account balance)

The class should contain one class variable:

                ROI (Rate of Interest), initialized to 10.5

•Define a constructor (__init__) that accepts Name and initial Amount.

•Implement the following instance methods:

Display() - displays account holder name and current balance

Deposit() - accepts an amount from the user and adds it to balance

◦Withdraw() - accepts an amount from the user and subtracts it from balance

(Ensure withdrawal is allowed only if sufficient balance exists)

CalculateInterest() - calculates and returns interest using formula:

Interest = (Amount * ROI) / 100

Create multiple objects and demonstrate all methods.
'''

class BankAccount:

        ROI = 10.5

        def __init__(self,Name,Amount):
                
                self.Name = Name
                self.Amount = Amount
                

        def Display(self):
                
            self.currentBalance = self.Amount
            print("Account Holder :",self.Name)
            print("The current balance is : ",self.currentBalance)

        def Deposit(self,Amount):
               
               self.currentBalance = self.currentBalance + Amount
               print(Amount,": Amount is Deposited Successfully..")
               print("Balance After the Deposite :",self.currentBalance)

        def Withdraw(self,Amount):
               
               if(Amount < self.currentBalance):
                
                self.currentBalance = self.currentBalance - Amount
                print("Amount to Withdraw :",Amount)
                print("Balance After the Amount Withdrwal",self.currentBalance)

        def CalculateInterest(self):
              
              Interest = (self.Amount * BankAccount.ROI) / 100
              print("The rate of Interest is : ",Interest)


obj1 = BankAccount("Amit",25000)
obj1.Display()
obj1.Deposit(2000)
obj1.Withdraw(1000)
obj1.CalculateInterest()

print("\n")

obj2 = BankAccount("Omkar",35000)
obj2.Display()
obj2.Deposit(6000)
obj2.Withdraw(11000)
obj2.CalculateInterest()