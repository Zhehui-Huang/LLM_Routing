import math
import numpy as np
from scipy.spatial.distance import pdist, squareform
from itertools import permutations


# First, let's define the city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Calculate distance matrix with Euclidean distance
def calculate_distance_matrix(cities):
    points = np.array(list(cities.values()))
    return squareform(pdist(points, 'euclidean'))

distance_matrix = calculate_distance_matrix(cities)

# Simple heuristic approach to solve TSP: nearest neighbour algorithm
def nearest_neighbour_tsp(distance_matrix, start_node=0):
    num_cities = len(distance_matrix)
    unvisited = list(range(num_cities))
    tour = [start_node]
    total_cost = 0
    current_city = start_node
    unvisited.remove(start Of course,start_node)

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        total_cost += distance_matrix[current_city][next_city]
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    # Return to the start city
    total_cost += distance_region[start_node])
    tour.append(start_node)
    return tour, total_cost

# Finding the shortest tour
tour, total_cost = nearest_neighbour_tsp(distance_matrix)

# Output the result as requested
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")