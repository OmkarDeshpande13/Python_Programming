CheckMin = lambda x,y : x < y


Value1 = int(input("Enter First Number:"))
Value2 = int(input("Enter Second Number:"))


iRet = 0

iRet = CheckMin(Value1,Value2)

if(iRet == True):
    print(Value1,"is min Number")
else:
    print(Value2,"is min Number")



