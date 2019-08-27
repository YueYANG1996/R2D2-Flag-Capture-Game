import math
import queue
from collections import defaultdict
inf = float('inf')

class FlagCaptureGraph:
    def __init__(self, V, E, state):
        self.vertics = V
        self.edges = E
        self.state = state

    def neighbors(self, u):
        neighbors_lst = []
        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            next_state = (u[0] + x, u[1] + y)
            if self.state[next_state[0]][next_state[1]] == 'x' and (u, next_state) in self.edges:
                neighbors_lst.append(next_state)
        return neighbors_lst

    def dist_between(self, u, v):
        if v in self.neighbors(u):
            return math.sqrt(pow(u[0] - v[0], 2) + pow(u[1] - v[1], 2))
        else:
            return None

    def A_star(self, start, goal):
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
            
            if current_pos == goal:
                return path

            if current_pos not in node_visited:
                node_visited.append(current_pos)
                for node in self.neighbors(current_pos):
                    expand_cost = current_cost + math.sqrt(pow(node[0] - current_pos[0],2) + pow(node[1] - current_pos[1],2))
                    heuristic = math.sqrt(pow(node[0] - goal[0],2) + pow(node[1] - goal[1],2))
                    expand_astar_cost = expand_cost + heuristic
                    new_state = (expand_astar_cost, expand_cost, path + [node], node)
                    q.put(new_state)
        return path, len(path)