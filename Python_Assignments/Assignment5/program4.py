from functools import reduce

Addition = lambda A,B : A + B

def main():

    Data = [10,20,30,40,50]
    print("Actual data is :",Data)

    Rdata = reduce(Addition,Data)
    print("Addition is:",Rdata)


if __name__ == "__main__":
    main()  