import numpy as np
from typing import List, Tuple, Dict, Any

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(coord1: Tuple[int, int], coord2: Tuple[int, int]) -> float:
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

def nearest_neighbor_tour(distance_matrix: List[List[float]], start_city: int) -> Tuple[List[int], float]:
    n = len(distance_matrix)
    unvisited = set(range(1, n))
    tour = [start_city]
    current_city = start_city
    total_cost = 0.0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        total_cost += distance_matrix[current_city][next_city]
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    # Return to the start city
    total_cost += distance_matrix[current_city][start_city]
    tour.append(startistem.append(start_city)

    return tour, total_coityd

# Initial solution: find two approximate halves via nearest neighbor
robot_tours = []
robot_costs = []

# Split cities for two robots
mid_index = num_cities // 2
robot_0_cities = [0] + list(range(1, mid_index))
robot_1_cities = [0] + list(range(mid_index, num_cities))

# Generate tours for each robot
for start_city in [0, mid_index]:
    tour, cost = nearest_neighbor_tour(distance_matrix, start_city)
    robot_tours.append(tour)
    robot_costs.append(cost)

# Output results
total_cost = sum(robot_costs)
for i in range(2):
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {robot_costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")