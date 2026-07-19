
# Write a program to check whether it is Divisible by 3 and 5

def Divisible(Value):

    if((Value % 3) or (Value % 5)== 0):
        return True
    
    else:
        return False



def main():

    Value = int(input("Enter The Number:"))
    iRet = 0

    iRet = Divisible(Value)

    if(iRet == True):
        print(Value,"is Divisible by 3 an 5")

    else:
        print("Not Divisible")

if __name__ == "__main__":
    main()