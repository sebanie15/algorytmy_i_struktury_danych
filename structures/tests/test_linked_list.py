
from unittest import TestCase, main

from structures.lists import LinkedList


class TestLinkedList(TestCase):

	def test_init_without_elements(self):
		values = LinkedList[int]()

		self.assertIsNone(values.head)

	def test_lenght_empty_list(self):
		values = LinkedList[int]()

		self.assertEqual(values.length(), 0)
		self.assertEqual(0, len(values))

	def test_length_one_element_in_list(self):
		values = LinkedList[int]()
		values.head = LinkedList.Node[int](9)

		self.assertEqual(1, values.length())
		self.assertEqual(1, len(values))

	def test_length_many_elements_in_list(self):
		values = LinkedList[int]()
		values.head = LinkedList.Node[int](9, LinkedList.Node[int](5, LinkedList.Node[int](1)))

		self.assertEqual(3, values.length())

	def test_str_empty_list(self):
		values = LinkedList[int]()

		self.assertEqual(str(values), '[]')

	def test_str_many_elements_in_list(self):
		values = LinkedList[int]()
		values.head = LinkedList.Node[int](9, LinkedList.Node[int](5, LinkedList.Node[int](1)))

		self.assertEqual('[9, 5, 1]', str(values))

	def test_append_first_element_in_list(self):
		values = LinkedList[int]()
		values.append(9)

		self.assertEqual(1, len(values))
		self.assertEqual('[9]', str(values))

	def test_init_with_elements(self):
		values = LinkedList[int](9, 5, 1)

		self.assertEqual('[9, 5, 1]', str(values))

	def test_first_index_of_element(self):
		values = LinkedList[int](9, 5, 1)
		val = values[0]

		self.assertEqual(9, val)

	def test_last_index_of_element(self):
		values = LinkedList[int](9, 5, 1)
		val = values[2]

		self.assertEqual(1, val)

	def test_out_of_index_of_element(self):
		values = LinkedList[int](9, 5, 1)

		with self.assertRaises(IndexError):
			value = values[200]


if __name__ == '__main__':
	main()
