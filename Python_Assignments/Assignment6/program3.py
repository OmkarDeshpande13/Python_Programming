
def Add(No1,No2):

    sum = No1 + No2
    return sum
    

def main():

    Value1 = int(input("Enter the Number:"))
    Value2 = int(input("Enter the Number:"))
    iRet = 0

    iRet = Add(Value1,Value2)
    print("Summation is :",iRet)
    
if __name__ == "__main__":
    main()