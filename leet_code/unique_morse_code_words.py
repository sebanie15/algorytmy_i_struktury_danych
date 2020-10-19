
# 804

from typing import List

morse_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.",
                  "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

CHAR_SHIFT = 97

class Solution:

	def uniqueMorseRepresentations(self, words: List[str]) -> int:
		result = []

		for word in words:
			morse_word = ''
			for char in word:
				morse_word += morse_alphabet[ord(char) - CHAR_SHIFT]
			result.append(morse_word)
		print(result)
		return len(set(result))


if __name__ == '__main__':
	print(ord('a'), ord('z'))
	obj1 = Solution()
	print(obj1.uniqueMorseRepresentations(['gin', 'zen', 'gig', 'msg']))
