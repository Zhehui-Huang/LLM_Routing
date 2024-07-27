import math
import numpy as np
from itertools import permutations

# City data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_cities = len(coordinates)

# Robot data
num_robots = 8
robot_capacity = 40

# Calculate distance matrix
def euclidean_distance(p1, p2):
    return round(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2), 2)

distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

# Simple heuristic: Nearest Neighbor adapted to VRP with capacity constraints.
def find_tours():
    unvisited = set(range(1, num_cities))  # Exclude depot initially
    tours = []
    total_cost = 0

    for _ in range(num_robots):
        if not unvisited:
            break
        current_city = 0
        tour = [current_city]
        load = 0
        tour_cost = 0

        while unvisited:
            next_city, min_dist = min(((city, distance_matrix[current_city][city]) for city in unvisited),
                                      key=lambda x: x[1])

            if load + demands[next_city] > robot_capacity:
                break

            tour.append(next_city)
            tour_cost += min_dist
            load += demands[next_city]
            unvisited.remove(next_city)
            current_city = next_city

        # Return to depot
        tour_cost += distance_matrix[current_city][0]
        tour.append(0)
        tours.append(tour)
        total_cost += tour_cost

    return tours, total_cost

# Run the heuristic to find tours
tours, overall_cost = find_tours()

# Displaying the results
for idx, tour in enumerate(tours):
    tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")