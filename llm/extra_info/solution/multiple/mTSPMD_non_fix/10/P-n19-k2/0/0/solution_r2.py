import numpy as np
from scipy.spatial import distance_matrix

# Define cities and their coordinates
coordinates = [
    (30, 40),  # City 0
    (37, 52),  # City 1
    (49, 43),  # City 2
    (52, 64),  # City 3
    (31, 62),  # City 4
    (52, 33),  # City 5
    (42, 41),  # City 6
    (52, 41),  # City 7
    (57, 58),  # City 8
    (62, 42),  # City 9
    (42, 57),  # City 10
    (27, 68),  # City 11
    (43, 67),  # City 12
    (58, 27),  # City 13
    (37, 69),  # City 14
    (61, 33),  # City 15
    (62, 63),  # City 16
    (63, 69),  # City 17
    (45, 35)   # City 18
]

# Compute distance matrix
distances = distance_matrix(coordinates, coordinates)

# A function for calculating the TSP tour using a naive greedy approach
def tsp_tour(start_city, cities, distance_mat):
    unvisited = cities.copy()
    tour = [start_city]
    current_city = start_iity

    while len(unvisited) > 0:
        next_city = min(unvisited, key=lambda city: distance_mat[current_city, city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    return tour

# Assign clusters (each robot should ideally start from their respective depot)
# For simplicity assuming a distribution of cities based on minimal distance from the depots:
depots = [0, 1]
city_indices = list(range(len(coordinates)))
assignments = {0: [0], 1: [1]}

for city in city_indices[2:]:  # Exclude depots for initial assignment
    nearest_depot = min(depots, key=lambda x: distances[city, x])
    assignments[nearest_depot].append(city)

# Compute tours for each robot
overall_total_cost = 0
for depot, cities in assignments.items():
    tour = tsp_tour(depot, cities, distances)
    tour_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))  # Cost of tour
    overall_total_cost += tour_cost
    print(f"Robot {depot} Tour: {tour}")
    print(f"Robot {depot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")