import math
from typing import List, Tuple

# Coordinates of the cities
coordinates = [
    (26, 60),  # Depot city 0
    (73, 84),
    (89, 36),
    (15, 0),
    (11, 10),
    (69, 22),
    (28, 11),
    (70, 2),
    (47, 50),
    (60, 29),
    (29, 26),
    (85, 68),
    (60, 1),
    (71, 73),
    (82, 47),
    (19, 25),
    (75, 9),
    (52, 54),
    (64, 72),
    (14, 89)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate distance matrix
num_cities = len(coordinates)
distance_matrix = [[0.0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Heuristic for TSP: Nearest Neighbor Algorithm
def nearest_neighbor_tour(start_city: int) -> Tuple[List[int], float]:
    unvisited = set(range(num_cities))
    tour = []
    current_city = start_city
    total_cost = 0.0

    unvisited.remove(current_city)
    tour.append(current_city)

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        total_cost += distance_matrix[current_city][next_city]
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(current_city)

    # Return to the depot city
    total_cost += distance_matrix[current_city][start_city]
    tour.append(start_city)

    return tour, total_cost

# Find the shortest tour starting and ending at the depot city 0
tour, total_cost = nearest_neighbor_tour(0)

# Output
print("Tour:", tour)
print("Total travel cost:", round(total_"cost, 2))