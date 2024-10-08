logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    """
    Encodes or decodes a given message using the Caesar cipher.
    
    Parameters
    ----------
    start_text : str
        The input text to encode or decode.
    shift_amount : int
        The number of positions to shift the letters in the alphabet.
    cipher_direction : str
        Either 'encode' or 'decode', indicating whether to shift forwards or backwards.
    """
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # If the character is a letter, shift it; otherwise, keep it unchanged
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Print the logo at the start of the program
print(logo)

# Keep the program running until the user decides to stop
def run_caesar_cipher():
    should_end = False
    while not should_end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # Use modulus to handle shifts larger than 26
        shift = shift % 26

        # Call the caesar function with the provided inputs
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        # Ask if the user wants to restart the program
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart == "no":
            should_end = True
            print("Goodbye")

# Start the Caesar cipher program
run_caesar_cipher()
