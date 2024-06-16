# WAP to implement Diffie-Hellman Key Exchange Algorithm
def diffie_hellman(p, g, private_key_a, private_key_b):
    A = pow(g, private_key_a, p)
    B = pow(g, private_key_b, p)
    shared_secret_a = pow(B, private_key_a, p)
    shared_secret_b = pow(A, private_key_b, p)

    assert shared_secret_a == shared_secret_b
    return shared_secret_a


p = 23
g = 5

private_key_a = 6
private_key_b = 15

shared_secret = diffie_hellman(p, g, private_key_a, private_key_b)
print(shared_secret)
