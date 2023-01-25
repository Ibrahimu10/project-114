def caculate():
  option=int(input("Enter Option 1:Addition 2:Subtraction 3:Division 4:Multiply "))
  if option==1:
    num1=int(input("Enter First Number"))
    num2=int(input("Enter Second Number"))
    num3=num1+num2
    print("Answer",num3)
  elif option==2:
    num1=int(input("Enter First Number"))
    num2=int(input("Enter Second Number"))
    num3=num1-num2
    print("Answer",num3)
  elif option==3:
    num1=int(input("Enter First Number"))
    num2=int(input("Enter Second Number"))
    num3=num1/num2
    print("Answer",num3)
  elif option==4:
    num1=int(input("Enter First Number"))
    num2=int(input("Enter Second Number"))
    num3=num1*num2
    print("Answer",num3)
  if num3>100:
    print("Your number is bigger than 100")
  if num3<100:
    print("Your number is smaller than 100")
caculate()