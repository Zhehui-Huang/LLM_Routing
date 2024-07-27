import math
import networkx as nx
from itertools import combinations

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Compute Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)

# Create a complete graph
def create_graph(cities):
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

# Get the degree of all vertices
def get_odd_vertex(G):
    odds = []
    for i in G.nodes():
        if G.degree(i) % 2 != 0:
            odds.append(i)
    return odds

# Match the minimum weight
def min_weight_match(G, odds):
    minimum = float('inf')
    min_pair = []
    pairings = combinations(odds, 2)
    for pair in pairings:
        weight = nx.dijkstra_path_length(G, pair[0], pair[1])
        if weight < minimum:
            minimum = weight
            min_pair = pair
    return min_pair

# Christofides Algorithm
def christofides_algorithm(G):
    # Step 1: MST T
    T = nx.minimum_spanning_tree(G)
    # Step 2: Vertices with odd degree
    odds = get_odd_vertex(T)
    # Step 3: Minimum weight matching
    while odds:
        u, v = min_weight_match(G, odds)
        T.add_edge(u, v, weight=G[u][v]['weight'])
        odds.remove(u)
        odds.remove(v)
    # Step 5: Eulerian circuit
    eulerian = list(nx.eulerian_circuit(T, source=0))
    path = []
    visited = set()
    for u, v in eulerian:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(0)
    # Step 6: Calculate the total weight/cost
    cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
    return path, cost

# Create graph and apply algorithm
G = create_graph(cities)
tour, total_cost = christofides_algorithm(G)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)