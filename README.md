# Robot Excercise 3: Flag Capture Game with Minimax Algorithm

## Instructions
In this assignment, you will combine your knowledege of informed search algorithm with the adversarial search game tree to teach the R2D2s how to play optimally in a flag capture game.

## Step 1: Create the Game Board
Similar to the A* game in last excercise, the game board also takes in the vertices and edges to define a graph. In addition to these two parameters, we also need to define the position of the robots and the flags.

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
You could expect the following outputs:

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

## Step 2: Define the A* algorithm and evaluate function
Implement the A star to calculate the shortest path between two vertics. This step is almost the same as the solution of excercise 2, but it should be noticed that, in the cases of the opponents occupy the flag, the path cannot lead to the goal(robots will be considered as obstacles), thus the total length of the path should be modified.

```python
def Astar(self, start, goal):
	'''
		return the path and length of the path
		in the form of (path, len(path))
	'''
	pass
```
You could expect the following outputs：

```python
>>> graph.Astar((0, 0), (2, 2))
([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], 5)
```

The evaluate function estimate the utilities (scores) of current state which reflect the chance of wining the game. There are various methods to evaluate the utilities in this game, and different approaches will have influence on the performance of the robot and game results. Here is a recommended solution: using the difference of the minimum cost to reach the flag of seach team as the utility, which is:
$U(D2) = min(Astar_cost(D2_1, flag_D2), Astar_cost(D2_2, flag_D2)) - min(Astar_cost(D2_1, flag_D2), Astar_cost(D2_2, flag_D2))$
