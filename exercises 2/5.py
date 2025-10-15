# import math

# num = int(input("Enter number: "))
# print(f"Factorial of {num} is {math.factorial(num)}")

# or use logic not built-in function of python
num = int(input("Enter number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")