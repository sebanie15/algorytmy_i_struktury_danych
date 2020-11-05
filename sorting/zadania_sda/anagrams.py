from typing import List


def anagrams(word: str, lst_of_words: List[str]) -> List[str]:
	def is_anagram(word1: str, word2: str) -> bool:
		char_set = set(word1)
		for char in char_set:
			if word1.count(char) != word2.count(char):
				return False
		return True

	return [word_ for word_ in lst_of_words if is_anagram(word, word_)]

# answer from sda
from collections import Counter


def anagrams2(word: str, lst_of_words: List[str]) -> List[str]:
	counts = Counter(word)
	return [w for w in lst_of_words if Counter(w) == counts]


if __name__ == '__main__':
	lst_of_words = ['tama', 'kat', 'tap', 'meta', 'mata', 'abba', 'bbaa']

	print(anagrams('tak', lst_of_words))
