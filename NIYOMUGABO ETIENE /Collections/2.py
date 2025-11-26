# def Factorial(num):
#     factorial = 1
#     for n in range(1, num + 1):
#         factorial *= n
#     return factorial

# number = int(input("Enter number to caliculate factorial: "))
# print(Factorial(number))


# sorting a list of 10 number
nums = [1, 3, 5, 7, 10, 40, 60, 100, 120, 110]
# ascending
ascending = sorted(nums)
print("Ascending", ascending)

# descending 
descending = sorted(nums, reverse=True)
print("Descending", descending)