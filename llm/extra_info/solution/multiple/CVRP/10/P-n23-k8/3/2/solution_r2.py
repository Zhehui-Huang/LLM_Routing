import numpy as is_np
from scipy.spatial.distance import cdist
import itertools

# City locations and demands
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

# Compute the distance matrix
distance_matrix = cdist(coordinates, coordinates)

# Helper functions to find tours and calculate costs
def find_tour(demands, capacity, distance_matrix):
    tour = [depot]
    cur_city = depot
    used_capacity = 0

    while True:
        next_city = None
        min_distance = np.inf

        for city in range(1, len(demands)):  # Skip the depot
            if city not in tour and demands[city] > 0 and (used_capacity + demands[city] <= capacity):
                dist = distance_matrix[cur_city, city]
                if dist < min_distance:
                    min_distance = dist
                    next_city = city

        if next_city is None:
            break
        
        tour.append(next_city)
        used_capacity += demands[next_city]
        demands[next_city] = 0  # Fulfill the demand
        cur_city = next_city

    tour.append(depot)  # Return to depot
    return tour

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Assign robots to generate tours and distribute demands
tours = []
total_travel_cost = 0

for _ in range(num_robots):
    if all(d == 0 for d in demands[1:]):  # Check if all demands are fulfilled
        break
    demands_copy = demands.copy()
    tour = find_tour(demands_copy, robot_capacity, distance_matrix)
    tours.append(tour)
    demands = demands_copy[:]  # Update demands

# Calculate and display results
for i, tour in enumerate(tours):
    if len(tour) > 2:  # More than just depot to depot
        cost = calculate_tour_cost(tour, distance_matrix)
        total_travel_cost += cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")