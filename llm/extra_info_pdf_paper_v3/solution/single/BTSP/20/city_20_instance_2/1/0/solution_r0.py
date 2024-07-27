import math
import sys

# Distances between all pairs will be stored here
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_all_distances(cities):
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

def find_tour(cities):
    num_cities = len(cities)
    distances = calculate_all_distances(cities)
    unvisited = set(range(1, num_cities))
    tour = [0]  # Start at the depot
    current_city = 0
    max_distance = 0

    # Construct the tour
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        new_dist = distances[current_city][next_city]
        max_distance = max(max_distance, new_dist)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    # Close the tour by returning to the depot
    tour.append(0)
    max_distance = max(max_distance, distances[current_city][0])

    # Calculating total travel cost
    total_travel_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

    return tour, total_travel_cost, max_distance

# Define the cities coordinates
# Coordinates are given as (x, y) tuples
cities = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

tour, total_cost, max_distance = find_tour(cities)

output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

output