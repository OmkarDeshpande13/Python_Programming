# 5. Write a program which accepts a file name and a word from the user and checks whether that word is present in

import os

def main():

    FileName = input("Enter the File Name : ")
    ret = os.path.exists(FileName)

    Word = input("enter the Word to Find in the File : ")

    if(ret == True):

        with open(FileName,"r") as f :

            Content = f.read()
            File_words = Content.split()
            
            for i in File_words:

                if(Word == i):

                    print(Word,"Word is Present in the File : ",FileName)
                
if __name__ == "__main__":
    main()