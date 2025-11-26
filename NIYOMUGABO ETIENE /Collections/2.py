def Factorial(num):
    factorial = 1
    for n in range(1, num + 1):
        factorial *= n
    return factorial

number = int(input("Enter number to caliculate factorial: "))
print(Factorial(number))