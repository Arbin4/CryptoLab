import random
from sympy import randprime


def elgamal_generate_keys(p, g):
    private_key = random.randrange(2, p - 1)
    public_key = pow(g, private_key, p)
    return private_key, public_key


def elgamal_encrypt(p, g, public_key, plaintext):
    k = random.randrange(2, p - 1)
    a = pow(g, k, p)
    b = [(ord(char) * pow(public_key, k, p)) % p for char in plaintext]
    return a, b


def elgamal_decrypt(p, private_key, a, ciphertext):
    s = pow(a, private_key, p)
    plaintext = ''.join([chr((char * pow(s, -1, p)) % p) for char in ciphertext])
    return plaintext


# Example usage:
p = randprime(10 ** 2, 10 ** 3)
g = 2  # primitive root modulo p

private_key, public_key = elgamal_generate_keys(p, g)
plaintext = "Arabinda Sigdel"
a, ciphertext = elgamal_encrypt(p, g, public_key, plaintext)
decrypted_message = elgamal_decrypt(p, private_key, a, ciphertext)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted message: {decrypted_message}")
