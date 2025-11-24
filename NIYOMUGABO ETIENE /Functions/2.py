num = int(input("Enter number to caliculate factorial: "))
factorial = 1

for n in range(1, num + 1):
    factorial *= n

print(factorial) 