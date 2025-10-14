for num in range(2, 21):
    for i in range(2, num):
        if i % num == 1:
            continue

    print(f"{num} is prime")