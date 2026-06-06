
LengthString = lambda x: len(x) > 5
    
def main():

    data = ['amit','Rahul','rajendra','yashraj']
    Fdata = filter(LengthString),data                                                                                       
    print("stings are:",Fdata)


if __name__ == "__main__":
    main()  