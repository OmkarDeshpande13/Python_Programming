
'''Problem Statement:
Write a program which accepts a file name and one string from the user and returns the frequency (count of
occurrences) of that string in the file.'''


import os

def main():

    FileName = input("Enter the Name of File : ")
    ret = os.path.exists(FileName)

    String = input("Enter the String to Search in the File : ")

    if(ret == True):

        with open(FileName,"r")as f:

            content =  f.read()
            words = content.splitlines()

            count = 0

            for i in words:
                    
                    count = count + i.count(String)

        
        print("the Number of Times String occerrences in the file is :",count)


if __name__ == "__main__":
    main()