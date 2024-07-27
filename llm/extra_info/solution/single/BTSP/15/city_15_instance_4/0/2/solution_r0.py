import math
from typing import List, Tuple

def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_and_max_distance(tour: List[int], coordinates: List[Tuple[int, int]]) -> Tuple[float, float]:
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

# Coordinates of cities including the depot
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# A simple approach: a greedy nearest neighbor algorithm starting from the depot
def greedy_tsp(coordinates: List[Tuple[int, int]]) -> List[int]:
    n = len(coordinates)
    unvisited = set(range(1, n))
    tour = [0]
    current_city = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(coordinates[current_city], coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(0)
    return tour

# Compute the tour using the greedy approach
tour = greedy_tsp(coordinates)

# Calculate total travel cost and maximum distance between consecutive cities
total_cost, max_dist_consecutive = calculate_total_and_max_distance(tour, coordinates)

output = f"Tour: {tour}\nTotal travel cost: {total_cost:.2f}\nMaximum distance between consecutive cities: {max_dist_consecutive:.2f}"
print(output)