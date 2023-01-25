num1=input("Enter Number: ")
num2=input("Enter Number: ")

def number():
    if num1 > num2:
        print(num1 + " is greater than " + num2)
    elif num1 == num2:
        print(num1 + " and " + num2 + " are equal")
    elif num2 > num1:
        print(num2 + " is greater than " + num1)

number()

