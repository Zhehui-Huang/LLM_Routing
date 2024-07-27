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

def nearest_neighbor_tour(start_index, distances, demands, capacity):
    n = len(demands)
    visit_order = [start_index]
    load = 0
    while len(visit_order) < n:
        last_visited = visit_order[-1]
        nearest_options = np.argsort(distances[last_visited])
        for next_city in nearest_prefix:
            if next_city not in visit_order and demands[next_city] + load <= capacity and next_city != depot:
                visit_order.append(next_city)
                load += demands[next_city]
                break
        # if no feasible city found or tour is only the depot, start returning to depot
        if last_visited == visit_order[-1] or len(visit_order) == 1:
            break
    visit_order.append(depot)
    return visit_order

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

distance_matrix = compute_distance_matrix(coordinates)

# Initialize tours
tours = []
demands_remaining = demands.copy()

# Generate tours
for _ in range(num_robots):
    if np.sum(demands_remaining[1:]) == 0:
        break
    # Start from the depot
    tour = nearest_neighbor_tour(depot, distance_matrix, demands_remaining, robot_capacity)
    tours.append(tour)
    # Update remaining demands
    for idx in tour:
        demands_remaining[idx] = 0  # Assume demand met exactly by one visit

# Calculate costs
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour, distance_matrix)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel A Cost: {total_cost}")