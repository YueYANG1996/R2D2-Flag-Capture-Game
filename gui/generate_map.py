import math
import random

def generate_map(row, column, barriers):
	vertics = [(i, j) for i in range(row) for j in range(column)]
	edges = []
	for vertic in vertics:
		for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			next_vertic = (vertic[0] + move[0], vertic[1] + move[1])
			if next_vertic in vertics:
				edges.append((vertic, next_vertic))
	for barrier in barriers:
		edges.remove(barrier)
		edges.remove((barrier[1], barrier[0]))
	return vertics, edges

def generate_random(row, column):
	vertics = [(i, j) for i in range(row) for j in range(column)]
	edges = []
	for vertic in vertics:
		for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			next_vertic = (vertic[0] + move[0], vertic[1] + move[1])
			if next_vertic in vertics:
				edges.append((vertic, next_vertic))

	# num_of_barriers = random.randint(0, row * column)
	num_of_barriers = round(row * 2 *column/3)
	barriers = random.sample(edges, num_of_barriers)
	for barrier in barriers:
		if barrier in edges:
			edges.remove(barrier)
		if random.random() > 0.15:

			if (barrier[1], barrier[0]) in edges:
				edges.remove((barrier[1], barrier[0]))

	return vertics, edges

def printmap(G):
	rows = G.vertics[-1][0] + 1
	cols = G.vertics[-1][1] + 1
	for i in range(2 * rows - 1):
		print_row = ''
		if i % 2 == 0:
			for j in range(cols):
				current_node = (int(i / 2), j)
				right_node = (int(i / 2), j + 1)
				pattern = '☐'
				if (current_node, right_node) in G.edges and (right_node, current_node) in G.edges:
					print_row += pattern + ' ' + '  '
				else:
					if right_node in G.vertics:
						print_row += pattern + ' ' + '| '
					else:
						print_row += pattern + ' ' + '  '
		else:
			for j in range(cols):
				current_node = (math.ceil(i/2), j)
				up_node = (math.ceil(i/2) - 1, j)
				if j == 0:
					if (current_node, up_node) in G.edges and (up_node, current_node) in G.edges: 
						print_row += '  ' + ' '
					else:
						print_row += '-- '
				else: 
					if (current_node, up_node) in G.edges and (up_node, current_node) in G.edges:
						print_row += '  ' + '  '
					else:
						print_row += '--- '
		print(print_row)

def printpath(G, start, goal, path):
	rows = G.vertics[-1][0] + 1
	cols = G.vertics[-1][1] + 1
	for i in range(2 * rows - 1):
		print_row = ''
		if i % 2 == 0:
			for j in range(cols):
				current_node = (int(i / 2), j)
				right_node = (int(i / 2), j + 1)
				if current_node == goal:
					pattern = '☒'
				elif current_node in path:
					pattern = '☑'
				else:
					pattern = '☐'
				if (current_node, right_node) in G.edges and (right_node, current_node) in G.edges:
					print_row += pattern + ' ' + '  '
				else:
					if right_node in G.vertics:
						print_row += pattern + ' ' + '| '
					else:
						print_row += pattern + ' ' + '  '
		else:
			for j in range(cols):
				current_node = (math.ceil(i/2), j)
				up_node = (math.ceil(i/2) - 1, j)
				if j == 0:
					if (current_node, up_node) in G.edges and (up_node, current_node) in G.edges: 
						print_row += '  ' + ' '
					else:
						print_row += '-- '
				else: 
					if (current_node, up_node) in G.edges and (up_node, current_node) in G.edges:
						print_row += '  ' + '  '
					else:
						print_row += '--- '
		print(print_row)

def printtsp(G, start, goals, path):
	rows = G.vertics[-1][0] + 1
	cols = G.vertics[-1][1] + 1
	for i in range(2 * rows - 1):
		print_row = ''
		if i % 2 == 0:
			for j in range(cols):
				current_node = (int(i / 2), j)
				right_node = (int(i / 2), j + 1)
				if current_node in goals:
					pattern = '☒'
				elif current_node in path:
					pattern = '☑'
				else:
					pattern = '☐'
				if (current_node, right_node) in G.edges and (right_node, current_node) in G.edges:
					print_row += pattern + ' ' + '  '
				else:
					if right_node in G.vertics:
						print_row += pattern + ' ' + '| '
					else:
						print_row += pattern + ' ' + '  '
		else:
			for j in range(cols):
				current_node = (math.ceil(i/2), j)
				up_node = (math.ceil(i/2) - 1, j)
				if j == 0:
					if (current_node, up_node) in G.edges and (up_node, current_node) in G.edges: 
						print_row += '  ' + ' '
					else:
						print_row += '-- '
				else: 
					if (current_node, up_node) in G.edges and (up_node, current_node) in G.edges:
						print_row += '  ' + '  '
					else:
						print_row += '--- '
		print(print_row)


