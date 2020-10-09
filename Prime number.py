number = int(input("Enter a number:"))

for i in range(2,number+1):
    if i == number:
              if i == 2:
                  print("Prime number")
                  break
              elif i%2 == 0:
                 print("It is not a prime number")
                 break

else:
    print("Prime number")
