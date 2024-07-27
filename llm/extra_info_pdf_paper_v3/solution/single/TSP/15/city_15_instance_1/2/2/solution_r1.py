import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def find_shortest_path_tour(cities):
    G = create_graph(cities)
    mst = nx.minimum_spanning_tree(G)
    odd_vertices = [v for v, deg in mst.degree if deg % 2 == 1]
    minimum_perfect_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_vertices), maxcardinality=True)
    augmented_mst = mst.copy()
    augmented_mst.add_edges_from(minimum_perfect_matching)
    eulerian = list(nx.eulerian_circuit(nx.eulerize(augmented_mst), source=0))
    
    path = []
    visited = set()
    cost = 0
    for u, v in eulerian:
        if u not in visited:
            path.append(u)
            visited.add(u)
        next_cost = G[u][v]['weight']
        cost += next_cost
    if path[0] != path[-1]:
        path.append(path[0])
        cost += G[path[-1]][path[0]]['weight']
    
    return path, cost

# Assume cities coordinates are given as in the problem statement
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate the tour and the total travel cost
tour, total_cost = find_shortest_path_tour(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))