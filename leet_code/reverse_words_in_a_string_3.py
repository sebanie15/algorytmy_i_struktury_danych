
# 557

class Solution:

	def reverseWords(self, s: str) -> str:
		words = s.split(' ')
		result = ''
		for idx, word in enumerate(words):
			result += word[::-1]
			if idx < len(words)-1:
				result += ' '

		return result

	def reverseWords2(selfself, s: str) -> str:
		return ' '.join([word[::-1] for word in s.split(' ')])


if __name__ == '__main__':
	obj1 = Solution()

	sentence = "Let's take LeetCode contest"
	print(obj1.reverseWords(sentence))
	print(obj1.reverseWords2(sentence))
