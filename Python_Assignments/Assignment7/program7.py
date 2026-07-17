                    
def Display(row,col):

    for i in range(row):

        for j in range(1,col+1):

            print(j,end=" ")
        print()



def main():

    rows =  int(input("Enter the Numbe rows : "))
    cols =  int(input("Enter the Number columns : "))

    Display(rows,cols)
if __name__ == "__main__":
    main()