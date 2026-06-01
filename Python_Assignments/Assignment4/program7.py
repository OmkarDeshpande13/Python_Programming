Check_Divisible = lambda x : x % 5 == 0


Value = int(input("Enter First Number:"))


iRet = 0

iRet = Check_Divisible(Value)

if(iRet == True):
    print(True)
else:
    print(False)


