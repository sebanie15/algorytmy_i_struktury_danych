
# 1518

class Solution:
	def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

		result = numBottles
		full_bottles = numBottles
		empty_bottles = full_bottles

		while full_bottles:
			print(full_bottles, empty_bottles, result)
			full_bottles = empty_bottles // numExchange
			empty_bottles -= (full_bottles * numExchange) - full_bottles
			result += full_bottles

		return result

if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.numWaterBottles(9, 3))
	print(obj1.numWaterBottles(15, 8))
	print(obj1.numWaterBottles(5, 5))
	print(obj1.numWaterBottles(2, 3))