
'''Problem Statement:
Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
console.
'''

def Read(filename):

    fobj = open(filename,"r")

    data = fobj.read()

    print("Data from File is : ",data)

def main():

    FileName = input("Enter the name of File : ")

    Read(FileName)

if __name__ == "__main__":
    main()