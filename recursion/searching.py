from typing import List


def search(values: List[int], target: int) -> int:
	idx = 0
	while idx < len(values):
		if values[idx] == target:
			return idx
		idx += 1
	return -1

def binary_search(values: List[int], target: int) -> int:
	def binary_search_help(values: List[int], target: int, left: int, right: int) -> int:
		if right >= left:
			mid = (left+right) // 2
			if target == values[mid]:
				return mid
			elif target < values[mid]:
				return binary_search_help(values, target=target, left=left, right=mid-1)
			elif target > values[mid]:
				return binary_search_help(values, target=target, left=mid+1, right=right)
		else:
			return -1

	left = 0
	right = len(values)-1

	return binary_search_help(values, target=target, left=left, right=right)



if __name__ == '__main__':

	length = 1000
	values = list(range(1, length +1))

	print(search(values, target=500))