
'''Problem Statement:
Write a program which accepts a file name from the user and checks whether that file exists in the current
directory or not.'''

import os

def main():

    FileName = input("Enter the name of File : ")

    Ret = os.path.exists(FileName)

    if(Ret == True):

        print("File is Exists in current directory..")
    else:
        print("There is no such file..")

if __name__ == "__main__":
    main()