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
record_game = []

while graph.game_over() != True:
	print('Round: ' + str(Round))
	print('D2 Turn')
	D2_movement = graph.get_best_move(D2, limit)[0]
	move_robot = D2_movement[0]
	print(move_robot)
	move_direction = graph.perform_move(graph.robot_pos[move_robot], D2_movement[1])
	record_game.append((move_robot, move_direction))
	graph.printmap()
	print('             ')
	if graph.game_over():
		print('D2 WIN')
		break

	print('Q5 Turn')
	Q5_movement = graph.get_best_move(False, limit)[0]
	move_robot = Q5_movement[0]
	move_direction = graph.perform_move(graph.robot_pos[move_robot], Q5_movement[1])
	record_game.append((move_robot, move_direction))
	graph.printmap()
	print('             ')
	if graph.game_over():
		print('Q5 WIN')
		break
	Round += 1
	if Round > 40:
		break
'''
while graph.game_over() != True:
	print('Round: ' + str(Round))
	print('Q5 Turn')
	Q5_movement = graph.get_best_move(False, limit)[0]
	move_direction = graph.perform_move(graph.robot_pos['Q5_1'], Q5_movement['Q5_1'])
	record_game.append(('Q5_1', move_direction))
	graph.printmap()
	print('             ')
	if graph.game_over():
		break
	move_direction = graph.perform_move(graph.robot_pos['Q5_2'], Q5_movement['Q5_2'])
	record_game.append(('Q5_2', move_direction))
	graph.printmap()
	print('             ')
	if graph.game_over():
		break
	print('D2 Turn')
	D2_movement = graph.get_best_move(True, limit)[0]
	move_direction = graph.perform_move(graph.robot_pos['D2_1'], D2_movement['D2_1'])
	record_game.append(('D2_1', move_direction))
	graph.printmap()
	print('             ')
	if graph.game_over():
		break
	move_direction = graph.perform_move(graph.robot_pos['D2_2'], D2_movement['D2_2'])
	record_game.append(('D2_2', move_direction))
	graph.printmap()
	print('             ')
	if graph.game_over():
		break
	Round += 1

from client import DroidClient
from r2d2_action import action
robot_tag = {'D2_1': 'D2-D74E', 'D2_2': 'D2-3493', 'Q5_1': 'Q5-D26A', 'Q5_2': 'Q5-B348'}
droid1 = DroidClient()
droid2 = DroidClient()
droid3 = DroidClient()
droid4 = DroidClient()
Droids = {'D2_1': droid1, 'D2_2': droid2, 'Q5_1': droid3, 'Q5_2': droid4}
for key in robot_tag:
	Droids[key].connect_to_droid(robot_tag[key])

for key in Droids:
	Droids[key].disconnect()
action(record_game, Droids, speed, time)'''



