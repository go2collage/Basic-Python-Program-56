# Python Program

# Exception: ZeroDivisionError

num1 = int(input("Enter first Integer Number: "))
num2 = int(input("Enter second Integer Number: "))

# Overcome it by using try-except block
try:
    div = num1 / num2
    print(f" {num1} / {num2} Division is: ", div)
except Exception:
    print("Can't divide by zero.")

# Thanks for Watching