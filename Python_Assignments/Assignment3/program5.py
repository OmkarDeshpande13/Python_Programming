
# Write a program which checks the mark and gives the grade according to the marks

def DisplayGrade(Marks):

    if(Marks >= 75):
        print("Distinction")
    elif (Marks >= 60):
        print("Second class")
    elif(Marks >= 50):
        print("First class")
    else:
        print("Fail")

def main():

    Value = int(input("Enter the Number:"))

    DisplayGrade(Value)

if __name__ == "__main__":
    main()