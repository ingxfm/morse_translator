MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '       ',}

word = input('Please enter a word: ')


def morse_translator(word):
    word_in_morse_list = []
    for letter in word:
        if letter.upper() in MORSE_CODE_DICT:
            word_in_morse_list.append(MORSE_CODE_DICT[letter.upper()])
            word_in_morse_str = ' '.join(word_in_morse_list)
        else:
            print('Please, do not enter special characters.')
            morse_translator()
    if word_in_morse_str:
        print(word_in_morse_str)


morse_translator(word=word)
