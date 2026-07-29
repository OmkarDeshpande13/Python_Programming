
# 4. Write a program which accepts two file names from the user.

import os

def main():

    FileName_main = input("Enter the Name of Main File : ")

    ret1 = os.path.exists(FileName_main)

    Filename_Copy = input("Enter the Name of Copy File :")


    if(ret1 == True):

        with open(FileName_main,"r") as f:

            Main_Content = f.read()

            with open(Filename_Copy,"w")as copy_f:

                copy_f.write(Main_Content)

                print("Content from main File Copied Successfully.")



if __name__ == "__main__":
    main()