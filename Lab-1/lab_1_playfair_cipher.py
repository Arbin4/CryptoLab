def generate_playfair_key_matrix(key):
    key = "".join(sorted(set(key), key=lambda x: key.index(x)))  # Remove duplicates while preserving order
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I and J are considered the same
    key_matrix = []

    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)

    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)

    matrix = [key_matrix[i:i + 5] for i in range(0, 25, 5)]
    return matrix


def format_plaintext(plain_text):
    plain_text = plain_text.upper().replace("J", "I")
    formatted_text = ""

    i = 0
    while i < len(plain_text):
        formatted_text += plain_text[i]
        if i + 1 < len(plain_text) and plain_text[i] == plain_text[i + 1]:
            formatted_text += 'X'
        elif i + 1 < len(plain_text):
            formatted_text += plain_text[i + 1]
        else:
            formatted_text += 'X'
        i += 2

    return formatted_text


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def playfair_encrypt(plain_text, key):
    matrix = generate_playfair_key_matrix(key)
    formatted_text = format_plaintext(plain_text)
    cipher_text = ""

    for i in range(0, len(formatted_text), 2):
        char1, char2 = formatted_text[i], formatted_text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            cipher_text += matrix[row1][(col1 + 1) % 5]
            cipher_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1 + 1) % 5][col1]
            cipher_text += matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += matrix[row1][col2]
            cipher_text += matrix[row2][col1]

    return cipher_text


def playfair_decrypt(cipher_text, key):
    matrix = generate_playfair_key_matrix(key)
    plain_text = ""

    for i in range(0, len(cipher_text), 2):
        char1, char2 = cipher_text[i], cipher_text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            plain_text += matrix[row1][(col1 - 1) % 5]
            plain_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += matrix[(row1 - 1) % 5][col1]
            plain_text += matrix[(row2 - 1) % 5][col2]
        else:
            plain_text += matrix[row1][col2]
            plain_text += matrix[row2][col1]

    return plain_text


# Full name to be encrypted and decrypted
full_name = "Arabinda Sigdel"
# Key for the Playfair Cipher
key = "PLAYFAIR"

# Encrypt the full name
formatted_name = full_name.upper().replace(" ", "").replace("J", "I")
encrypted_name = playfair_encrypt(formatted_name, key)
print(f"Encrypted Name: {encrypted_name}")

# Decrypt the full name
decrypted_name = playfair_decrypt(encrypted_name, key)
print(f"Decrypted Name: {decrypted_name}")
