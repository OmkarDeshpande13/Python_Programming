CheckMax = lambda x,y : x > y


Value1 = int(input("Enter First Number:"))
Value2 = int(input("Enter Second Number:"))


iRet = 0

iRet = CheckMax(Value1,Value2)

if(iRet == True):
    print(Value1,"is Max Number")
else:
    print(Value2,"is Max Number")



