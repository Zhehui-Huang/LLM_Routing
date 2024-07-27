import math
from typing import List, Tuple

# Define the cities coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

def euclidean_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all pairwise distances
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

def nearest_neighbor_tour(start_city: int, distances: List[List[float]]) -> List[int]:
    n = len(distances)
    unvisited = set(range(n))
    unvisited.remove(start_city)
    tour = [start_city]

    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # Return to the start city to complete the tour
    return tour

def calc_tour_stats(tour: List[int], distances: List[List[float]]) -> Tuple[float, float]:
    total_cost = 0.0
    max_distance = 0.0

    for i in range(1, len(tour)):
        dist = distances[tour[i - 1]][tour[i]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    return total_cost, max_distance

# Calculate the tour
tour = nearest_neighbor_tour(0, distances)
total_cost, max_distance = calc_tour_stats(tour, distances)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")