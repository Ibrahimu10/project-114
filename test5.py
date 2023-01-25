def pie():
  option=int(input("Enter Option 1:Full Number 2:Decimal Number"))
  if option==1:
    num1=int(input("Enter Radius:"))
    num3=num1*num1
    print("First Step(Square The Radius)=",num3)
    num4=num3*3.14159265358979324
    print("Second Step(Multiply It By Pi)=",num4)
  elif option==2:
    num1=float(input("Enter Radius:"))
    
    num3=num1*num1
    print("First Step(Square The Radius) =",num3)
    num4=num3*3.14159265358979324
    print("Second Step(Multiply It By Pi) =",num4)
    print("So the answer is: ", num4)
pie()