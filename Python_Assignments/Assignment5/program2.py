
Even = lambda No: No % 2 == 0


def main():

    Data = [10,21,11,15,30,50]
    print("Actual data is :",Data)

    Fdata = list(filter(Even,Data))
    print("filtered data is:",Fdata)


if __name__ == "__main__":
    main()  
