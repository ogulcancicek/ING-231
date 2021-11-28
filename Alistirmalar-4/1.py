plainText = "bugunhavacokguzel"

# remove punctuations and blanks
def clear_text(text):
    for char in text:
        if not(char.isalpha()):
            text = text.replace(char,"")
    return text

def encrypt_text(plainText,num):
    letters = list(plainText)
    for idx,letter in enumerate(letters):
        ascii_val = ord(letter) + num
        if ascii_val > 122:
            ascii_val = 96 + (ascii_val - 122)
        letters[idx] = chr(ascii_val)
    encrypted_text = "".join(letters)
    return encrypted_text

def decrypt_text(encrypted_text,num):
    letters = list(encrypted_text)
    for idx,letter in enumerate(letters):
        ascii_val = ord(letter) - num
        if ascii_val < 97:
            ascii_val = 123 + (ascii_val - 97)
        letters[idx] = chr(ascii_val)
    decrypted_text = "".join(letters)
    return decrypted_text


plainText = clear_text(plainText)
print(plainText)
encrypted_text = encrypt_text(plainText,5)
print(encrypted_text)
decrypted_text = decrypt_text(encrypted_text,5)
print(decrypted_text)