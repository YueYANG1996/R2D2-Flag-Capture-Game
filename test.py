from FlagCapture import FlagCaptureGraph, printmap, generate_map
V, E = generate_map(4, 4, [])
robots_pos = {'D2_1': (0, 0), 'D2_2': (1, 0), 'Q5_1': (2, 3), 'Q5_2': (3, 3)}
flags_pos = {'flag_D2': (3, 2), 'flag_Q5': (0, 1)}
graph = FlagCaptureGraph(V, E, robots_pos, flags_pos)
printmap(graph)