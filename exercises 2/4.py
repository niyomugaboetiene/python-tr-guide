for num in range(0, 21):
    for i in range(0, num):
        if i % num == 0:
            break

print(f"{num} is prime")