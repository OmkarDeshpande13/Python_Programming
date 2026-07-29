
# 3. Write a program which accepts a file name from the user and displays the contents of the file line by line on the
#screen

import os

def main():

    FileName = input("Enter the Name of File : ")

    ret = os.path.exists(FileName)

    if(ret == True):

        with open(FileName,"r")as f:

            for text in f:

                f.seek(0)
                text = (f.read().splitlines())            
    
    for t in text:

        print(t)



if __name__ == "__main__":
    main()