
def square(No):
    return No ** 2

def main():

    Data = [10,20,30,40,50]
    print("Actual data is :",Data)

    Mdata = list(map(lambda No :(No ** 2),Data))
    print("Data After Mapping is:",Mdata)


if __name__ == "__main__":
    main()  