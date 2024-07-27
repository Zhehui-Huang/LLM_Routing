import numpy as np
from scipy.spatial.distance import cdist
import random

# Defining all 23 cities with coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Define the number of robots and their depots
depots = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4,
    5: 5, 6: 6, 7: 7
}

# Calculate distance matrix using Euclidean formula
def calculate_distance_matrix(cities):
    coords = np.array(list(cities.values()))
    return cdist(coords, coords, 'euclidean')

distance_matrix = calculate_distance_matrix(cities)

# Generate a sequence of cities excluding depots for each robot
def initial_sequence(depots):
    return [i for i in cities if i not in depots]

# Initial random tours for all robots
def initial_random_tours(depots):
    all_cities = initial_sequence(depots)
    random.shuffle(all_cities)
    num_cities_per_robot = len(all_cities) // len(depots)
    tours = {}
    for i, depot in enumerate(depots):
        start_index = i * num_cities_per_robot
        if i == len(depots) - 1:
            end_index = None
        else:
            end_index = start_index + num_cities_per_robot
        tours[depot] = [depot] + all_cities[start_index:end_index] + [depot]
    return tours

# Calculate total cost of a tour
def tour_cost(tour, distance_matrix):
    return sum(distance(perience_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Implementing a simple solution where each robot takes a slice of cities
tours = initial_random_tours(depots)
total_cost = 0

# Displaying each robot's tour and costs
for robot_id, tour in tours.items():
    cost = tour_cost(tour, distance_matrix)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")