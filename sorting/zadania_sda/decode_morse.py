MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def decode_morse(morse_code: str) -> str:
	result = ''

	for word in morse_code.strip().split('   '):
		chars = word.strip().split(' ')
		for char in chars:
			if char in MORSE_CODE:
				result += MORSE_CODE[char]
			else:
				raise ValueError('Undefined character in the message!')
		result += ' '
	return result


# answer from sda
def decode_morse2(morse_sequence: str) -> str:
	words = []
	for morse_word in morse_sequence.split('   '):
		word = ''.join(MORSE_CODE.get(morse_char, '') for morse_char in morse_word.split(' '))
		if word:
			words.append(word)
	return ' '.join(words)


if __name__ == '__main__':
	print(decode_morse('.... . -.--   .--- ..- -.. .'))
	print(decode_morse(' . '))
	print(decode_morse('...   ---   ...'))
