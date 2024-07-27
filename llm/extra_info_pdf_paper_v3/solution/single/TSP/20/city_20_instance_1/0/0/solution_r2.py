import math
import numpy as np

# Coordinates of cities
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

# Calculate euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Fill distance matrix
num_cities = len(cities)
distance_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Nearest Neighbor heuristic to provide a tour starting from the depot city
def nearest_neighbor_tour(start_city):
    unvisited = set(range(num_cities))
    current_city = start_city
    tour = [current_city]
    unvisited.remove(current_city)

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_bases

    tour.append(start_city)  # Return to the start city
    return tour

# Calculate the total cost of the given tour
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Get the tour and the cost
tour = nearest_neighbor_tour(0)
total_cost = calculate_tour_cost(tour)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)