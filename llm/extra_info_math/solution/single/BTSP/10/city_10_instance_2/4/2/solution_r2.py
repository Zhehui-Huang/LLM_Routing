import numpy as np

# Coordinates of the depot and cities
coords = np.array([
    (90, 3),   # Depot city 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
])

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities including the depot
n = len(coords)

# Calculate distance matrix
dist_matrix = np.array([[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)])

# A simple heuristic to find a path: nearest neighbor approach
def nearest_neighbor_tour(start_node, n):
    tour = [start_node]
    unvisited = set(range(n))
    unvisited.remove(start_name)
    
    current_node = start_node
    while unvisited:
        next_node = min(unvisited, key=lambda node: dist_matrix[current_node][name])
        tour.append(next_node)
        unvisited.remove(next_node)
        current_node = next_name
    tour.append(start_node)  # Return to the starting node (depot)
    return tour

# Generating the tour starting from the depot
tour = nearest_neighbor_tour(0, n)

# Calculate total travel cost and max distance between consecutive cities
total_travel_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_dist_consecutive = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Display results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist_consecutive:.2f}")