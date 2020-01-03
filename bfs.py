trace = []
path = []
queue = []

def bfs(G, start):
    G.nodes_visited[start] = True
    trace.append(start)
    queue.append(start)
    while queue != []:
        temp_start = queue.pop(0)
        for neighbor in G.adj_of_node[temp_start]:
            if G.nodes_visited[neighbor] != True:
                G.nodes_visited[neighbor] = True
                trace.append(neighbor)
                queue.append(neighbor)
    return trace


def shortest_path_bfs(G, start, end):  # for finding shortest path
    G.nodes_visited[start] = True
    queue.append(start)
    prev = [None for i in range(G.nodes_num)]
    while queue != []:
        temp_start = queue.pop(0)
        if temp_start == end:
            return reconstruct_shortes_path_bfs(prev, start, end)
        for neighbor in G.adj_of_node[temp_start]:
            if G.nodes_visited[neighbor] != True:
                G.nodes_visited[neighbor] = True
                prev[neighbor] = temp_start
                queue.append(neighbor)
    return path


def reconstruct_shortes_path_bfs(prev, parent, child):
    global path
    while parent != child:
        path.append(child)
        child = prev[child]
    path.append(child)
    path.reverse()
    return path
