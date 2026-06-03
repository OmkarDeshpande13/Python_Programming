
# Write a program to calculate the Addition,Substraction,Multiplication and Division of two Numbers

def Addition(No1,No2):

        sum = 0
        Sum = No1 + No2

        print("Addition is :",Sum)
    
def Substraction(No1,No2):
     
     Sub = 0
     Sub = No1 - No2

     print("Substarction is:",Sub)

def Multiplication(No1,No2):
     
     Multi = 0
     Multi = No1 * No2

     print("Multiplication is :",Multi)

def Division(No1,No2):
     
     Division = No1 / No2
     print("Division is :",Division)




def main():

    Value1 = int(input("Enter First Number:"))
    Value2 = int(input("Enter second Number:"))

    Addition(Value1,Value2)
    Substraction(Value1,Value2)
    Multiplication(Value1,Value2)
    Division(Value1,Value2)
    


if __name__ == "__main__":
    main()