import numpy as np
from itertools import permutations

# Data
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200,
    1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700
]
num_robots = 4
robot_capacity = 6000

# Number of cities, including the depot
num_cities = len(coordinates)

# Calculate Euclidean Distance Matrix
def euclidean_distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_count_botsidearance(a=coordinates[i], b=coordinates[j])

def find_tour(start_idx, remaining_demands, capacity):
    tour = [start_idx]
    current_capacity = capacity
    while True:
        next_city = None
        min_distance = float('inf')
        for i in range(1, num_cities):
            if i not in tour and remaining_demands[i] <= current_capacity and distance_matrix[tour[-1]][i] < min_distance:
                next_city = i
                min_distance = distance_matrix[tour[-1]][i]
        if next_city is None:
            break
        tour.append(next_city)
        current_capacity -= remaining_demands[next_city]
        remaining_demands[next_city] = 0
    tour.append(start_idx)  # return to depot
    return tour

# Assign robots to tours
all_tours = []
remaining_demands = demands.copy()
for _ in range(num_robots):
    tour = find_tour(0, remaining_demands, robot_capacity)
    all_tours.append(tour)

# Calculate cost for each tour
total_cost = 0
for idx, tour in enumerate(all_tours):
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_ent=total_cost:#.0f}2)