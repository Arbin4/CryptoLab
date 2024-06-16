# WAP to find primitive roots
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_primitive_root(g, n):
    if gcd(g, n) != 1:
        return False

    required_set = set(range(1, n))
    actual_set = set()

    for k in range(1, n):
        actual_set.add(pow(g, k, n))

    return required_set == actual_set


def find_primitive_roots(n):
    primitive_roots = []
    for g in range(1, n):
        if is_primitive_root(g, n):
            primitive_roots.append(g)
    return primitive_roots


num = int(input("Enter a integer: "))
print(f"Primitive Root of {num} is {find_primitive_roots(num)}")
