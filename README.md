# Robot Excercise 3: Flag Capture Game using a Minimax Algorithm

## Instructions
In this assignment, you will combine your knowledge of informed search algorithms with the adversarial search game tree to teach the R2D2s how to play optimally in a capture the flag game.

In this game, there will be two teams of two robots each. One team will consist of two D2 robots, and the other team will consist of two Q5 robots. The goal of the game is to have one of the teams "win" by capturing the flag corresponding to their team first.

## Step 1. Create the Game Board [15 points]

1. **[8 points]** Similar to the A* game in the last extra credit exerecise, the game board in this assignment also takes in the vertices and edges to define a graph. Along with these two parameters, we also need to define the position of the robots and the flags. These location vertices will be passed to the constructor for our FlagCaptureGraph game.

```python
def __init__(self, V, E, robots_pos, flags_pos):
	'''
		self.vertices --  store the vertices of the graph
		self.edges   --  store the edges of the graph
		self.robots_pos -- store the positions of the robots in a dictionary, keys = robot name, value = vertex
		self.flags_pos    -- store the positions of the flags
	'''
	pass
```
Given the inputs as shown, you should match the following outputs (the printmap function is already defined in our skeleton file):

```python
>>> V, E = generate_map(4, 4, [])
>>> robots_pos = {'D2_1': (0, 0), 'D2_2': (1, 0), 'Q5_1': (2, 3), 'Q5_2': (3, 3)}
>>> flags_pos = {'flag_D2': (3, 2), 'flag_Q5': (0, 1)}
>>> graph = FlagCaptureGraph(V, E, robots_pos, flags_pos)
>>> printmap(graph)
○   ⚑   ☐   ☐   
               
○   ☐   ☐   ☐   
               
☐   ☐   ☐   ●   
               
☐   ☐   ⚐   ● 
```

2. **[5 points]** Implement the neighbors function to return neighbors of a vertex that are not currently occupied by a robot. The return value should be a list containing all non-occupied vertices adjacent to the input vertex (if the input vertex is on a corner/edge, adjust accordingly).

```python	
def neighbors(self, u):
	'''
		Return the neighbors of a vertex.
		If there is a robot occupying the neighboring vertex, 
		do not return that vertex as a neighbor.
	'''
	pass
```
With the FlagCaptureGraph variable graph as defined above, you should have:

```python
>>> graph.neighbors((0, 0))
[(0, 1)]
```

3. **[2 points]** Implement the distance function to return the euclidean distance between two vertices.

```python
def dist_between(self, u, v):
	'''
		Return the distance between two vertices.
	'''
	pass
```

```python
>>> graph.dist_between((0, 0), (0, 1))
1.0
```
## Step 2. Defining the Game Rules [23 points]

In this step, we will define the basic rules of the game, such as how to update the game state, what the successors of a state are, how to judge whether the game is over, etc. You will be updating the following functions:

```python	
def perform_move(self, robot, direction):
	'''
		Execute the movement of the robot and update the game accordingly, updating the state,
		map, and robot_pos parameters. This function should throw an exception if the move is not leagl.
	'''
	pass
	
def copy(self):
	'''
		Return a new FlagCaptureGraph object that is identical to the current
	'''
	pass

def successors(self, D2):
	'''
		Generate the successors of a game state. The parameter D2 indicates whether it is 
		the D2 team's turn. This function should yield a tuple where the first element is
		the movements of the two robots (a dictionary with keys of the robots and their
		next positions), as well as a copy of the new game map after these moves are performed.
	'''
	pass
	
def game_over(self):
	'''
		Return a boolean indicating if the game is over.
	'''
	pass
```

1. **[8 points]** Implement the function: ```perform_move(self, robot, direction)``` to execute the movement of the robot and update the game accordingly. Make sure to update the map, state, and robot_pos parameters.  The first input corresponds to the the robot, and the second corresponds to the direction that the robot should move. You should thown an exception if this function tries to do something illegal (e.g. moves into an occupied space, or moves off the board, etc.).

```python
>>> graph.printmap()
○ ◙ ☐ ☐
○ ☐ ☐ ☐
☐ ☐ ☐ •
☐ ☐ ◘ •

>>> graph.perform_move((0, 0), (0, 1))
'east'

>>> graph.printmap()
☐ ○ ☐ ☐
○ ☐ ☐ ☐
☐ ☐ ☐ •
☐ ☐ ◘ •
>>> graph.map
[['x', 'D2_1', 'x', 'x'], ['D2_2', 'x', 'x', 'x'], ['x', 'x', 'x', 'Q5_1'], ['x', 'x', 'x', 'Q5_2']]
>>> graph.state
{(0, 0): 'x', (0, 1): 'D2_1', (0, 2): 'x', (0, 3): 'x', (1, 0): 'D2_2', (1, 1): 'x', (1, 2): 'x', (1, 3): 'x', (2, 0): 'x', (2, 1): 'x', (2, 2): 'x', (2, 3): 'Q5_1', (3, 0): 'x', (3, 1): 'x', (3, 2): 'x', (3, 3): 'Q5_2'}
>>> graph.robot_pos
{'D2_1': (0, 1), 'D2_2': (1, 0), 'Q5_1': (2, 3), 'Q5_2': (3, 3)} 
```

2. **[2 points]** Implement ```copy(self)``` to return a new FlagCaptureGraph object that is identical to the current, making a deep copy of the current map in doing so. You do not need to deep copy the vertex, edge, or flag parameters as these will not change during a game.

```python
>>> new_graph = graph.copy()
>>> print(new_graph.state == graph.state)
True
>>> new_graph.perform_move((0, 0), (0, 1))
'east'
>>> print(new_graph.state == graph.state)
False
```

3. **[10 points]** Implement the function: ```successors(self, D2)``` to generate the successors of a game state. The parameter D2 indicates whether it is the D2 team's turn. During each turn for a team, the robot 1 will move first and then the robot 2, meaning that if the first robot leaves a position, that position is open for the robot's teammate on its move. This function should yield a tuple where the first element is the movements of the two robots (a dictionary with keys of the robots and their next positions), as well as a copy of the new game map after these moves are performed. For the FlagCaptureGraph graph defined previously, we expect the following outputs:

```python
>>> for move, game in graph.successors(D2 = True):
...     print(move)
...     game.printmap()
... 
{'D2_1': (0, 1), 'D2_2': (0, 0)}
○ ○ ☐ ☐
☐ ☐ ☐ ☐
☐ ☐ ☐ •
☐ ☐ ◘ •
{'D2_1': (0, 1), 'D2_2': (1, 1)}
☐ ○ ☐ ☐
☐ ○ ☐ ☐
☐ ☐ ☐ •
☐ ☐ ◘ •
{'D2_1': (0, 1), 'D2_2': (2, 0)}
☐ ○ ☐ ☐
☐ ☐ ☐ ☐
○ ☐ ☐ •
☐ ☐ ◘ •
``` 
```python
>>> for move, game in graph.successors(D2 = False):
...     print(move)
...     game.printmap()
... 
{'Q5_1': (1, 3), 'Q5_2': (2, 3)}
○ ◙ ☐ ☐
○ ☐ ☐ •
☐ ☐ ☐ •
☐ ☐ ◘ ☐
{'Q5_1': (1, 3), 'Q5_2': (3, 2)}
○ ◙ ☐ ☐
○ ☐ ☐ •
☐ ☐ ☐ ☐
☐ ☐ • ☐
{'Q5_1': (2, 2), 'Q5_2': (2, 3)}
○ ◙ ☐ ☐
○ ☐ ☐ ☐
☐ ☐ • •
☐ ☐ ◘ ☐
{'Q5_1': (2, 2), 'Q5_2': (3, 2)}
○ ◙ ☐ ☐
○ ☐ ☐ ☐
☐ ☐ • ☐
☐ ☐ • ☐
``` 

4. **[10 points]** Implement ```game_over(self)``` to reflect whether a game is over or not. The criteria for a game being over is if a robot from a team is on its flag.

```python
>>> V = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
>>> E = [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((0, 1), (0, 2)), ((0, 1), (1, 1)), ((0, 1), (0, 0)), ((0, 2), (0, 3)), ((0, 2), (1, 2)), ((0, 2), (0, 1)), ((0, 3), (1, 3)), ((0, 3), (0, 2)), ((1, 0), (0, 0)), ((1, 0), (1, 1)), ((1, 0), (2, 0)), ((1, 1), (0, 1)), ((1, 1), (1, 2)), ((1, 1), (2, 1)), ((1, 1), (1, 0)), ((1, 2), (0, 2)), ((1, 2), (1, 3)), ((1, 2), (2, 2)), ((1, 2), (1, 1)), ((1, 3), (0, 3)), ((1, 3), (2, 3)), ((1, 3), (1, 2)), ((2, 0), (1, 0)), ((2, 0), (2, 1)), ((2, 0), (3, 0)), ((2, 1), (1, 1)), ((2, 1), (2, 2)), ((2, 1), (3, 1)), ((2, 1), (2, 0)), ((2, 2), (1, 2)), ((2, 2), (2, 3)), ((2, 2), (3, 2)), ((2, 2), (2, 1)), ((2, 3), (1, 3)), ((2, 3), (3, 3)), ((2, 3), (2, 2)), ((3, 0), (2, 0)), ((3, 0), (3, 1)), ((3, 1), (2, 1)), ((3, 1), (3, 2)), ((3, 1), (3, 0)), ((3, 2), (2, 2)), ((3, 2), (3, 3)), ((3, 2), (3, 1)), ((3, 3), (2, 3)), ((3, 3), (3, 2))]
>>> state = [['D2_1', 'x', 'x', 'x'], ['D2_2', 'x', 'x', 'x'], ['x', 'x', 'x', 'Q5_1'], ['x', 'x', 'x', 'Q5_2']]
>>> flag = {'flag_D2': (3, 2), 'flag_Q5': (0, 1)}
>>> graph = FlagCaptureGraph(V, E, state, flag)

>>> graph.game_over()
False

>>> state = [['D2_1', 'x', 'x', 'x'], ['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'Q5_1'], ['x', 'x', 'D2_2', 'Q5_2']]
>>> graph = FlagCaptureGraph(V, E, state, flag)

>>> graph.game_over()
True
```

## Step 3: Define the A* algorithm and the evaluate function [32 points]

1. **[25 points]** Implement the A star algorithm to calculate the shortest path between two vertices. This function should return the path and length of the path in the form of (path, len(path)), here the path being a list of the vertices encountered along the path. In the case where a robot occupies the goal vertex, the path cannot lead to the goal (robots will be considered as obstacles). In this case, when the robot ends up next to the goal vertex, return the current path as well as the path length plus one.

```python
def Astar(self, start, goal):
	'''
		return an optimal path and length of the path
		in the form of (path, len(path))
	'''
	pass
```
Using the same parameters of the graph as above, you should expect the following outputs (any path that is the shortest is alright)：

```python
>>> graph.Astar((0, 0), (2, 2))
([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)], 5)
```

2. **[7 points]** The ```evaluate(self, D2)``` function estimates the utilities (scores) of the current state which reflects the chance of winning the game. There are various methods to evaluate the utilities in this game, and different approaches will have different influences on the performance of the robots and the game results. Here is a recommended solution: using the difference of the minimum cost to reach the flag of each team as the utility. D2 is a boolean representing whether the utility is for the D2 team or not. If the D2 team is "winning", their utility should be higher.

```python
def evaluate(self, D2):
	'''
		Return a numeric value (float/int) representing the utility for the D2 or Q5 team.
		If the team is "winning" their utility should be higher.
	'''
	pass
```

## Step 4: Implement Minimax algorithm with alpha-beta pruning [30 points]

In this part, you will utilize your knowledge of alpha-beta minimax algorithm to help the R2D2s find out the optimal movements.

```python
def alpha_beta_max(self, D2, original_D2, limit, alpha, beta):
	pass

def alpha_beta_min(self, D2, original_D2, limit, alpha, beta):
	pass

def get_best_move(self, D2, limit):
	'''
		D2 - boolean representing if it is the D2 team's turn
		limit - upper bound on the number of turns
		
		Return the best move, its utility value, and the total number of leaves encountered as
		(best_move, best_value, total_leaves)
	'''
	pass
```

Here, you are free to use whatever implementation of the minimax algorithm you want. We will not be testing the alpha_beta_max or alpha_beta_min functions, just the get_best_move function. This means you can also alter the parameters of the first two functions to whatever feels best.

However, we require that in your get_best_move function, your return value be of the type ```best_move, best_value, total_leaves```, where best_move is the best move (syntax equivalent to the first element of the successors function), best_value is some value corresponding to what ```alpha_beta_max``` returns (won't be testing on this value), and total_leaves is the total number of leaf elements encountered, where a leaf is a finished goal state or any state after performing limit amount of moves. The return type of get_best_move should be a hint on what the return types of alpha_beta_max and alpha_beta_min should look like.

The inputs to the get_best_move function are D2, a boolean representing if it is the D2 team's turn, and limit, an upper bound on the number of turns to take.

After you finished the minimax algorithm, you could now play the game in a virtual environment.

```python
>>> from game_simulation import simulate_game
>>> record_game = simulate_game(graph, D2 = True, limit = 4)
Round: 1
D2 Turn
☐ ○ ☐ ☐
○ ☐ ☐ ☐
☐ ☐ ☐ •
☐ ☐ ◘ •
             
☐ ○ ☐ ☐
☐ ☐ ☐ ☐
○ ☐ ☐ •
☐ ☐ ◘ •
             
Q5 Turn
☐ ○ ☐ ☐
☐ ☐ ☐ •
○ ☐ ☐ ☐
☐ ☐ ◘ •
             
☐ ○ ☐ ☐
☐ ☐ ☐ •
○ ☐ ☐ ☐
☐ ☐ • ☐

...

Q5 Turn
☐ • ☐ ☐
☐ ☐ ☐ ○
☐ ○ ☐ ☐
• ☐ ◘ ☐
             
Q5 WIN
```

## Step 5: Set up your Robots to play a real game [0 points]
You will apply your algorithm in the real robots to visulize your program. The ```record_game``` store the movement of each robot and the data looks like:

```python
>>> record_game
[('D2_1', 'east'), ('D2_2', 'south'), ('Q5_1', 'north'), ('Q5_2', 'west'), ('D2_1', 'east'), ('D2_2', 'south'), ('Q5_1', 'west'), ('Q5_2', 'west'), ('D2_1', 'east'), ('D2_2', 'north'), ('Q5_1', 'north'), ('Q5_2', 'west'), ('D2_1', 'south'), ('D2_2', 'east'), ('Q5_1', 'west')]
```

You could implement an API to send commands to the robots to perform the movements. First, you need to connect to all of your robots using the following code.  

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



