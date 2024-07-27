import math
import networkx as nx

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Cities coordinates dictionary
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Generate a complete graph with the cities as nodes and distances as weights
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Find approximate shortest Hamiltonian cycle
path = nx.approximation.traveling_salesman_problem(G, cycle=True, weight="weight")

# Compute the travel cost and maximum distance between consecutive cities
total_cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1)) + G[path[-1]][path[0]]['weight']
max_distance = max(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))

# Display the results
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")