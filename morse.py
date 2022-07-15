# Dictionary mapping letters to morse code equivalent
ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Get user input
string_to_translate = input("Type something to be translated to morse code: ")

# Empty list to store morse code for each character
morse_code = []
for char in string_to_translate:
    # If char is the space character, just add that directly to the list
    if char.isspace():
        morse_code.append(' ')
    # Search dictionary for key matching char, get the morse code, and add it to the list
    else:
        morse_char = ENGLISH_TO_MORSE.get(char.upper())
        morse_code.append(morse_char)

# Join all elements of the list to create a final string
translated_string = ''.join(char for char in morse_code)
print(translated_string)
