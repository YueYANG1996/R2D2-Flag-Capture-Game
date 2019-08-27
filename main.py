from FlagCapture import FlagCaptureGraph
V = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
E = [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((0, 1), (0, 2)), ((0, 1), (1, 1)), ((0, 1), (0, 0)), ((0, 2), (0, 3)), ((0, 2), (1, 2)), ((0, 2), (0, 1)), ((0, 3), (1, 3)), ((0, 3), (0, 2)), ((1, 0), (0, 0)), ((1, 0), (1, 1)), ((1, 0), (2, 0)), ((1, 1), (0, 1)), ((1, 1), (1, 2)), ((1, 1), (2, 1)), ((1, 1), (1, 0)), ((1, 2), (0, 2)), ((1, 2), (1, 3)), ((1, 2), (2, 2)), ((1, 2), (1, 1)), ((1, 3), (0, 3)), ((1, 3), (2, 3)), ((1, 3), (1, 2)), ((2, 0), (1, 0)), ((2, 0), (2, 1)), ((2, 0), (3, 0)), ((2, 1), (1, 1)), ((2, 1), (2, 2)), ((2, 1), (3, 1)), ((2, 1), (2, 0)), ((2, 2), (1, 2)), ((2, 2), (2, 3)), ((2, 2), (3, 2)), ((2, 2), (2, 1)), ((2, 3), (1, 3)), ((2, 3), (3, 3)), ((2, 3), (2, 2)), ((3, 0), (2, 0)), ((3, 0), (3, 1)), ((3, 1), (2, 1)), ((3, 1), (3, 2)), ((3, 1), (3, 0)), ((3, 2), (2, 2)), ((3, 2), (3, 3)), ((3, 2), (3, 1)), ((3, 3), (2, 3)), ((3, 3), (3, 2))]
state = [['D2_1', 'x', 'x', 'x'], ['D2_2', 'x', 'x', 'x'], ['x', 'x', 'x', 'Q5_1'], ['x', 'x', 'x', 'Q5_2']]
flag = {'flag_D2': (3, 2), 'flag_Q5': (0, 1)}
graph = FlagCaptureGraph(V, E, state, flag)

#Test Game
D2 = True
limit = 4
Round = 1
while graph.game_over() != True:
	print('Round: ' + str(Round))
	print('D2 Turn')
	D2_movement = graph.get_best_move(D2, limit)[0]
	graph.perform_move(graph.robot_pos['D2_1'], D2_movement['D2_1'])
	graph.printmap()
	print('             ')
	if graph.game_over():
		break
	graph.perform_move(graph.robot_pos['D2_2'], D2_movement['D2_2'])
	graph.printmap()
	print('             ')
	if graph.game_over():
		break
	print('Q5 Turn')
	Q5_movement = graph.get_best_move(False, limit)[0]
	graph.perform_move(graph.robot_pos['Q5_1'], Q5_movement['Q5_1'])
	graph.printmap()
	print('             ')
	if graph.game_over():
		break
	graph.perform_move(graph.robot_pos['Q5_2'], Q5_movement['Q5_2'])
	graph.printmap()
	print('             ')
	if graph.game_over():
		break
	Round += 1

graph.perform_move((0, 0), (0, 1))
for X, Y in graph.successors(True):
	print(X)
	Y.printmap()
for X, Y in graph.successors(False):
	print(X)
	print(Y.map)
graph.Astar(graph.robot_pos['Q5_1'], graph.flag['flag_Q5'])
graph.evaluate(True)

