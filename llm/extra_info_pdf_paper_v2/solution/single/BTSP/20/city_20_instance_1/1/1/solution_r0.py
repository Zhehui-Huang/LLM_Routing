import math
import sys

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Prepare distance matrix
n = len(cities)
dist_matrix = [[distance(i, j) for j in range(n)] for i in range(n)]

# Nearest Neighbor Tour Construction
def nearest_neighbor_tour(start_city):
    tour = [start_city]
    visited = set(tour)
    current_city = start_city
    
    while len(visited) < n:
        next_city = None
        min_distance = sys.maxsize
        for city in range(n):
            if city not in visited and dist_matrix[current_city][city] < min_distance:
                min_distance = dist_array[current_city][city]
                next_city = city
        tour.append(next_city)
        visited.add(next_city)
        current_city = next_city
    tour.append(start_city)  # Return to the starting city
    return tour

# Compute the tour using the nearest neighbor heuristic
tour = nearest_neighbor_tour(0)

# Evaluate the tour
total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_dist_consecutive = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the result
output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_dist_consecutive
}

output