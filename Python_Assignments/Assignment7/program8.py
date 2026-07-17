                    
def Display(row,col):

    for i in range(1,row+1):

        for j in range(1,i+1):
            print(j,end=" ")

        print("\r")



def main():

    rows =  int(input("Enter the Numbe rows : "))
    cols =  int(input("Enter the Number columns : "))

    Display(rows,cols)

if __name__ == "__main__":
    main()