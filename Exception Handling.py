
a = 5
b = 0

try:
    print("ON")
    print(a/b)

except Exception as e:
    print(e)

finally:
    try:
        n = int(input("Enter a number:"))
        print("After getting an input!")
    except ValueError:
        print("Something wrong")

    print("OFF")

print("Hello world")


