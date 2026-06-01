
def Prime(Value):

    if Value < 2 :
        return False
    if Value == 2:
        return True
    if Value % 2 == 0:
        return False
    
    for i in range(3,Value):

        if(Value % i == 0):
            return False
        i = i + 2

    return True

def main():
    
    Value = int(input("Enter the Number:"))
    iRet = 0
    iRet = Prime(Value)

    if(iRet == True):
        print(Value,"is prime Number")
    else:
        print(Value,"is not a prime Number")



if __name__ == "__main__":
    main()