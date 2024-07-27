import numpy as np
import random
from math import sqrt

# Provided City Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1_idx, city2_idx):
    c1, c2 = cities[city1_idx], cities[city2_idx]
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculating distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(i, j)
        else:
            distance_matrix[i][j] = float('inf')  # no self loop

def nearest_neighbour_solution(start_point):
    tour = [start_point]
    unvisited = set(cities.keys()) - {start_point}

    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distance_matrix[last][x])
        unvisited.remove(next_city)
        tour.append(next_city)
    
    tour.append(start_point)  # return to the depot
    return tour

# Each robot starts a tour from its respective depot
robot_0_tour = nearest_neighbour_solution(0)
robot_1_tour = nearest_neighbour_solution(1)

# Calculate the total distance for each robot's tour
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

robot_0_cost = calculate_tour_cost(robot_0_tour)
robot_1_cost = calculate_tour_cost(robot_1_tour)
total_cost = robot_0_cost + robot_1_cost

# Print Results
print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", robot_0_cost)

print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", robot_1_cost)

print("Overall Total Travel Cost:", total_cost)