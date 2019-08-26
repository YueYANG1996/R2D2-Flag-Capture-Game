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
        lst = []
        for i in range(len(self.edges)):
            current_set = self.edges[i]
            if u in current_set:
                for node in current_set:
                    if node != u:
                        lst.append(node)
        return lst

    def dist_between(self, u, v):
        if v in self.neighbors(u):
        	return math.sqrt(pow(u[0] - v[0], 2) + pow(u[1] - v[1], 2))
        else:
        	return None