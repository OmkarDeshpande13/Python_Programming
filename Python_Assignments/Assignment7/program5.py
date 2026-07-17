def prime(No):
    freq = 0
    for i in range(1,No,1):

        if(No % i == 0):
            freq = freq + i
        
    if(freq > 2):
            return True
    else:
            return False   
       



def main():

    Value = int(input("Enter the Number : "))
    
    iRet = prime(Value)

    if (iRet == True):
        print("It is not prime")
    else:
        print("It isPrime")
        


if __name__ == "__main__":
    main()