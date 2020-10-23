
# 589

from typing import List


class Node:
	def __init__(self, val=None, children=None):
		self.val = val
		self.children = children


class Solution:

	def preorder(self, root: Node) -> List[int]:
		result = []
		temp = [root]

		while temp:
			node  = temp.pop()
			if node:
				result.append(node.val)
			if node and node.children:
				for child in node.children[::-1]:
					temp.append(child)

		return result


if __name__ == '__main__':
	obj1 = Solution()
	t1 = Node(
		1,
		[
			Node(3, [Node(5), Node(6)]),
			Node(2, [None]),
			Node(4),
			Node(None)
		]
	)
	root = [1, None, 3, 2, 4, None, 5, 6]

	print(obj1.preorder(t1))

