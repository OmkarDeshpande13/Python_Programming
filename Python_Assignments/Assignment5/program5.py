from functools import reduce

maximum = lambda x, y : x if x > y else y

def main():

    Data = [10,20,30,40,50]
    print("Actual data is :",Data)

    max_number = reduce(maximum,Data)
    print("Maximum is:",max_number)


if __name__ == "__main__":
    main()  