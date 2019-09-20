# Robot Excercise 3: Flag Capture Game using a Minimax Algorithm

## Instructions
In this assignment, you will combine your knowledge of informed search algorithms with the adversarial search game tree to teach the R2D2s how to play optimally in a flag capture game.

## Step 1: Create the Game Board
Similar to the A* game in last excercise, the game board also takes in the vertices and edges to define a graph. In addition to these two parameters, we also need to define the position of the robots and the flags.

```python
def __init__(self, V, E, initial_state, flag):
	'''
		self.vertices --  store the vertices of the graph
		self.edges   --  store the edges of the graph
		self.state     --  store the state of the gameboard
		self.flag    -- store the positions of the flags
		
		self.map   --  dictionary to represent the state of each grid, keys = vertices, value = vertex value in state
		self.robot_pos -- store the positions of the robots in a dictionary, keys = robot name, value = vertex
	'''
	pass
	
def neighbors(self, u):
	'''
		Return the neighbors of a vertex.
		If there is a robot occupying the neighboring vertex, 
		do not return that vertex as a neighbor.
	'''
	pass

def dist_between(self, u, v):
	'''
		Return the distance between two vertices.
	'''
	pass
```
Given the inputs as shown, you could expect the following outputs:

```python
>>> V = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
>>> E = [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((0, 1), (0, 2)), ((0, 1), (1, 1)), ((0, 1), (0, 0)), ((0, 2), (0, 3)), ((0, 2), (1, 2)), ((0, 2), (0, 1)), ((0, 3), (1, 3)), ((0, 3), (0, 2)), ((1, 0), (0, 0)), ((1, 0), (1, 1)), ((1, 0), (2, 0)), ((1, 1), (0, 1)), ((1, 1), (1, 2)), ((1, 1), (2, 1)), ((1, 1), (1, 0)), ((1, 2), (0, 2)), ((1, 2), (1, 3)), ((1, 2), (2, 2)), ((1, 2), (1, 1)), ((1, 3), (0, 3)), ((1, 3), (2, 3)), ((1, 3), (1, 2)), ((2, 0), (1, 0)), ((2, 0), (2, 1)), ((2, 0), (3, 0)), ((2, 1), (1, 1)), ((2, 1), (2, 2)), ((2, 1), (3, 1)), ((2, 1), (2, 0)), ((2, 2), (1, 2)), ((2, 2), (2, 3)), ((2, 2), (3, 2)), ((2, 2), (2, 1)), ((2, 3), (1, 3)), ((2, 3), (3, 3)), ((2, 3), (2, 2)), ((3, 0), (2, 0)), ((3, 0), (3, 1)), ((3, 1), (2, 1)), ((3, 1), (3, 2)), ((3, 1), (3, 0)), ((3, 2), (2, 2)), ((3, 2), (3, 3)), ((3, 2), (3, 1)), ((3, 3), (2, 3)), ((3, 3), (3, 2))]
>>> state = [['D2_1', 'x', 'x', 'x'], ['D2_2', 'x', 'x', 'x'], ['x', 'x', 'x', 'Q5_1'], ['x', 'x', 'x', 'Q5_2']]
>>> flag = {'flag_D2': (3, 2), 'flag_Q5': (0, 1)}
>>> graph = FlagCaptureGraph(V, E, state, flag)

>>> graph.state
[['D2_1', 'x', 'x', 'x'], ['D2_2', 'x', 'x', 'x'], ['x', 'x', 'x', 'Q5_1'], ['x', 'x', 'x', 'Q5_2']]

>>> graph.printstate()
* x x x 
* x x x 
x x x o 
x x x o 

>>> graph.map
{(0, 0): 'D2_1', (0, 1): 'x', (0, 2): 'x', (0, 3): 'x', (1, 0): 'D2_2', (1, 1): 'x', (1, 2): 'x', (1, 3): 'x', (2, 0): 'x', (2, 1): 'x', (2, 2): 'x', (2, 3): 'Q5_1', (3, 0): 'x', (3, 1): 'x', (3, 2): 'x', (3, 3): 'Q5_2'}

>>> graph.robot_pos
{'D2_1': (0, 0), 'D2_2': (1, 0), 'Q5_1': (2, 3), 'Q5_2': (3, 3)}

>>> graph.neighbors((0, 0))
[(0, 1)]

>>> graph.dist_between((0, 0), (0, 1))
1.0
```
## Step 2: Define the Game Rules
In this step, we will define the basic rules of the game, such as how to judge whether the game is over, how to update the game state, when to perform a move on the robot, etc. You will be updating the following functions:

```python	
def perform_move(self, current_state, move_state):
	'''
		Execute the movement of the robot and update the game accordingly, updating the state, map, and robot_pos parameters. 
		This function should also return the direction of the movement ("north", "south", "west", "east")
	'''
	pass

def successors(self, D2):
	pass

def copy(self):
	pass
	
def game_over(self):
	pass
```
```perform_move(self, current_state, move_state)``` execute the movement of the robot and update the game accordingly, updating the state, map, and robot_pos parameters. This function should also return the direction of the movement ("north", "south", "west", "east").

```python
>>> graph.printmap()
* x x x 
* x x x 
x x x o 
x x x o 
>>> graph.perform_move((0, 0), (0, 1))
'east'
>>> graph.printmap()
x * x x 
* x x x 
x x x o 
x x x o
>>> graph.map
[['x', 'D2_1', 'x', 'x'], ['D2_2', 'x', 'x', 'x'], ['x', 'x', 'x', 'Q5_1'], ['x', 'x', 'x', 'Q5_2']]
>>> graph.robot_pos
{'D2_1': (0, 1), 'D2_2': (1, 0), 'Q5_1': (2, 3), 'Q5_2': (3, 3)} 
>>> graph.state
{(0, 0): 'x', (0, 1): 'D2_1', (0, 2): 'x', (0, 3): 'x', (1, 0): 'D2_2', (1, 1): 'x', (1, 2): 'x', (1, 3): 'x', (2, 0): 'x', (2, 1): 'x', (2, 2): 'x', (2, 3): 'Q5_1', (3, 0): 'x', (3, 1): 'x', (3, 2): 'x', (3, 3): 'Q5_2'}
```

```successors(self, D2)``` generate the successors of a game state. The paramater D2 indicates whether it is the D2 team's turn. In each turn of a team, the robot 1 will move first and then the robot 2, meaning that if the first robot leaves a position, that position is open for the robot's teammate on its move. This function should yield a tuple where the first element is the movements of the two robots (a dictionary with keys of the robots and their next positions), as well as a copy of the new game map after these moves are performed.

```python
>>> for move, game in graph.successors(D2 = True):
...     print(move)
...     game.printmap()
... 
{'D2_1': (0, 1), 'D2_2': (0, 0)}
* * x x 
x x x x 
x x x o 
x x x o 
{'D2_1': (0, 1), 'D2_2': (1, 1)}
x * x x 
x * x x 
x x x o 
x x x o 
{'D2_1': (0, 1), 'D2_2': (2, 0)}
x * x x 
x x x x 
* x x o 
x x x o 
``` 
```python
>>> for move, game in graph.successors(D2 = False):
...     print(move)
...     game.printmap()
... 
{'Q5_1': (1, 3), 'Q5_2': (2, 3)}
* x x x 
* x x o 
x x x o 
x x x x 
{'Q5_1': (1, 3), 'Q5_2': (3, 2)}
* x x x 
* x x o 
x x x x 
x x o x 
{'Q5_1': (2, 2), 'Q5_2': (2, 3)}
* x x x 
* x x x 
x x o o 
x x x x 
{'Q5_1': (2, 2), 'Q5_2': (3, 2)}
* x x x 
* x x x 
x x o x 
x x o x
``` 
```copy(self)``` Return a new game object that is identical to the current, making a deep copy of the current state.

```python
>>> new_graph = graph.copy()
>>> print(new_graph.state == graph.state)
True
>>> new_graph.perform_move((0, 0), (0, 1))
'east'
>>> print(new_graph.state == graph.state)
False
```

```game_over(self)``` reflects a game is over or not, and the criteria is whether the robot gets to the position of their flags.

```python
>>> V = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
>>> E = [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((0, 1), (0, 2)), ((0, 1), (1, 1)), ((0, 1), (0, 0)), ((0, 2), (0, 3)), ((0, 2), (1, 2)), ((0, 2), (0, 1)), ((0, 3), (1, 3)), ((0, 3), (0, 2)), ((1, 0), (0, 0)), ((1, 0), (1, 1)), ((1, 0), (2, 0)), ((1, 1), (0, 1)), ((1, 1), (1, 2)), ((1, 1), (2, 1)), ((1, 1), (1, 0)), ((1, 2), (0, 2)), ((1, 2), (1, 3)), ((1, 2), (2, 2)), ((1, 2), (1, 1)), ((1, 3), (0, 3)), ((1, 3), (2, 3)), ((1, 3), (1, 2)), ((2, 0), (1, 0)), ((2, 0), (2, 1)), ((2, 0), (3, 0)), ((2, 1), (1, 1)), ((2, 1), (2, 2)), ((2, 1), (3, 1)), ((2, 1), (2, 0)), ((2, 2), (1, 2)), ((2, 2), (2, 3)), ((2, 2), (3, 2)), ((2, 2), (2, 1)), ((2, 3), (1, 3)), ((2, 3), (3, 3)), ((2, 3), (2, 2)), ((3, 0), (2, 0)), ((3, 0), (3, 1)), ((3, 1), (2, 1)), ((3, 1), (3, 2)), ((3, 1), (3, 0)), ((3, 2), (2, 2)), ((3, 2), (3, 3)), ((3, 2), (3, 1)), ((3, 3), (2, 3)), ((3, 3), (3, 2))]
>>> state = [['D2_1', 'x', 'x', 'x'], ['D2_2', 'x', 'x', 'x'], ['x', 'x', 'x', 'Q5_1'], ['x', 'x', 'x', 'Q5_2']]
>>> flag = {'flag_D2': (3, 2), 'flag_Q5': (0, 1)}
>>> graph = FlagCaptureGraph(V, E, state, flag)
>>> graph.gameover()
False
>>> state = [['D2_1', 'x', 'x', 'x'], ['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'Q5_1'], ['x', 'x', 'D2_2', 'Q5_2']]
>>> graph = FlagCaptureGraph(V, E, state, flag)
>>> graph.game_over()
True
```

## Step 3: Define the A* algorithm and the evaluate function
Implement the A star to calculate the shortest path between two vertics. This step is almost the same as the solution of excercise 2, but it should be noticed that, in the cases of the opponents occupy the flag, the path cannot lead to the goal(robots will be considered as obstacles). In this case, when the robot ends up next to the flag, return the current path as well as the path length plus one.

```python
def Astar(self, start, goal):
	'''
		return the path and length of the path
		in the form of (path, len(path))
	'''
	pass
```
Using the same parameters of graph as above, you could expect the following outputs (any path that is the shortest is alright)：

```python
>>> graph.Astar((0, 0), (2, 2))
([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], 5)
```

The ```evaluate(self, D2)``` estimates the utilities (scores) of current state which reflect the chance of winning the game. There are various methods to evaluate the utilities in this game, and different approaches will have different influences on the performance of the robots and the game results. Here is a recommended solution: using the difference of the minimum cost to reach the flag of each team as the utility. D2 is a boolean representing whether the utility is for the D2 team or not. If the D2 team is "winning", their utility should be higher.

```python
def evaluate(self, D2):
	pass
```

## Step 4: Implement Minimax algorithm with alpha-beta pruning
In this part, you will utilize your knowledge of alpha-beta minimax algorithm to help the R2D2s find out the optimal movements.

```python
def alpha_beta_max(self, D2, original_D2, limit, alpha, beta):
	pass

def alpha_beta_min(self, D2, original_D2, limit, alpha, beta):
	pass

def get_best_move(self, D2, limit):
	pass
```

After you finished the minimax algorithm, you could now play the game in a virtual environment.

```python
>>> from game_simulation import simulate_game
>>> record_game = simulate_game(graph, D2 = True, limit = 4)
Round: 1
D2 Turn
x * x x 
* x x x 
x x x o 
x x x o 
             
x * x x 
x x x x 
* x x o 
x x x o 
             
Q5 Turn
x * x x 
x x x o 
* x x x 
x x x o 
             
x * x x 
x x x o 
* x x x 
x x o x 

...

Q5 Turn
x o x x 
x x x * 
x * x x 
o x x x 
             
Q5 WIN
```

## Step 5: Let your Robots rolling in a real game
You will apply your algorithm in the real robots to visulize your program. The ```record_game``` store the movement of each robot and the data looks like:

```python
>>> record_game
[('D2_1', 'east'), ('D2_2', 'south'), ('Q5_1', 'north'), ('Q5_2', 'west'), ('D2_1', 'east'), ('D2_2', 'south'), ('Q5_1', 'west'), ('Q5_2', 'west'), ('D2_1', 'east'), ('D2_2', 'north'), ('Q5_1', 'north'), ('Q5_2', 'west'), ('D2_1', 'south'), ('D2_2', 'east'), ('Q5_1', 'west')]
```

You could implement a API to send commands to the robots to perform the movements. First, you need to connect to all of your robots using the following code.

```python
>>> from client import DroidClient
>>> from r2d2_action import action
###replace with your own tags###
>>> robot_tag = {'D2_1': 'D2-FE32', 'D2_2': 'D2-3493', 'Q5_1': 'Q5-D26A', 'Q5_2': 'Q5-B348'}
>>> droid1 = DroidClient()
>>> droid2 = DroidClient()
>>> droid3 = DroidClient()
>>> droid4 = DroidClient()
>>> Droids = {'D2_1': droid1, 'D2_2': droid2, 'Q5_1': droid3, 'Q5_2': droid4}
>>> for key in robot_tag:
...     Droids[key].connect_to_droid(robot_tag[key])
```

Then, you will write a function to convert the ```record_game``` to the rolling commands. ```r2d2_action(record_game, Droids, speed, time)``` takes in the movement of a game, all the droids, as well as the speed and time to control the distance of one movement.

When you finish all the tasks above, you could now let your robots play a real world game!

```python
###adjust the speed and time according to the grid size###
speed = 0.4
time = 1.5
action(record_game, Droids, speed, time)
```



