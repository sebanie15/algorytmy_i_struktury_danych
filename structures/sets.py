from abc import ABC, abstractmethod
from typing import Generic, Any, List

from structures.hashing import NaiveHash
from structures.lists import LinkedList


class Set(ABC):
	@abstractmethod
	def add(self, value: Any) -> None:
		pass

	@abstractmethod
	def __contains__(self, item: Any):
		pass

	@abstractmethod
	def clear(self):
		pass

	@abstractmethod
	def remove(self, value: Any) -> None:
		pass


class HashSet(Set):

	def __init__(self, hash_function: NaiveHash, initial_buckets_size: int = 4, payload_factor: float = 0.75,
	             increase_factor: int = 2):
		self.hash_function = hash_function
		self.initial_buckets_size = initial_buckets_size
		self.payload_factor = payload_factor
		self.increase_factor = increase_factor

		self.buckets = self._create_empty_buckets(initial_buckets_size)

		self.size = 0

	def __contains__(self, item: Any):

			hash_value = self.hash_function.hash(item)
			bucket_index = hash_value % len(self.buckets)

			return item in self.buckets[bucket_index]


	def clear(self):
		self.size = 0
		self._create_empty_buckets(self.initial_buckets_size)

	def remove(self, value: Any) -> None:
		pass

	def add(self, value: Any) -> None:

		if self.size / len(self.buckets) >= self.payload_factor:
			self._increase_bucket_count(self.increase_factor * len(self.buckets))

		hash_value = self.hash_function.hash(value)
		bucket_index = hash_value % len(self.buckets)
		self.buckets[bucket_index].append(value)
		self.size += 1

	def _create_empty_buckets(self, bucket_counts: int) -> List[LinkedList]:
		return [LinkedList() for _ in range(bucket_counts)]

	def _increase_bucket_count(self, target_bucket_count) -> None:
		new_buckets = self._create_empty_buckets(target_bucket_count)

		for bucket in self.buckets:
			for value in bucket:
				hash_value = self.hash_function.hash(value)
				bucket_index = hash_value % len(new_buckets)
				new_buckets[bucket_index].append(value)
		self.buckets = new_buckets

	def buckets_str(self) -> str:
		return '\n'.join([f'{i:3} -> {str(bucket)}' for i, bucket in enumerate(self.buckets)])
