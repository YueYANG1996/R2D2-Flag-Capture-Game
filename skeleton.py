##include your imports here###

class FlagCaptureGraph:
    def __init__(self, V, E, initial_state, flag):

    def neighbors(self, u):
        pass

    def dist_between(self, u, v):
        pass

    def Astar(self, start, goal):
        pass

    def copy(self):
        new_map = copy.deepcopy(self.map)
        return FlagCaptureGraph(self.vertics, self.edges, new_map, self.flag)

    def game_over(self):
        pass

    def successors(self, D2):
        pass

    def perform_move(self, current_state, move_state):
        pass

    def evaluate(self, D2):
        pass

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
