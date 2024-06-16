# WAP to implement RSA Algorithm
import random
from sympy import randprime


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    def find_e(phi):
        e = random.randrange(2, phi)
        while gcd(e, phi) != 1:
            e = random.randrange(2, phi)
        return e

    e = find_e(phi)
    d = pow(e, -1, phi)
    return (e, n), (d, n)


def encrypt_rsa(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]


def decrypt_rsa(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])


# Example usage:
p = randprime(10 ** 2, 10 ** 3)
q = randprime(10 ** 2, 10 ** 3)

public_key, private_key = generate_keypair(p, q)
plaintext = "Arabinda Sigdel"
ciphertext = encrypt_rsa(public_key, plaintext)
decrypted_message = decrypt_rsa(private_key, ciphertext)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted message: {decrypted_message}")
