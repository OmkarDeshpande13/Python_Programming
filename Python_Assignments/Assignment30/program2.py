
# 2. Write a program which accepts a file name from the user and counts the total number of words in that file.

import os

def main():

    FileName = input("Enter the Name of File : ")

    ret = os.path.exists(FileName)

    if(ret == True):

        with open(FileName,"r") as f:

            content = f.read()
            words = content.split()
            Num_of_words = len(words)
        print("Number of Words in the File are : ",Num_of_words)

    else:
        print("File Not Exists")

if __name__ == "__main__":
    main()