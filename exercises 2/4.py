for num in range(2, 21):
    for i in range(2, num):
        if num % i == 0:
            continue

    print(f"{num} is prime")