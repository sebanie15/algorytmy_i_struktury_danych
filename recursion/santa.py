from typing import List


def delivery_presents_iteratively(houses: List[str]) -> None:

	for house in houses:
		print(f'Delivering presents to {house}')

def delivery_presents_recursively(houses: List[str]) -> None:
	if not houses:
		return None

	if len(houses) == 1:
		print(f'Delivering presents to {houses[0]}')
	else:
		mid = len(houses) // 2
		delivery_presents_recursively(houses[:mid])
		delivery_presents_recursively(houses[mid:])


if __name__ == '__main__':
	houses = ["Piotr's House", "Ola's House", "John's House", "Ada's House", ]
	delivery_presents_iteratively(houses)

	print('-'*40)

	delivery_presents_recursively([])
