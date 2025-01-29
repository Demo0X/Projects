
alphabets = {chr(i+97):i for i in range(0,26)}
text = input("Enter a text to encrypt: ")
shifted = int(input("Enter the shift key (a number): "))

def encrypt_caesar_cipher(plaintext, shift):
    encryptedtext = ""
    letters = [i for i in plaintext.lower()]
    for i in range(len(letters)):
        if letters[i] in alphabets:
            number = alphabets[letters[i]]
            answer = (number + shift) % 26
            for key, val in alphabets.items():
                if val == answer:
                    encryptedtext += key
    return encryptedtext

def decrypt_caesar_cipher(ciphertext, shift):
    plain_text = ""
    letters = [i for i in ciphertext.lower()]
    for i in range(len(letters)):
        if letters[i] in alphabets:
            number = alphabets[letters[i]]
            answer = (number - shift) % 26
            for key, val in alphabets.items():
                if val == answer:
                    plain_text += key
    return plain_text



encrypted = encrypt_caesar_cipher(text, shifted)

print(f"Encrypted text: {encrypted}")

decrypted = decrypt_caesar_cipher(encrypted, shifted)

print(f"Decrypted text: {decrypted}")
