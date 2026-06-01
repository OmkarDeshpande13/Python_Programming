Check_Even = lambda x : x % 2 == 0


Value = int(input("Enter First Number:"))


iRet = 0

iRet = Check_Even(Value)

if(iRet == True):
    print(True)
else:
    print("False")


