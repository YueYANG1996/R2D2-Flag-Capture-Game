# Robot Excercise 3: Flag Capture Game with Minimax Algorithm

## Instructions
In this assignment, you will combine your knowledge of informed search algorithms with the adversarial search game tree to teach the R2D2s how to play optimally in a flag capture game.

## Step 1: Create the Game Board
Similar to the A* game in the last excercise, the game board also takes in the vertices and edges to define a graph. In addition to these two parameters, we also need to define the position of the robots and the flags.

```python
def __init__(self, V, E, initial_state, flag):
	'''
		self.vertics --  store the vertics of the graph
		self.edges   --  store the edges of the graph
		self.map     --  store the state of the gameboard
		self.state   --  dictionary to represent the state of each grid
		self.robot_pos -- store the positions of the robots
		self.flag    -- store the positions of the flags
	'''
	pass
	
def neighbors(self, u):
	'''
		return the neighbors of a grid, 
		if there is a robot occupies the neighboring grid, 
		it will not be take as a neighbor.
	'''
	pass

def dist_between(self, u, v):
	'''
		return the distance between two vertics
	'''
	pass
```
You should expect the following outputs:

```python
>>> V = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
>>> E = [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((0, 1), (0, 2)), ((0, 1), (1, 1)), ((0, 1), (0, 0)), ((0, 2), (0, 3)), ((0, 2), (1, 2)), ((0, 2), (0, 1)), ((0, 3), (1, 3)), ((0, 3), (0, 2)), ((1, 0), (0, 0)), ((1, 0), (1, 1)), ((1, 0), (2, 0)), ((1, 1), (0, 1)), ((1, 1), (1, 2)), ((1, 1), (2, 1)), ((1, 1), (1, 0)), ((1, 2), (0, 2)), ((1, 2), (1, 3)), ((1, 2), (2, 2)), ((1, 2), (1, 1)), ((1, 3), (0, 3)), ((1, 3), (2, 3)), ((1, 3), (1, 2)), ((2, 0), (1, 0)), ((2, 0), (2, 1)), ((2, 0), (3, 0)), ((2, 1), (1, 1)), ((2, 1), (2, 2)), ((2, 1), (3, 1)), ((2, 1), (2, 0)), ((2, 2), (1, 2)), ((2, 2), (2, 3)), ((2, 2), (3, 2)), ((2, 2), (2, 1)), ((2, 3), (1, 3)), ((2, 3), (3, 3)), ((2, 3), (2, 2)), ((3, 0), (2, 0)), ((3, 0), (3, 1)), ((3, 1), (2, 1)), ((3, 1), (3, 2)), ((3, 1), (3, 0)), ((3, 2), (2, 2)), ((3, 2), (3, 3)), ((3, 2), (3, 1)), ((3, 3), (2, 3)), ((3, 3), (3, 2))]
>>> state = [['D2_1', 'x', 'x', 'x'], ['D2_2', 'x', 'x', 'x'], ['x', 'x', 'x', 'Q5_1'], ['x', 'x', 'x', 'Q5_2']]
>>> flag = {'flag_D2': (3, 2), 'flag_Q5': (0, 1)}
>>> graph = FlagCaptureGraph(V, E, state, flag)

>>> graph.map
[['D2_1', 'x', 'x', 'x'], ['D2_2', 'x', 'x', 'x'], ['x', 'x', 'x', 'Q5_1'], ['x', 'x', 'x', 'Q5_2']]

>>> graph.printmap()
* x x x 
* x x x 
x x x o 
x x x o 

>>> graph.state
{(0, 0): 'D2_1', (0, 1): 'x', (0, 2): 'x', (0, 3): 'x', (1, 0): 'D2_2', (1, 1): 'x', (1, 2): 'x', (1, 3): 'x', (2, 0): 'x', (2, 1): 'x', (2, 2): 'x', (2, 3): 'Q5_1', (3, 0): 'x', (3, 1): 'x', (3, 2): 'x', (3, 3): 'Q5_2'}

>>> graph.robot_pos
{'D2_1': (0, 0), 'D2_2': (1, 0), 'Q5_1': (2, 3), 'Q5_2': (3, 3)}

>>> graph.neighbors((0, 0))
[(0, 1)]

>>> graph.dist_between((0, 0), (0, 1))
1.0
```
## Step 2: Define the Game Rules
In this step, we will define the basic rules of the game, such as how to judge whether the game is over, how to update the game state when perform a move on the robot, etc.

<<<<<<< HEAD
```python
def copy(self):
	'''
		
	'''
	pass
	
def game_over(self):
	pass
	
def successors(self, D2):
	pass

def perform_move(self, current_state, move_state):
	pass
```

## Step 3: Define the A* algorithm and the evaluate function
Implement the A star to calculate the shortest path between two vertics. This step is almost the same as the solution of excercise 2, but it should be noticed that, in the cases of the opponents occupy the flag, the path cannot lead to the goal(robots will be considered as obstacles), thus the total length of the path should be modified.
=======
## Step 2: Define the A* algorithm and evaluate function
Implement the A star to calculate the shortest path between two vertices. This step is almost the same as the solution of excercise 2, but it should be noticed that, in the cases where the opponents are occupying the flag, the path cannot lead to the goal(robots will be considered as obstacles), and thus the total length of the path should be modified.
>>>>>>> 4cbe65e1fb45b2c762858dc8fe7370ea37a2d347

```python
def Astar(self, start, goal):
	'''
		return the path and length of the path
		in the form of (path, len(path))
	'''
	pass
```
You should expect the following outputs：

```python
>>> graph.Astar((0, 0), (2, 2))
([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], 5)
```

<<<<<<< HEAD
The evaluate function estimate the utilities (scores) of current state which reflect the chance of wining the game. There are various methods to evaluate the utilities in this game, and different approaches will have influence on the performance of the robot and game results. Here is a recommended solution: using the difference of the minimum cost to reach the flag of seach team as the utility.

```python
def evaluate(self, D2):
	pass
```





=======
The evaluate function estimates the utilities (scores) of the current state which reflect the chance of winning the game. There are various methods to evaluate the utilities in this game, and different approaches will influence the performance of the robot and game results. Here is a recommended solution: using the difference of the minimum cost to reach the flag of the search team as the utility, which is:
$U(D2) = min(Astar_cost(D2_1, flag_D2), Astar_cost(D2_2, flag_D2)) - min(Astar_cost(D2_1, flag_D2), Astar_cost(D2_2, flag_D2))$
>>>>>>> 4cbe65e1fb45b2c762858dc8fe7370ea37a2d347
