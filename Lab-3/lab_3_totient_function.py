# WAP to implement Euler's Totient Function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def euler_totient(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count


num = int(input("Enter a integer: "))
print(f"Totient Function of {num} is {euler_totient(num)}")
