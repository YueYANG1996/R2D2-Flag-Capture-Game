from FlagCapture import FlagCaptureGraph, printmap

def simulate_game(graph, D2, limit):
	Round = 1
	record_game = []
	if D2 == True:
		while graph.game_over() != True:
			print('Round: ' + str(Round))

			print('D2 Turn')
			D2_movement = graph.get_best_move(True, limit)[0]
			D2_1_move_direction = D2_movement['D2_1']
			graph.perform_move('D2_1', D2_1_move_direction)
			record_game.append(('D2_1', D2_1_move_direction))
			printmap(graph)
			print('--------------')
			if graph.game_over():
				print('D2 WIN')
				break

			D2_2_move_direction = D2_movement['D2_2']
			graph.perform_move('D2_2', D2_2_move_direction)
			record_game.append(('D2_2', D2_2_move_direction))
			printmap(graph)
			print('--------------')
			if graph.game_over():
				print('D2 WIN')
				break

			print('Q5 Turn')
			Q5_movement = graph.get_best_move(False, limit)[0]
			Q5_1_move_direction = Q5_movement['Q5_1']
			graph.perform_move('Q5_1', Q5_1_move_direction)
			record_game.append(('Q5_1', Q5_1_move_direction))
			printmap(graph)
			print('--------------')
			if graph.game_over():
				print('Q5 WIN')
				break

			Q5_2_move_direction = Q5_movement['Q5_2']
			graph.perform_move('Q5_2', Q5_2_move_direction)
			record_game.append(('Q5_2', Q5_2_move_direction))
			printmap(graph)
			print('--------------')
			if graph.game_over():
				print('Q5 WIN')
				break

			Round += 1
			if Round > 20:
				break
	else:
		while graph.game_over() != True:
			print('Round: ' + str(Round))

			print('Q5 Turn')
			Q5_movement = graph.get_best_move(False, limit)[0]
			move_direction = graph.perform_move(graph.robots_pos['Q5_1'], Q5_movement['Q5_1'])
			record_game.append(('Q5_1', move_direction))
			graph.printmap()
			print('             ')
			if graph.game_over():
				print('Q5 WIN')
				break

			move_direction = graph.perform_move(graph.robots_pos['Q5_2'], Q5_movement['Q5_2'])
			record_game.append(('Q5_2', move_direction))
			graph.printmap()
			print('             ')
			if graph.game_over():
				print('Q5 WIN')
				break

			print('D2 Turn')
			D2_movement = graph.get_best_move(True, limit)[0]
			move_direction = graph.perform_move(graph.robots_pos['D2_1'], D2_movement['D2_1'])
			record_game.append(('D2_1', move_direction))
			graph.printmap()
			print('             ')
			if graph.game_over():
				print('D2 WIN')
				break

			move_direction = graph.perform_move(graph.robots_pos['D2_2'], D2_movement['D2_2'])
			record_game.append(('D2_2', move_direction))
			graph.printmap()
			print('             ')
			if graph.game_over():
				print('D2 WIN')
				break

			Round += 1
			if Round > 20:
				break
	return record_game