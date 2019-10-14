import pickle
from generate_map import generate_random, generate_map
from FlagCapture import FlagCaptureGraph as Graph
import os


base_dir = os.path.abspath(os.path.dirname(__file__))

robots_pos = {
            'D2_1': None,
            'D2_2': None,
            'Q5_1': None,
            'Q5_2': None,
        }

flags_pos = {
            'flag_D2': None,
            'flag_Q5': None
        }

size_ls = [
    (4, 4),
    (5, 5),
    (6, 6),
    ]

for r, c in size_ls:
    for i in range(1, 4):
        vertics, edges = generate_map(r, c, [])
        graph = Graph(V=vertics, E=edges, robots_pos=robots_pos, flags_pos=flags_pos)
        fp = os.path.join(base_dir, 'scenes', 'scene_{}x{}_{}.sc'.format(r, c, i))
        print(fp)
        with open(fp, 'wb') as f:
            pickle.dump(graph, f)
