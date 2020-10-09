
# At first we get three numbers

number1 = int(input("Enter 1st number:"))
number2 = int(input("Enter 2nd number:"))
number3 = int(input("Enter 3rd number:"))

if (number1>number2) & (number1>number3):
    print(str(number1)+" is the max number")

elif (number2>number1) & (number2>number3):
    print(str(number2)+" is the max number")

elif (number3 > number1) & (number3 > number2):
    print(str(number3)+" is the max number")
