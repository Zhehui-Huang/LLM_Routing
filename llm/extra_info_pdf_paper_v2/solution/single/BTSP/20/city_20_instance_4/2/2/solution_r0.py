import numpy as np
import itertools
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix

# Define city coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Compute Euclidean distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            dist_matrix[i][j] = float('inf')

# Apply MST to get a minimum spanning tree
mst = minimum_spanning_tree(csr_matrix(dist_matrix))

# Create graph squared of MST
def generate_graph_squared(mst):
    n = mst.shape[0]
    mat = mst.toarray()
    g_squared = (mat + mat.T) ** 2
    return csr_matrix(g_squared)

graph_squared = generate_graph_squared(mst)

# Function to attempt to form a Hamiltonian cycle
def nearest_neighbor_tour(graph_squared, start=0):
    n = graph_squared.shape[0]
    visited = set([start])
    tour = [start]
    current = start

    while len(visited) < n:
        next_city = np.argmin([graph_squared[current, j] if j not in visited else float('inf') for j in range(n)])
        visited.add(next_city)
        tour.append(next_city)
        current = next_city
    
    tour.append(start)  # Close the tour back to the starting point
    return tour

def calculate_tour_properties(tour):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = dist_matrix[tour[i-1], tour[i]]
        total_cost += distance
        max_distance = max(max_distance, distance)
    return total_cost, max_distance

# Generate the tour using nearest neighbor heuristic from graph squared
tour = nearest_neighbor_tour(graph_squared)
total_cost, max_distance = calculate_tour_properties(tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")