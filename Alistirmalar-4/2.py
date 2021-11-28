from math import sqrt

plainText = 'bugünhavaçokgüzel'

# Find matrix size (n x n)
def find_size_of_matrix(num):
    if sqrt(num).is_integer():
        return int(sqrt(num))
    else:
        num += 1
        return find_size_of_matrix(num)

# Create matrix
def create_matrix(size):
    matrix = []
    for i in range(size):
        matrix.append([])
    return matrix

# Append letters into matrix and create ceaser box 
def create_ceaser_box(text,size):
    ceasar_box = create_matrix(size)
    current_row = 0
    for letter in text:
        ceasar_box[current_row].append(letter)
        if current_row == (size-1):
            current_row = 0
        else:
            current_row += 1
    return ceasar_box

def create_encrypted_text(matrix):
    encrypted_text = ""
    for row in matrix:
        encrypted_text += "".join(row)
    return encrypted_text

# Take encrypted text as an argument and created ceaser matrix
def create_ceaser_box_from_encyrpted_text(text,size):
    matrix = create_matrix(size)
    cursor = 0
    for row in range(size):
        matrix[row] = list(text[cursor:cursor + size])
        cursor += size
    return matrix

# Decrypt ceaser box
def decrypt_text(text,size):
    decrypted_text = ""
    matrix = create_ceaser_box_from_encyrpted_text(text, size)
    for col in range(size):
        for row in range(len(matrix[col])):  ##### IndexError: list index out of range
            decrypted_text += matrix[row][col]
    return decrypted_text

    
size = find_size_of_matrix(len(plainText))

ceaser_box = create_ceaser_box(plainText,size)
for row in ceaser_box:
    print(row)
print("-"*15)

encrypted_text = create_encrypted_text(ceaser_box)
print("Encrypted Text: ",encrypted_text)
print("-"*15)

decrypted_text = decrypt_text(encrypted_text,size)
print("Decrypted Text: ",decrypted_text)
print("-"*15)