
# 1475
from typing import List


class Solution:

	def finalPrices(self, prices: List[int]) -> List[int]:
		result = []
		idx = 0
		if 1 <= len(prices) <= 500 and 1 <= max(prices) <= 1000:
			while idx < len(prices):
				temp = 0
				for n in prices[idx+1:]:
					if prices[idx] >= n:
						temp = n
						break

				result.append(prices[idx] - temp)

				idx += 1

		return result


if __name__ == '__main__':
	obj1 = Solution()
	prices_1 = [8, 4, 6, 2, 3]
	print(obj1.finalPrices(prices_1))

	prices_1 = [1,2,3,4,5]
	print(obj1.finalPrices(prices_1))

	prices_1 = [10,1,1,6]
	print(obj1.finalPrices(prices_1))
