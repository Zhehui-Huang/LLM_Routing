import math
import networkx as nx

# Distance calculator using Euclidean distance
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Define the cities and their locations
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Create a complete graph from the cities and their respective distances
G = nx.complete_graph(len(cities))
for i, j in G.edges:
    G[i][j]['weight'] = calculate_distance(cities[i], cities[j])

# Compute a minimum spanning tree to ensure connectivity
mst = nx.minimum_spanning_tree(G)

# Find an Eulerian tour and convert it into a TSP tour using shortcuts
eulerian_circuit = list(nx.eulerian_circuit(nx.MultiGraph(mst), source=0))
tsp_tour = []

visited = set()
for u, v in eulerian_circuit:
    if v not in visited:
        tsp_tour.append(v)
        visited.add(v)

# Include returning to the starting node to make it a complete tour
tsp_tour.append(tsp_tour[0])

# Compute the travel cost and the maximum distance
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(tsp_tour[:-1], tsp_tour[1:]))
max_distance = max(G[u][v]['weight'] for u, v in zip(tsp_tour[:-1], tsp_tour[1:]))

# Output the results
print("Tour:", tsp_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)