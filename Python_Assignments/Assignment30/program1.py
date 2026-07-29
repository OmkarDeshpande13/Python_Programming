
# 1. Write a program which accepts a file name from the user and counts how many lines are present in the file.

import os

def main():

    FileName = input("Enter the name of File :")

    ret = os.path.exists(FileName)

    if(ret == True):

        with open(FileName,"r") as f:
            
            line_count = len(f.readlines())
    else:
        print("File Not Exist...")
    
    print("The Number of Line File has : ",line_count)






if __name__ == "__main__":
    main()