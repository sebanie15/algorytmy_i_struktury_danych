
from unittest import TestCase, main

from structures.queues import Stack

class TestStack(TestCase):

	def test_push(self):
		pass

	def test_push_init_elements(self):
		values = Stack[int]()

		# values.push(2)

		# self.assertEqual(Stack[int](2), 2)

	def test_front(self):
		values = Stack[int]()

		with self.assertRaises(Stack.EmptyStackError):
			values.push(2)

	def test_pop_stack_with_elements(self):
		pass

	def test_pop_empty_stack(self):
		pass


if __name__ == '__main__':
	main()