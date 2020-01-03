class Graph():
    def __init__(self, nodes_num): # index num starts from 0
        self.nodes_num = nodes_num
        self.nodes = [i for i in range(self.nodes_num)]
        self.nodes_visited = [False for i in range(self.nodes_num)]
        self.adj_of_node = [[] for i in range(self.nodes_num)]
    def build_undirected_edge(self, u, v):
        if v not in self.adj_of_node[u]:
            self.adj_of_node[u].append(v)
        if u not in self.adj_of_node[v]:
            self.adj_of_node[v].append(u)
    def build_directed_edge(self, u, v):
        if v not in self.adj_of_node[u]:
            self.adj_of_node[u].append(v)
