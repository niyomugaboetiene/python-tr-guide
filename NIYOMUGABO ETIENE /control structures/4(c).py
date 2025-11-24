num = 1

while num < 50:
    num += 1
    if num == 5:
        continue
    # if num % 2 == 0:
    print(num)
    
    # second option for even numbers
while num < 50:
    num += 1
    if num == 5:
        continue
    if num % 2 == 0:
       print(f"{num} is even")
