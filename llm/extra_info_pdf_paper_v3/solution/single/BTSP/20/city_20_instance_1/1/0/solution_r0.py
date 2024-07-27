import math
from itertools import permutations

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of cities including the depot
cities = [
    (14, 77),  # Depot city 0
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# Create matrix of distances between each pair of cities
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic to find a more optimal path
def find_path():
    # Starting at depot city 0
    path = [0]
    unvisited = set(range(1, n))
    max_edge_length = 0
    
    current = 0
    while unvisited:
        next_city, edge_length = min(
            [(city, distance_matrix[current][city]) for city in unvisited], key=lambda x: x[1]
        )
        max_edge_length = max(max_edge_length, edge_length)
        path.append(next_city)
        current = next_city
        unvisited.remove(next_city)
        
    # Return to the depot
    final_leg = distance_matrix[current][0]
    path.append(0)
    max_edge_length = max(max_edge_length, final_leg)
    
    # Total travel cost
    total_cost = sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
    
    return path, total_cost, max_edge_length

# Finding the tour
tour_path, total_travel_cost, max_consecutive_distance = find_path()

# Output the results
print("Tour:", tour_path)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)