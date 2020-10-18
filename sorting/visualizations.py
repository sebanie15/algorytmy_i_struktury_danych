
import json
from typing import List

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


def show_algorithm_complexities_2(files: List, generate_type: str) -> None:
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

	for file in files:
		try:
			with open(file, 'r') as f:
				result = json.load(f)
		except FileNotFoundError as error:
			is_error = True
			print(f'{error}')
		else:
			domain = list(result[generate_type].keys())
			figure.add_trace(go.Scatter(x=domain, y=list(result[generate_type].values()), mode='lines+markers', name=file))

	if not is_error:
		figure.show()


if __name__ == '__main__':
	# show_algorithm_complexities('BubbleSort_100.json')

	show_algorithm_complexities_2([str(BASE) + '/BubbleSort_100.json', str(BASE) + '/InsertSort_100.json'], REVERSED)
