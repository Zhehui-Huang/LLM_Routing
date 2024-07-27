import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []
        self.adj_list = {node: [] for node in nodes}
    
    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def is_biconnected(self):
        """ Simple check for biconnection using two DFS starting from any node. """
        def dfs(v, discovery, low, parent, articulation_points):
            nonlocal time
            children = 0
            visited[v] = True
            discovery[v] = low[v] = time
            time += 1

            for (to, _) in self.adj_list[v]:
                if not visited[to]: 
                    parent[to] = v
                    children += 1
                    dfs(to, discovery, low, parent, articulation_points)

                    low[v] = min(low[v], low[to])

                    if parent[v] == -1 and children > 1:
                        articulation_points.add(v)
                    if parent[v] != -1 and low[to] >= discovery[v]:
                        articulation_points.add(v)
                elif to != parent[v]:
                    low[v] = min(low[v], discovery[to])

        n = len(self.nodes)
        visited = [False] * n
        discovery = [float('inf')] * n
        low = [float('inf')] * n
        parent = [-1] * n
        articulation_points = set()
        time = 0

        for node in self.nodes:
            if not visited[node]:
                dfs(node, discovery, low, parent, articulation_points)

        return len(articulation_points) == 0

def find_btsp_tour(cities):
    n = len(cities)
    graph = Graph(list(range(n)))

    # Step 0: Initialize graph and calculate all pairs distances
    all_edges = []
    for i, j in combinations(range(n), 2):
        dist = euclidean_distance(cities[i], cities[j])
        all_edges.append((i, j, dist))

    # Step 1: Sort edges by weight
    all_edges.sort(key=lambda x: x[2])

    # Step 2: Construct a biconnected subgraph with minimal bottleneck value
    eb = []
    eb_graph = Graph(list(range(n)))
    max_edge_in_bb = 0

    for u, v, weight in all_edges:
        eb_graph.add_edge(u, v, weight)
        if not eb_graph.is_biconnected():
            eb.append((u, v, weight))
            max_edge_in_bb = max(max_edge_in_bb, weight)
        else:
            eb_graph.edges.pop()   # remove edge if it makes the graph non-biconnected

    # Tour Identification using the edges in eb
    tour = [0]
    visited = [False] * n
    visited[0] = True

    def find_tour(current):
        if len(tour) == n:
            if (0 in graph.adj_list[current]):
                tour.append(0)
                return True
            else:
                return False
        for neighbor, _ in sorted(graph.adj_list[current], key=lambda x: x[1]):
            if not visited[neighbor]:
                visited[neighbor] = True
                tour.append(neighbor)
                if find_tour(neighbor):
                    return True
                tour.pop()
                visited[neighbor] = False
        return False

    find_tour(0)

    tour_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    
    return {'Tour': tour, 'Total travel cost': tour_cost, 'Maximum distance between consecutive cities': max_distance}

# City coordinates
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

result = find_btsp_tour(cities)
print('Tour:', result['Tour'])
print('Total travel cost:', result['Total travel respect'])
print('Maximum distance between consecutive cities:', result['Maximum distance between consecutive cities'])