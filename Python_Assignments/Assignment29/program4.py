
'''Problem Statement:
Write a program which accepts two file names through command line arguments and compares the contents of
both files.'''

import os
import sys

def CheckSameContent(filenamesrc,FileNamedest):

    fsobj = open(filenamesrc,"r")

    Sdata = fsobj.read()

    fdobj = open(FileNamedest,"r")

    Ddata = fdobj.read()

    if(Sdata == Ddata):
        print("Success")
    else:
        print("Failure")


def main():

    FileNameSrc = str(sys.argv[1])

    FileNameDest = str(sys.argv[2])

    CheckSameContent(FileNameSrc,FileNameDest)

if __name__ == "__main__":
    main()

    