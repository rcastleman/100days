from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol_list = []
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    notepad = ""
    #guardrails in case user enters shift > 26: 
    shift_amount = shift_amount % 26
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == 'encode':
                new_position = position + shift_amount
            elif cipher_direction == 'decode':
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            notepad += new_letter
        else:
            notepad += char
    print(f"The result is '{notepad}'.")

should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if restart == "no":
    should_end = True
    print("Goodbye")