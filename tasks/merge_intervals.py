from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
	"""the method allows to combine the intervals contained in the table
	Args:
		intervals: List[List[int]]
	Returns:
		List[List[int]]
	"""

	if len(intervals) < 2:
		return intervals
	else:
		intervals = sorted(intervals)

		result = [intervals[0]]
		for interval in intervals[1:]:
			if interval[0] <= result[-1][1]:
				result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
			else:
				result.append(interval)

	return result


if __name__ == '__main__':
	arr = [[2, 4], [8, 12], [5, 9]]

	print(merge_intervals(arr))

	arr = [[2, 3], [2, 4]]
	print(merge_intervals(arr))
