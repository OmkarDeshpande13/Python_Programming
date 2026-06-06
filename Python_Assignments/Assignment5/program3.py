
Odd = lambda No: No % 2 != 0


def main():

    Data = [10,11,21,30,50,51]
    print("Actual data is :",Data)

    Fdata = list(filter(Odd,Data))
    print("filtered data is:",Fdata)


if __name__ == "__main__":
    main()  