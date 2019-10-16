import math
import queue
import copy
from collections import defaultdict
inf = float('inf')


class FlagCaptureGraph:
    def __init__(self, V, E, robots_pos, flags_pos):
        self.vertics = V
        self.edges = E
        self.flags_pos = flags_pos
        self.robots_pos = robots_pos
        self.direct2vec = {'south': (1, 0), 'north': (-1, 0), 'east': (0, 1), 'west': (0, -1), 'stay': (0, 0)}
        self.adjacent = {}
        for node in self.vertics:
            neighbors = []
            for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_state = (node[0] + x, node[1] + y)
                if (node, next_state) in self.edges:
                    if next_state not in self.robots_pos.values():
                        neighbors.append(next_state)
            self.adjacent[node] = neighbors
        
    def neighbors(self, u):
        return self.adjacent[u]

    def dist_between(self, u, v):
        return math.sqrt(pow(u[0] - v[0], 2) + pow(u[1] - v[1], 2))

    def copy(self):
        new_robots_pos = copy.deepcopy(self.robots_pos)
        new_flag_pos = copy.deepcopy(self.flags_pos)
        return FlagCaptureGraph(self.vertics, self.edges, new_robots_pos, new_flag_pos)

    def game_over(self):
        if self.robots_pos['D2_1'] == self.flags_pos['flag_D2'] or self.robots_pos['D2_2'] == self.flags_pos['flag_D2'] or self.robots_pos['Q5_1'] == self.flags_pos['flag_Q5'] or self.robots_pos['Q5_2'] == self.flags_pos['flag_Q5']:
            return True
        else:
            return False

    def islegalmove(self, move_robot, move_direction):
        current_pos = self.robots_pos[move_robot]
        movement = self.direct2vec[move_direction]
        next_pos = (current_pos[0] + movement[0], current_pos[1] + movement[1])
        if next_pos in self.robots_pos.values():
            return False
        else:
            if (current_pos, next_pos) in self.edges:
                return True
            else:
                return False

    def legalmoves(self, move_robot):
        result = []
        for move_direction in ['south', 'north', 'east', 'west']:
            if self.islegalmove(move_robot, move_direction):
                result.append(move_direction)
        if len(move_direction) == 0:
            result.append('stay')
        return result

    def perform_move(self, move_robot, move_direction):
        if self.islegalmove(move_robot, move_direction) == False:
            return None
        movement = self.direct2vec[move_direction]
        current_pos = self.robots_pos[move_robot]
        self.robots_pos[move_robot] = (current_pos[0] + movement[0], current_pos[1] + movement[1])

    def successors(self, D2):
        if D2 == True:
            for move_direction_1 in self.legalmoves('D2_1'):
                movement = {}
                movement['D2_1'] = move_direction_1
                new_game_1 = self.copy()
                new_game_1.perform_move('D2_1', move_direction_1)
                for move_direction_2 in new_game_1.legalmoves('D2_2'):
                    movement['D2_2'] = move_direction_2
                    new_game_2 = new_game_1.copy()
                    new_game_2.perform_move('D2_2', move_direction_2)
                    yield movement, new_game_2
        else:
            for move_direction_1 in self.legalmoves('Q5_1'):
                movement = {}
                movement['Q5_1'] = move_direction_1
                new_game_1 = self.copy()
                new_game_1.perform_move('Q5_1', move_direction_1)
                for move_direction_2 in new_game_1.legalmoves('Q5_2'):
                    movement['Q5_2'] = move_direction_2
                    new_game_2 = new_game_1.copy()
                    new_game_2.perform_move('Q5_2', move_direction_2)
                    yield movement, new_game_2

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
            
            if goal in self.robots_pos.values():
                if self.dist_between(current_pos, goal) == 1:
                    return (path, len(path) + 1)

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

    def evaluate(self, D2):
        cost_D2_1 = self.Astar(self.robots_pos['D2_1'], self.flags_pos['flag_D2'])[1]
        cost_D2_2 = self.Astar(self.robots_pos['D2_2'], self.flags_pos['flag_D2'])[1]
        cost_Q5_1 = self.Astar(self.robots_pos['Q5_1'], self.flags_pos['flag_Q5'])[1]
        cost_Q5_2 = self.Astar(self.robots_pos['Q5_2'], self.flags_pos['flag_Q5'])[1]
        
        # freedom_D2_1 = len(self.legalmoves('D2_1'))
        # freedom_D2_2 = len(self.legalmoves('D2_2'))
        # freedom_Q5_1 = len(self.legalmoves('Q5_1'))
        # freedom_Q5_2 = len(self.legalmoves('Q5_2'))

        utilities = 0
        if D2 == True:
            if min(cost_Q5_1, cost_Q5_2) <= 2:
                return min(cost_Q5_1, cost_Q5_2)
            else:
                return cost_Q5_1 + cost_Q5_2 - (cost_D2_1 + cost_D2_2)
        else:
            if min(cost_D2_1, cost_D2_2) <= 2:
                return min(cost_D2_1, cost_D2_2)
            else:
                return - (cost_Q5_1 + cost_Q5_2) + (cost_D2_1 + cost_D2_2)

    def alpha_beta_max(self, D2, original_D2, limit, alpha, beta):
        if limit <= 0 or self.game_over():
            return None, self.evaluate(original_D2), 1
        best_move, best_value, total_leaves = None, float("-inf"), 0
        for move, new_game in self.successors(D2):
            new_move, new_value, new_leaves = new_game.alpha_beta_min(
                not D2, original_D2, limit - 1, alpha, beta)
            total_leaves += new_leaves
            if new_value > best_value:
                best_move, best_value = move, new_value
            if best_value >= beta:
                break
            alpha = max(alpha, best_value)
        return best_move, best_value, total_leaves

    def alpha_beta_min(self, D2, original_D2, limit, alpha, beta):
        if limit <= 0 or self.game_over():
            return None, self.evaluate(original_D2), 1
        best_move, best_value, total_leaves = None, float("inf"), 0
        for move, new_game in self.successors(D2):
            new_move, new_value, new_leaves = new_game.alpha_beta_max(
                not D2, original_D2, limit - 1, alpha, beta)
            total_leaves += new_leaves
            if new_value < best_value:
                best_move, best_value = move, new_value
            if best_value <= alpha:
                break
            beta = min(beta, best_value)
        return best_move, best_value, total_leaves

    def get_best_move(self, D2, limit):
        return self.alpha_beta_max(D2, D2, limit, float("-inf"),
            float("inf"))

def printmap(G):
    rows = G.vertics[-1][0] + 1
    cols = G.vertics[-1][1] + 1
    inv_robots_pos = {v: k for k, v in G.robots_pos.items()}
    inv_flags_pos = {v: k for k, v in G.flags_pos.items()}
    for i in range(2 * rows - 1):
        print_row = ''
        if i % 2 == 0:
            for j in range(cols):
                current_node = (int(i / 2), j)
                right_node = (int(i / 2), j + 1)
                pattern = '☐'
                if current_node in G.flags_pos.values():
                    if inv_flags_pos[current_node] == 'flag_D2':
                        pattern = '⚐'
                    elif inv_flags_pos[current_node] == 'flag_Q5':
                        pattern = '⚑'

                if current_node in G.robots_pos.values():
                    if inv_robots_pos[current_node] == 'D2_1':
                        pattern = '➀'
                    elif inv_robots_pos[current_node] == 'D2_2':
                        pattern = '➁'
                    elif inv_robots_pos[current_node] == 'Q5_1':
                        pattern = '❶'
                    elif inv_robots_pos[current_node] == 'Q5_2':
                        pattern = '❷'


                if (current_node, right_node) in G.edges and (right_node, current_node) in G.edges:
                    print_row += pattern + ' ' + '  '
                else:
                    if right_node in G.vertics:
                        print_row += pattern + ' ' + '| '
                    else:
                        print_row += pattern + ' ' + '  '
        else:
            for j in range(cols):
                current_node = (math.ceil(i/2), j)
                up_node = (math.ceil(i/2) - 1, j)
                if j == 0:
                    if (current_node, up_node) in G.edges and (up_node, current_node) in G.edges: 
                        print_row += '  ' + ' '
                    else:
                        print_row += '-- '
                else: 
                    if (current_node, up_node) in G.edges and (up_node, current_node) in G.edges:
                        print_row += '  ' + '  '
                    else:
                        print_row += '--- '
        print(print_row)


def generate_map(row, column, barriers):
    vertics = [(i, j) for i in range(row) for j in range(column)]
    edges = []
    for vertic in vertics:
        for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_vertic = (vertic[0] + move[0], vertic[1] + move[1])
            if next_vertic in vertics:
                edges.append((vertic, next_vertic))

    for barrier in barriers:
        edges.remove(barrier)
        edges.remove((barrier[1], barrier[0]))

    return vertics, edges
        