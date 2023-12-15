# implement A* algorithm

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def A_star(graph, start, goal, h):
    open_set = {start}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: h[start]}
    while len(open_set) > 0:
        current = min(f_score, key=f_score.get)
        if current == goal:
            return reconstruct_path(came_from, current)
        open_set.remove(current)
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph.weight(current, neighbor) # assume graph is weighted
            if neighbor not in g_score.keys() or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h[neighbor]
                if neighbor not in open_set:
                    open_set.add(neighbor)
    return None

if __name__ == '__main__':
    array = [[0, 0, 1, 0, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 1, 1, 1, 0],
             [0, 0, 0, 0, 1, 0]]
    path = A_star(array, (0, 0), (4, 5))
    print(path)