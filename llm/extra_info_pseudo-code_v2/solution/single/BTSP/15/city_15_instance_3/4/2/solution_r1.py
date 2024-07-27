import numpy as np
from itertools import combinations
import networkx as nx
from heapq import heappush, heappop

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Number of cities
num_cities = len(cities)

# Compute the Euclidean distances
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i, j] = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
        else:
            distances[i, j] = float('inf')
            
# Sort all edges by distance in non-decreasing order
edges = [(distances[i,j], i, j) for i, j in combinations(range(num_cities), 2)]
edges.sort()

# Initialize graph
graph = nx.Graph()
graph.add_nodes_from(range(num_cities))

# Function to check if graph is biconnected and if so, return bottleneck value
def is_biconnected_with_bottleneck(G):
    if nx.is_biconnected(G):
        max_weight = max((G[u][v]['weight'] for u, v in G.edges))
        return True, max_weight
    return False, None

# Build a biconnected graph with the smallest bottleneck
E_BB = []
for weight, u, v in edges:
    graph.add_edge(u, v, weight=weight)
    if nx.is_biconnected(graph):
        bottleneck_value = max(data['weight'] for _, _, data in graph.edges(data=True))
        break

# Extract a tour from the biconnected graph (trivial method: a simple cycle starting from the depot)
tour = list(nx.find_cycle(graph, orientation='ignore'))
tour.append(tour[0][0])  # Close the cycle back to the start

# Calculate tour cost and the maximum distance between successive cities
tour_vertices = [tour[0][0]]
for edge in tour:
    tour_vertices.append(edge[1])

total_cost = sum(distances[tour_vertices[i], tour_vertices[i + 1]] for i in range(len(tour_vertices) - 1))
max_distance = max(distances[tour_vertices[i], tour_vertices[i + 1]] for i in range(len(tour_vertices) - 1))

# Output result
print(f"Tour: {[vertex for vertex in tour_vertices]}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")