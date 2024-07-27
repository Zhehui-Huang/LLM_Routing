import numpy as np
import random

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Function to compute Euclidean distance
def distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Initializes tours starting at assigned depots
def initialize_tours(depots, remaining_cities):
    tours = { depot: [depot] for depot in depots }
    city_assignment = random.sample(remaining_cities, len(remaining_cities))
    split_size = len(city_assignment) // len(depots)
    for index, depot in enumerate(depots):
        start_index = index * split_size
        if index == len(depots) - 1:
            tours[depot] += city_assignment[start_index:]
        else:
            tours[depot] += city_assignment[start_index:start_index + split_size]
        tours[depot].append(depot)  # Ensure tour returns to the start
    return tours

# Calculate the travel cost for each tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

depots = [0, 1, 2, 3, 4, 5, 6, 7]
remaining_cities = [i for i in range(8, 23)]

# Generate initial tours
tours = initialize_tours(depots, remaining_cities)

# Calculate costs
total_global_cost = 0
for robot_id, tour in tours.items():
    tour_cost = calculate_tour_cost(tour)
    total_global_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_global_cost, 2)}")