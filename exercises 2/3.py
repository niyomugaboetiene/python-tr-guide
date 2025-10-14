multiply = 2
for num in range(11):
    if num == 0:
        continue
    multiply *= num
    print(num ,"X", multiply, "=", num)