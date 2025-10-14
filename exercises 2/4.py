for num in range(2, 21):   # start from 2, since 0 and 1 aren't prime
    for i in range(2, num):
        if num % i == 0:   # if divisible, not prime
            break
    else:                  # loop finished without finding a divisor
        print(f"{num} is prime")
