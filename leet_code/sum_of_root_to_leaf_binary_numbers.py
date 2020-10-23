# 1022

# Definition for a binary tree node.
from collections import deque


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:

	def sumRootToLeaf(self, root: TreeNode) -> int:
		result = 0
		nodes = [(root, 0)]

		while nodes:
			node, current_number = nodes.pop()
			if node:
				current_number = (current_number << 1) | node.val

				if not node.left and not node.right:
					result += current_number
				else:
					nodes.append((node.left, current_number))
					nodes.append((node.right, current_number))

		return result


if __name__ == '__main__':
	obj1 = Solution()

	t1 = TreeNode(
		1,
		left=TreeNode(
			0, TreeNode(0), TreeNode(1)
		),
		right=TreeNode(
			1, TreeNode(0), TreeNode(1)
		)
	)

	print(obj1.sumRootToLeaf(t1))

	print('-' * 40)

	current_number = 0
	current_number = (current_number << 1) | 1
	print(current_number)

	current_number = (current_number << 1) | 0
	print(current_number)

	current_number = (current_number << 1) | 1
	print(current_number)
