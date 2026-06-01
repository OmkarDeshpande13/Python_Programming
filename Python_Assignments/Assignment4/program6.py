Check_Odd = lambda x : x % 2 != 0


Value = int(input("Enter First Number:"))


iRet = 0

iRet = Check_Odd(Value)

if(iRet == True):
    print(True)
else:
    print(False)


