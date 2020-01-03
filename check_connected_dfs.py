nodes_group_id = {}
connected_group_size = 0

def find_all_group(G, n):
    cur_group_id = 0
    for i in range(n + 1):
        if G.nodes_visited[i] == False:
            cur_group_id += 1
            nodes_group_id[cur_group_id] = []
            check_connected_dfs(G, i, cur_group_id)
    return nodes_group_id


def check_connected_dfs(G, i, cur_group_id):
    G.nodes_visited[i] = True
    nodes_group_id[cur_group_id].append(i)
    for neighbor in G.adj_of_node[i]:
        if G.nodes_visited[neighbor] == False:
            check_connected_dfs(G, neighbor, cur_group_id)


def check_connected_num_dfs(G, i):
    if G.nodes_visited[i] != True:
        G.nodes_visited[i] = True
        global connected_group_size
        connected_group_size += 1
        for neighbor in G.adj_of_node[i]:
            check_connected_num_dfs(G, neighbor)
    return connected_group_size
