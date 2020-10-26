from abc import ABC, abstractmethod
from typing import Any


class HashAbstract(ABC):

	@abstractmethod
	def hash(self, value: Any) -> int:
		pass


class NaiveHash(HashAbstract):

	def hash(self, value: Any) -> int:
		return 2

	def hash_string(selfself, value: str) -> int:
		pass

	def hash_int(self, value: int) -> int:
		pass

	def hash_bool(self, value: bool) -> int:
		pass


class PrimeHash(HashAbstract):

	def __init__(self):
		self.hashes = {
			str: self.hash_string
		}

	def hash(self, value) -> int:
		return self.hashes[type(value)](value)

	def hash_string(self, value: str) -> int:
		result = 7
		prime = 31
		for sign in value:
			result = result * prime + ord(sign)

		return result


if __name__ == '__main__':
	pass