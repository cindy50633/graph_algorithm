from graph_class import Graph
time = 0

def topsort_dfs(G):
    global time
    time = 0
    toporder_list = []
    finished_time = {i: None for i in range(G.nodes_num)}
    G.nodes_visited = [False for i in range(G.nodes_num)]
    for i in range(G.nodes_num):
        if G.nodes_visited[i] == False:
            topsort_dfs_util(G, i, finished_time)
    finished_time = {node: time for node, time in sorted(finished_time.items(),
    key=lambda item: item[1], reverse = True)}
    toporder_list = [finished_time.keys()]
    # print(str(finished_time))
    return toporder_list


def topsort_dfs_util(G, start, finished_time):
    G.nodes_visited[start] = True
    global time
    # time += 1
    for neighbor in G.adj_of_node[start]:
        if G.nodes_visited[neighbor] == False:
            topsort_dfs_util(G, neighbor, finished_time)
    time += 1
    finished_time[start] = time


def topsort_kahn(G):  # sort by degree
    all_set = {i for i in range(G.nodes_num)}
    no_incoming_set = set()
    edge_to_node_set = set()
    indegree_list = [0 for i in range(G.nodes_num)]
    toporder_list = []
    G.nodes_visited = [False for i in range(G.nodes_num)]
    for i in range(G.nodes_num):
        for edge_to in G.adj_of_node[i]:
            indegree_list[edge_to] += 1
            edge_to_node_set.add(edge_to)
    no_incoming_set = all_set.difference(edge_to_node_set)
    while no_incoming_set:
        out_element = no_incoming_set.pop()
        G.nodes_visited[out_element] = True
        toporder_list.append(out_element)
        for i in G.adj_of_node[out_element]:
            indegree_list[i] -= 1
            if indegree_list[i] == 0:
                no_incoming_set.add(i)
    if all((G.nodes_visited)):
        return toporder_list
    else:
        return 'NOT A VALID DAG'
    #print(str(all_set))
    #print(str(edge_to_set))
    #print(str(no_incoming_set))
    #print(str(indegree_list))
    #print(toporder_list)

DAG1 = Graph(8)
DAG1.build_directed_edge(1,4)
DAG1.build_directed_edge(1,6)
DAG1.build_directed_edge(2,7)
DAG1.build_directed_edge(3,4)
DAG1.build_directed_edge(3,7)
DAG1.build_directed_edge(4,5)
DAG1.build_directed_edge(7,5)
DAG1.build_directed_edge(7,6)
#print(topsort_dfs(DAG1))
print(topsort_kahn(DAG1))

DAG2 = Graph(8)
DAG2.build_directed_edge(0,6)
DAG2.build_directed_edge(1,2)
DAG2.build_directed_edge(1,4)
DAG2.build_directed_edge(1,6)
DAG2.build_directed_edge(3,4)
DAG2.build_directed_edge(3,0)
DAG2.build_directed_edge(5,1)
DAG2.build_directed_edge(7,1)
DAG2.build_directed_edge(7,0)
print(topsort_dfs(DAG2))
print(topsort_kahn(DAG2))

DAG3 = Graph(6)
DAG3.build_directed_edge(5,2)
DAG3.build_directed_edge(5,0)
DAG3.build_directed_edge(4,0)
DAG3.build_directed_edge(4,1)
DAG3.build_directed_edge(2,3)
DAG3.build_directed_edge(3,1)
#print(topsort_dfs(DAG3))
print(topsort_kahn(DAG3))
