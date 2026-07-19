
# Write a Program which gets 2 values from User and Check the Greater value 

def ChkGreater(Value1,Value2):

    if(Value1 > Value2):
        return True
    
    else:
        return False




def main():

    Value1 = int(input("Enter First Number:"))
    Value2 = int(input("Enter Second Number:"))
    iRet = False


    iRet = ChkGreater(Value1,Value2)

    if(iRet == True):

        print(Value1," is Greater")
    else:

        print(Value2," is Greater")

if __name__ == "__main__":
    main()