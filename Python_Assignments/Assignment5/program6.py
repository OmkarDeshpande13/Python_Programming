from functools import reduce

minimum = lambda x, y : x if x < y else y

def main():

    Data = [10,20,30,40,50]
    print("Actual data is :",Data)

    min_number = reduce(minimum,Data)
    print("minimum is:",min_number)


if __name__ == "__main__":
    main()  