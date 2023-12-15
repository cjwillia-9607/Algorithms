# implement dfs

def dfs(visited, graph, start):
    if start not in visited:
        print(start)
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(visited, graph, neighbor)
    return visited


if __name__ == '__main__':
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
    print(dfs(set(), graph, 'A'))