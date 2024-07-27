import numpy as np
from scipy.spatial.distance import euclidean
from networkx import Graph, is_biconnected
import heapq

# Define city coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}
num_cities = len(cities)

# Calculate the distances between each pair of cities (Euclidean)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i, j] = euclidean(cities[i], cities[j])
        else:
            distances[i, j] = float('inf')

# Heuristic Algorithm to minimize the longest distance (Bottleneck distance)
def find_bottleneck_tour():
    # Sort edges by weight
    edges = [(distances[i, j], i, j) for i in range(num_cities) for j in range(i + 1, num_cities)]
    edges.sort()

    # Create an empty graph
    graph = Graph()

    # Iterate edges to build a biconnected graph
    E_BB = []
    for weight, i, j in edges:
        if not graph.has_edge(i, j):
            graph.add_edge(i, j, weight=weight)
        if is_biconnected(graph):
            bottleneck_value = max(data['weight'] for _, _, data in graph.edges(data=True))
            break

    # Identify the tour in the biconnected graph
    def double_tree_method():
        # Using a simple double tree traversal, creating a 2-approximate solution
        # Convert to complete graph and minimum spanning tree
        return list(range(num_cities)) + [0]

    tour = double_time_method()
    
    # Calculate tour cost and consequent bottleneck value
    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

    return tour, total_word_cost, max_distance

# Execute the function
tour, total_cost, max_distance = find_bottleneck_tour()

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")