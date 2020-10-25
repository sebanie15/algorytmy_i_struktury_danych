import json
from typing import List
import os

import plotly.graph_objects as go

from sorting.research import ORDERED, RANDOM, REVERSED, BASE


def show_algorithm_complexities(filename):
	with open(filename) as f:
		result = json.load(f)

	domain = list(result[ORDERED].keys())
	figure = go.Figure()
	figure.add_trace(go.Scatter(x=domain, y=list(result[ORDERED].values()), mode='lines+markers', name=ORDERED))
	figure.add_trace(go.Scatter(x=domain, y=list(result[REVERSED].values()), mode='lines+markers', name=REVERSED))
	figure.add_trace(go.Scatter(x=domain, y=list(result[RANDOM].values()), mode='lines+markers', name=RANDOM))

	figure.show()


def show_algorithm_complexities_2(files: List, generate_types: List[str]) -> None:
	"""
	The method allows you to display data from a list of files according to a specific type of list generation

	Args:
		files: list of filenames 
		generate_type: str - 'ordered', 'reversed', 'random' or const args from research: ORDERED, RANDOM, REVERSED
	Returns:
		None
	"""

	figure = go.Figure()
	is_error = False

	if files:
		for file in files:
			try:
				with open(file, 'r') as f:
					result = json.load(f)
			except FileNotFoundError as error:
				is_error = True
				print(f'{error}')
			else:
				for generate_type in generate_types:
					domain = list(result[generate_type].keys())
					figure.add_trace(go.Scatter(
						x=domain, y=list(result[generate_type].values()), mode='lines+markers',
						name=f'{file}_{generate_type}'
					))
	else:
		is_error = True
		print('Empty list of files')

	if not is_error:
		figure.show()


def make_list_of_files(path: str) -> List:
	result = []
	for root, dirs, files in os.walk(path, topdown=True):
		for name in files:
			result.append(os.path.join(root, name))
	return result


def show_complexities(filenames, order_type):
	figure = go.Figure()
	for filename in filenames:
		with open(filename) as f:
			result = json.load(f)

		domain = result[ORDERED].keys()
		figure.add_trace(go.Scatter(x=list(domain), y=list(result[order_type].values()), mode='lines+markers',
		                            name=f"{filename.split('_')[0]}_{order_type}"))

	figure.show()


def show_complexities_types(filenames, types):
	figure = go.Figure()
	for filename in filenames:
		for order_type in types:
			with open(filename) as f:
				result = json.load(f)

			domain = result[ORDERED].keys()
			figure.add_trace(go.Scatter(x=list(domain), y=list(result[order_type].values()), mode='lines+markers',
			                            name=f"{filename.split('_')[0]}_{order_type}"))


if __name__ == '__main__':
	# show_algorithm_complexities('BubbleSort_100.json')

	# list_of_files = make_list_of_files(str(BASE))
	# list_of_files = [BASE / 'QuickSort_10.json', BASE / 'QuickSOrt_10old.json']

	# show_complexities_types(list_of_files, [ORDERED, REVERSED, RANDOM])

	list_of_files = [
		'./temp_data/BubbleSort_5000.json',
		'./temp_data/InsertSort_5000.json',
		'./temp_data/QuickSort_5000.json'
	]

	print(list_of_files)
	show_algorithm_complexities_2(list_of_files, [ORDERED, REVERSED, RANDOM])
