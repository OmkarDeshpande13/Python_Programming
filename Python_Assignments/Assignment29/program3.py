
'''
Problem Statement:
Write a program which accepts an existing file name through command line arguments, creates a new file
named Demo.txt, and copies all contents from the given file into Demo.txt.
'''

import os
import sys

def Copy(filenamesrc,FileNamedest):

    # Read the Data From Existing File
    fsobj = open(filenamesrc,"r")

    data = fsobj.read()

    # Write the Data into Destination File

    fdobj = open(FileNamedest,"w")

    fdobj.write(data)
    
    print("Data is Successfully written in the File..")





def main():

    FileNameSrc = str(sys.argv[1])

    FileNameDest = str(sys.argv[2])

    Copy(FileNameSrc,FileNameDest)

if __name__ == "__main__":
    main()

    