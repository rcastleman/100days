# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(text,shift,direction):
    notepad = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == 'encode':
            new_position = position + shift
        elif direction == 'decode':
            new_position = position - shift
        new_letter = alphabet[new_position]
        notepad += new_letter
    print(f"The result is {notepad}")

ceasar(text,shift,direction)

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(plain_text)

# if direction == 'encode':
#     encrypt(plain_text=text,shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text,shift_amount=shift)

