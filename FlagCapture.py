import math
import queue
import copy
from collections import defaultdict
inf = float('inf')

class FlagCaptureGraph:
    def __init__(self, V, E, initial_state, flag):
        self.vertics = V
        self.edges = E
        self.map = initial_state
        self.state = {}
        self.robot_pos = {}
        for vertic in self.vertics:
            if initial_state[vertic[0]][vertic[1]] != 'x':
                self.robot_pos[initial_state[vertic[0]][vertic[1]]] = vertic
            self.state[vertic] = initial_state[vertic[0]][vertic[1]]
        self.flag = flag


    def neighbors(self, u):
        neighbors_lst = []
        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            next_state = (u[0] + x, u[1] + y)
            if (u, next_state) in self.edges:
                if self.state[next_state] == 'x':
                    neighbors_lst.append(next_state)
        return neighbors_lst

    def dist_between(self, u, v):
        return math.sqrt(pow(u[0] - v[0], 2) + pow(u[1] - v[1], 2))


    def Astar(self, start, goal):
        rows = self.vertics[-1][0]
        cols = self.vertics[-1][1]
        node_visited = []
        q = queue.PriorityQueue()
        astar_cost_start = math.sqrt(pow(start[0] - goal[0],2) + pow(start[1] - goal[1],2))
        cost_start = 0
        path = [start]
        q.put((astar_cost_start, cost_start, path, start))
        
        while q.empty() != True:
            current_node = q.get()
            astar_cost, current_cost, path, current_pos = current_node[0], current_node[1], current_node[2], current_node[3]
            
            if self.state[goal] != 'x':
                if self.dist_between(current_pos, goal) == 1:
                    return (path, float('inf'))

            if current_pos == goal:
                return (path, len(path))

            if current_pos not in node_visited:
                node_visited.append(current_pos)
                for node in self.neighbors(current_pos):
                    expand_cost = current_cost + math.sqrt(pow(node[0] - current_pos[0],2) + pow(node[1] - current_pos[1],2))
                    heuristic = math.sqrt(pow(node[0] - goal[0],2) + pow(node[1] - goal[1],2))
                    expand_astar_cost = expand_cost + heuristic
                    new_state = (expand_astar_cost, expand_cost, path + [node], node)
                    q.put(new_state)
        return (path, len(path))

    def copy(self):
        new_map = copy.deepcopy(self.map)
        return FlagCaptureGraph(self.vertics, self.edges, new_map, self.flag)


    def game_over(self, D2):
        if self.robot_pos['D2_1'] == self.flag['flag_D2'] or self.robot_pos['D2_2'] == self.flag['flag_D2'] or self.robot_pos['Q5_1'] == self.flag['flag_Q5'] or self.robot_pos['Q5_2'] == self.flag['flag_Q5']:
            return True

    def printmap(self):
        for row in self.map:
            row_str = ''
            for grid in row:
                if grid == 'D2_1' or grid == 'D2_2':
                    add = '*'
                elif grid == 'Q5_1' or grid == 'Q5_2':
                    add = 'o'
                else:
                    add = 'x'
                row_str += add
            print(row_str)

    def successors(self, D2):
        if D2 == True:
            D2_1_current_state = self.robot_pos['D2_1']
            for D2_1_next_state in self.neighbors(D2_1_current_state):
                move = {}
                move['D2_1'] = D2_1_next_state
                new_game_1 = self.copy()
                new_game_1.perform_move(D2_1_current_state, D2_1_next_state)
                D2_2_current_state = new_game_1.robot_pos['D2_2']

                for D2_2_next_state in new_game_1.neighbors(D2_2_current_state):
                    move['D2_2'] = D2_2_next_state
                    new_game_2 = new_game_1.copy()
                    new_game_2.perform_move(D2_2_current_state, D2_2_next_state)
                    yield move, new_game_2
        else:
            Q5_1_current_state = self.robot_pos['Q5_1']
            for Q5_1_next_state in self.neighbors(Q5_1_current_state):
                move = {}
                move['Q5_1'] = Q5_1_next_state
                new_game_1 = self.copy()
                new_game_1.perform_move(Q5_1_current_state, Q5_1_next_state)
                Q5_2_current_state = new_game_1.robot_pos['Q5_2']

                for Q5_2_next_state in new_game_1.neighbors(Q5_2_current_state):
                    move['Q5_2'] = Q5_2_next_state
                    new_game_2 = new_game_1.copy()
                    new_game_2.perform_move(Q5_2_current_state, Q5_2_next_state)
                    yield move, new_game_2

    def perform_move(self, current_state, move_state):
        move_robot = self.state[current_state]
        self.state[move_state] = move_robot
        self.state[current_state] = 'x'
        self.robot_pos[move_robot] = move_state
        self.map[current_state[0]][current_state[1]] = 'x'
        self.map[move_state[0]][move_state[1]] = move_robot
        pass

    def evaluate(self, D2):
        cost_D2_1 = self.Astar(self.robot_pos['D2_1'], self.flag['flag_D2'])[1]
        cost_D2_2 = self.Astar(self.robot_pos['D2_2'], self.flag['flag_D2'])[1]
        cost_Q5_1 = self.Astar(self.robot_pos['Q5_1'], self.flag['flag_Q5'])[1]
        cost_Q5_2 = self.Astar(self.robot_pos['Q5_2'], self.flag['flag_Q5'])[1]
        if D2 == True:
            return min(cost_Q5_1, cost_Q5_2) - min(cost_D2_1, cost_D2_2)
        else:
            return - min(cost_Q5_1, cost_Q5_2) + min(cost_D2_1, cost_D2_2)

    '''def alpha_beta_max(self, D2, original_D2, limit, alpha, beta):
        if limit <= 0 or self.game_over(D2):
            return None, self.evaluate(original_D2), 1
        best_move, best_value, total_leaves = None, float("-inf"), 0
        for move, new_game in self.successors(vertical):
            new_move, new_value, new_leaves = new_game.alpha_beta_min(
                not vertical, original_vertical, limit - 1, alpha, beta)
            total_leaves += new_leaves
            if new_value > best_value:
                best_move, best_value = move, new_value
            if best_value >= beta:
                break
            alpha = max(alpha, best_value)
        return best_move, best_value, total_leaves

    def alpha_beta_min(self, vertical, original_vertical, limit, alpha, beta):
        if limit <= 0 or self.game_over(vertical):
            return None, self.evaluate(original_vertical), 1
        best_move, best_value, total_leaves = None, float("inf"), 0
        for move, new_game in self.successors(vertical):
            new_move, new_value, new_leaves = new_game.alpha_beta_max(
                not vertical, original_vertical, limit - 1, alpha, beta)
            total_leaves += new_leaves
            if new_value < best_value:
                best_move, best_value = move, new_value
            if best_value <= alpha:
                break
            beta = min(beta, best_value)
        return best_move, best_value, total_leaves

    def get_best_move(self, vertical, limit):
        return self.alpha_beta_max(vertical, vertical, limit, float("-inf"),
            float("inf"))'''
