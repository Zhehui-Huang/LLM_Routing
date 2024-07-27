from math import sqrt
import networkx as nx

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate complete graph
G = nx.complete_graph(len(cities))  # Complete graph with nodes from 0 to 9
for i in cities:
    for j in cities:
        if i != j:
            G[i][j]['weight'] = euclidean_distance(i, j)

# Heuristic Solution for the problem based on Minimum Spanning Tree and shortcuts
mst = nx.minimum_spanning_tree(G)
tour = list(nx.approximation.traveling_salesman_problem(G, weight='weight', cycle=True))

max_distance = max(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")