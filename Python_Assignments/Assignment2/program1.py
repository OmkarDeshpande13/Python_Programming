
# Write a Program to check if the Character is a Vowel

def Vowel(ch):

    if(ch =='a' or ch == 'e' or ch == 'i'or ch == 'o' or ch == 'u' 
        or ch =='A' or ch == 'E' or ch == 'I'or ch == 'O' or ch == 'U'):
        
        return True
    
    else:
        return False
    
    


def main():

    ch = str(input("Enter the Character:"))
    iret = False

    iret = Vowel(ch)

    if(iret == True):
        print(ch,"is a Vowel")
    else:
        print("It is not a vowel")

if __name__ == "__main__":
    main()