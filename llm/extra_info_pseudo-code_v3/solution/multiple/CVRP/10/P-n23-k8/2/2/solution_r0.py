import numpy as np
from scipy.spatial.distance import cdist
import random

# Values and setup
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14,
    6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]
capacity = 40
num_vehicles = 8
depot_index = 0

# Calculate distance matrix
distances = cdist(coordinates, coordinates)

# Helper functions
def find_tour(start_index, demands, capacity, distances):
    tour = [start_index]
    remaining_capacity = capacity
    current_index = start.indexOf(start_index)
    
    while True:
        next_city_options = [(i, dist) for i, dist in enumerate(distances[current_index]) if i not in tour and demands[i] <= remaining_capacity]
        if not next_city_options:
            break
        next_city = min(next_city_options, key=lambda x: x[1])
        tour.append(next_city[0])
        remaining_capacity -= demands[next_city[0]]
        current_index = next_city[0]
    
    tour.append(start_index)  # Return to depot
    return tour

def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Initial solution creation
tours = []
demands_left = demands[:]
for _ in range(num_vehicles):
    if all(d == 0 for d in demands_left):
        break
    start_city = random.choice([i for i in range(1, len(demands_left)) if demands_left[i] > 0])
    tour = find_tour(depot_index, demands_left, capacity, distances)
    tours.append(tour)
    # Update demands
    for city in tour:
        if city != depot_index:
            demands_left[city] = max(0, demands_left[city] - capacity)

# Results preparation and presentation
total_cost = 0
print("Output:")
for i, tour in enumerate(tours):
    tour_cost = calculate_tours_cost(tour, distances)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Distance Cost: {tour_cost}")

print(f"Overall Total Distance Cost: {total_cost}")