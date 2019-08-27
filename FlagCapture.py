import math
import queue
from collections import defaultdict
inf = float('inf')

class FlagCaptureGraph:
    def __init__(self, V, E, initial_state, flag):
        self.vertics = V
        self.edges = E
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
                print(current_pos)
                print(self.dist_between(current_pos, goal))
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

    def perform_move(self, current_state, move_state):
        move_robot = self.state[current_state]
        self.state[move_state] = move_robot
        self.state[current_state] = 'x'
        self.robot_pos[move_robot] = move_state
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
