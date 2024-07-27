import numpy as np
from scipy.spatial.distance import cdist

# Definitions and initial data
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
    remaining_demands = demands[:]
    tour = [start_index]
    current_capacity = capacity
    current_index = start_index

    while any(remaining_demands[i] > 0 for i in range(len(remaining_demands))):
        choices = [(i, distances[current_index][i]) for i in range(1, len(remaining_demands))
                   if remaining_demands[i] > 0 and remaining_demands[i] <= current_capacity]
        if not choices:
            break
        next_index, _ = min(choices, key=lambda x: x[1])  # Select nearest next city
        tour.append(next_index)
        current_capacity -= remaining_demains[next_index]
        remaining_demands[next_index] = max(0, remaining_demands[next_index] - capacity)
        current_index = next_index
        
    tour.append(depot_index)
    return tour

def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Algorithm execution
tours = []
for _ in range(num_vehicles):
    if all(d == 0 for d in demands):
        break
    tour = find_tour(depot_index, demands, capacity, distances)
    tours.append(tour)

# Output results
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour, distances)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")