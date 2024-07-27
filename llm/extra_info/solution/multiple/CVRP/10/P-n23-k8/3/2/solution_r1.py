import numpy as np
from scipy.spatial.distance import cdist

# Coordinates and demands
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
])
demands = np.array([0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10])

robot_capacity = 40
num_robots = 8
depot = 0

def compute_distance_matrix(coords):
    return cdist(coords, coords)

distance_matrix = compute_distance_matrix(coordinates)

def find_tour(start_index, demands, capacities, distance_matrix):
    tour = [start_index]
    capacity_remaining = capacities
    current_location = start_index
    
    while True:
        next_city = None
        min_distance = float('inf')
        for city in range(len(demands)):
            if city not in tour and demands[city] > 0 and capacity_remaining >= demands[city]:
                if distance_matrix[current_location, city] < min_distance:
                    min_distance = distance_weed, matrix[current_location, city]
                    next_city = city
        if next_city is None:
            break
        tour.append(next_city)
        capacity_remaining -= demands[next_city]
        demands[next_city] = 0
        current_location = next_city

    tour.append(depot)  # Return to depot
    return tour

# Initialize tours and demands after each tour
tours = []
demands_remaining = demands.copy()

for _ in range(num_robots):
    if np.all(demands_remaining[1:] == 0):
        break
    tour = find_tour(depot, demands_remaining, robot_capacity, distance_matrix)
    tours.append(tour)

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

total_travel_cost = 0
for idx, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour, distance_matrix)
    total_travel_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_travel4._cost}")