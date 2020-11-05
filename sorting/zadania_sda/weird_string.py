
def to_weird_case(string: str) -> str:
	result = [str.upper(string[i]) if i % 2 == 0 else str.lower(string[i]) for i in range(len(string))]
	return ''.join(result)


if __name__ == '__main__':
	print(to_weird_case('Algorytmy i struktury danych'))
