import numpy as np
import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Coordinates array including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Number of cities (excluding depot)
num_cities = len(coordinates) - 1  
# Number of robots
num_robots = 8 

# Create a simple initial partition of cities to robots
cities_per_robot = num_cities // num_robots
assignment = []
start_index = 1

for i in range(num_robots):
    if i < num_robots - 1:
        assignment.append(list(range(start_index, start_index + cities_per_robot)))
    else:
        # Last robot gets any remaining cities
        assignment.append(list(range(start_index, num_cities + 1)))
    start_index += cities_per_robot

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

# Generate initial tours for each robot starting and ending at the depot
initial_tours = []
for robot_cities in assignment:
    tour = [0] + robot_cities + [0]
    initial_tours.append(tour)

# Calculate initial costs
costs = [calculate_tour_cost(tour) for tour in initial_tours]
max_cost = max(costs)

# Function to print the tours in the desired output format
def print_tours(tours, costs):
    for i, tour in enumerate(tours):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {costs[i]}")
    print(f"Maximum Travel Cost: {max(costs)}")

# Displaying the initial result
print_tours(initial_tours, costs)