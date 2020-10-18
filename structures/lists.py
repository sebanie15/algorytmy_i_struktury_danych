from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Optional

from structures.own_types import T


class List(ABC, Generic[T]):

	@abstractmethod
	def append(self, element: T) -> None:
		pass

	@abstractmethod
	def __getitem__(self, item):
		pass

	@abstractmethod
	def __setitem__(self, key: int, value: T) -> None:
		pass

	@abstractmethod
	def __eq__(self, other: LinkedList) -> bool:
		pass

	@abstractmethod
	def length(self):
		pass

	@abstractmethod
	def __str__(self) -> str:
		pass

	def __len__(self):
		return self.length()


class LinkedList(List[T]):
	@dataclass
	class Node(Generic[T]):
		value: T
		next: Optional[LinkedList.Node] = None

	def __init__(self, *args: T) -> None:
		self.head = None
		self._append_init_elements(args)

	def _append_init_elements(self, args):
		if args:
			for arg in args:
				self.append(arg)

	def append(self, element: T) -> None:
		node = LinkedList.Node[int](element)

		if self.head is None:
			self.head = node
		else:
			pointer = self.head
			while pointer.next is not None:
				pointer = pointer.next

			pointer.next = node

	def __getitem__(self, item: int) -> T:
		pointer = self.head
		pointer_index = 0

		while pointer is not None and pointer_index < item:

			pointer = pointer.next
			pointer_index += 1

		if pointer is not None:
			return pointer.value
		else:
			raise IndexError('Index out of range')

	def __setitem__(self, key: int, value: T) -> None:
		pointer = self.head
		pointer_index = 0

		while pointer and pointer_index < key:
			pointer = pointer.next
			pointer_index += 1

		if pointer:
			pointer.value = value
		else:
			raise IndexError('Index out of range')

	def __eq__(self, other: LinkedList) -> bool:
		self_pointer = self.head
		other_pointer = other.head

		if len(self) == len(other):
			while self_pointer:
				if self_pointer != other_pointer:
					return False
				self_pointer = self_pointer.next
				other_pointer = other_pointer.next
			return True
		return False


	def __str__(self) -> str:
		result = ''
		pointer = self.head

		while pointer is not None:

			result += str(pointer.value)
			pointer = pointer.next

			if pointer is not None:
				result += ', '

		return  str(f'[{result}]')

	def length(self) -> int:
		result = 0
		pointer = self.head

		while pointer is not None:
			result += 1
			pointer = pointer.next

		return result
