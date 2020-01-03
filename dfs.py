from graph_class import Graph

def dfs(G, start):
    path = []
    G.nodes_visited = [False for i in range(G.nodes_num)]
    dfs_util(G, start, path)
    return path

def dfs_util(G, start, path):
    G.nodes_visited[start] = True
    path.append(start)
    for neighbor in G.adj_of_node[start]:
        if G.nodes_visited[neighbor] == False:
            dfs_util(G, neighbor, path)

G1 = Graph(13)
G1.build_undirected_edge(0,1)
G1.build_undirected_edge(0,9)
G1.build_undirected_edge(1,8)
G1.build_undirected_edge(2,3)
G1.build_undirected_edge(3,4)
G1.build_undirected_edge(3,5)
G1.build_undirected_edge(3,7)
G1.build_undirected_edge(5,6)
G1.build_undirected_edge(6,7)
G1.build_undirected_edge(7,8)
G1.build_undirected_edge(7,10)
G1.build_undirected_edge(7,11)
G1.build_undirected_edge(8,9)
G1.build_undirected_edge(10,7)
G1.build_undirected_edge(10,11)
print(dfs(G1, 0))
print(dfs(G1, 5))

G2 = Graph(18)
G2.build_undirected_edge(5,1)
G2.build_undirected_edge(5,17)
G2.build_undirected_edge(5,16)
G2.build_undirected_edge(0,4)
G2.build_undirected_edge(0,8)
G2.build_undirected_edge(0,14)
G2.build_undirected_edge(0,13)
G2.build_undirected_edge(15,9)
G2.build_undirected_edge(15,2)
G2.build_undirected_edge(15,10)
G2.build_undirected_edge(3,9)
G2.build_undirected_edge(6,7)
G2.build_undirected_edge(6,11)
#print(find_all_group(G2, G2.nodes_num))
print(dfs(G2, 0))
