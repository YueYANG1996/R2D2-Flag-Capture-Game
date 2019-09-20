##include your imports here###

class FlagCaptureGraph:
    
    ##############################################
    ##                  Part 1                  ##
    ##############################################
    
    def __init__(self, V, E, initial_state, flag):
        '''
		self.vertices --  store the vertices of the graph
		self.edges   --  store the edges of the graph
		self.map     --  store the state of the gameboard
		self.flag    -- store the positions of the flags
		
		self.state   --  dictionary to represent the state of each grid, keys = vertices, value = vertex value in map
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
        pass
    
    def successors(self, D2):
        pass
    
    def copy(self):
        pass

    def game_over(self):
        pass
    
    ##############################################
    ##                  Part 3                  ##
    ##############################################

    def Astar(self, start, goal):
        '''
		return the path and length of the path
		in the form of (path, len(path))
	    '''
        pass

    def evaluate(self, D2):
        pass
    
    ##############################################
    ##                  Part 4                  ##
    ##############################################

    def alpha_beta_max(self, D2, original_D2, limit, alpha, beta):
        pass

    def alpha_beta_min(self, D2, original_D2, limit, alpha, beta):
        pass

    def get_best_move(self, D2, limit):
        return self.alpha_beta_max(D2, D2, limit, float("-inf"),
            float("inf"))

    def printmap(self):
        for row in self.map:
            row_str = ''
            for grid in row:
                if grid == 'D2_1' or grid == 'D2_2':
                    add = '* '
                elif grid == 'Q5_1' or grid == 'Q5_2':
                    add = 'o '
                else:
                    add = 'x '
                row_str += add
            print(row_str)
