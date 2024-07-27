import math
import networkx as nx
from heapq import heappush, heappop

def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

edges = sorted([(euclidean_distance(cities[i], cities[j]), i, j) 
                for i in cities for j in cities if i < j])

# Building the biconnected subgraph using Kruskal's but adapting for biconnectivity
def build_biconnected_subgraph(nodes, edges):
    # Using a union-find data structure to manage connected components
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v, u):
        rootV = find(v)
        rootU = find(u)
        if rootV != rootU:
            if rank[rootV] > rank[rootU]:
                parent[rootU] = rootV
            else:
                parent[rootV] = rootU
                if rank[rootV] == rank[rootU]:
                    rank[rootU] += 1

    graph = nx.Graph()
    graph.add_nodes_from(nodes)

    for weight, v, u in edges:
        if find(v) != find(u):
            graph.add_edge(v, u, weight=weight)
            union(v, u)
            if nx.is_biconnected(graph):  # checking biconnectivity
                return graph
        else:
            # Try adding and checking to allow for algorithmic exploration
            graph.add_edge(v, u, weight=weight)
            if nx.is_biconnected(graph):
                return graph
            graph.remove_edge(v, u)
    return graph  # Return what was built even if not biconnected

def find_tour(G):
    # Finding a Hamiltonian cycle, approximating with nx.approximation.traveling_salesman_problem
    tour = list(nx.approximation.traveling_salesman_problem(G, cycle=True))
    if tour[0] != 0:
        # Ensure it starts and ends at the depot
        start_index = tour.index(0)
        tour = tour[start_index:] + tour[:start_index]
    tour.append(0)  # complete the cycle
    return tour

# Creating the biconnected subgraph
nodes = list(cities.keys())
biconnected_graph = build_biconnected_subgraph(nodes, edges)

# Extracting the tour
tour = find_tour(biconnected_graph)
distance, max_distance = 0, 0
for i in range(1, len(tour)):
    dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    distance += dist
    max_distance = max(max_dist, dist)

print(f"Tour: {tour}")
print(f"Total travel cost: {distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")