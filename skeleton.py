##include your imports here###

class FlagCaptureGraph:
    
    ##############################################
    ##                  Part 1                  ##
    ##############################################
    
    def __init__(self, V, E, game_map, flag):
        '''
		self.vertices --  store the vertices of the graph
		self.edges    --  store the edges of the graph
		self.map      --  store the map of the gameboard
		self.flag     -- store the positions of the flags
		
		self.state    --  dictionary to represent the state of each grid, keys = vertices, value = vertex value in map
		self.robot_pos -- store the positions of the robots in a dictionary, keys = robot name, value = vertex
	'''

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
    
    ##############################################
    ##                  Part 2                  ##
    ##############################################
    
    def perform_move(self, current_state, move_state):
	'''
		Execute the movement of the robot and update the game accordingly, updating the state,
		map, and robot_pos parameters. This function should also return the direction of the 
		movement ("north", "south", "west", "east")
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
    
    ##############################################
    ##                  Part 3                  ##
    ##############################################

    def Astar(self, start, goal):
        '''
		return an optimal path and length of the path
		in the form of (path, len(path))
	'''
        pass

    def evaluate(self, D2):
	'''
		Return a numeric value (float/int) representing the utility for the D2 or Q5 team.
		If the team is "winning" their utility should be higher.
	'''
        pass
    
    ##############################################
    ##                  Part 4                  ##
    ##############################################

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
        return self.alpha_beta_max(D2, D2, limit, float("-inf"),
            float("inf"))

####################################################

    def printmap(self):
        for i in range(len(self.map)):
            row_str = ''
            for j in range(len(self.map[0])):
                grid = self.map[i][j]
                if grid == 'D2_1' or grid == 'D2_2':
                    add = '○ '
                elif grid == 'Q5_1' or grid == 'Q5_2':
                    add = '• '
                elif self.flag['flag_D2'] == (i, j):
                    add = '◘ '
                elif self.flag['flag_Q5'] == (i, j):
                    add = '◙ '
                else:
                    add = '☐ '
                row_str += add
            print(row_str)
