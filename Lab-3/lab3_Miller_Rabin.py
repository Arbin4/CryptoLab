# WAP to implement Miller-Rabin Algorithm
import random


def miller_rabin(n, k=5):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    # Write (n - 1) as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def is_composite(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    for _ in range(k):
        a = random.randrange(2, n - 1)
        if is_composite(a):
            return False

    return True


num = int(input("Enter a integer: "))
if miller_rabin(num):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")
