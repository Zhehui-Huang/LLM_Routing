import math
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Define the cities coordinates
cities_coords = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Compute the distance matrix
dist_matrix = distance_matrix(cities_coords, cities_calls)

# Calculate Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix))
mst_matrix = mst_matrix.toarray().astype(float)

# Function to get the tour from the MST (Depth-First Search)
def get_mst_tour(start, visited, graph):
    path = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            for neighbor in reversed(range(len(graph))):
                if graph[node][neighbor] != 0 and neighbor not in visited:
                    stack.append(neighbor)
    return path

# Generate the tour from the MST
visited = set()
tour = get_mst_tour(0, visited, mst_matrix)
tour.append(0)  # back to the depot

# Calculate the maximum distance and total cost in the tour
total_travel_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    city1 = tour[i]
    city2 = tour[i + 1]
    curr_distance = dist_matrix[city1, city2]
    total_travel_cost += curr_distance
    max_distance = max(max_distance, curr_distance)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")