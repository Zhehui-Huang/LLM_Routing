import numpy as np
from math import sqrt

# Define the coordinates of each city
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate distances matrix
def calc_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance = sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance
    return distance_matrix

def greedy_tour(start_index, cities, num_cities_per_robot):
    remaining_cities = set(range(len(cities))) - {start_index}
    tour = [start_index]
    current_city = start_index
    
    while len(tour) < num_cities_per_robot:
        next_city = min(remaining_cities, key=lambda x: distance_matrix[current_city][x])
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
        
    return tour

# Configuration
num_robots = 8
distance_matrix = calc_distance_matrix(cities)

# Calculate number of cities per robot and assign cities to each robot
cities_per_robot = len(cities) // num_robots
extra_cities = len(cities) % num_robots

tours = []
robot_start_indices = range(0, num_robots * cities_per_robot, cities_per_robot)

# Generate tours
total_cost = 0
for idx, start_idx in enumerate(robot_start_indices):
    num_cities_for_robot = cities_per_robot
    if idx < extra_cities:
        num_cities_for_robot += 1
    tour = greedy_tour(start_idx, cities, num_cities_for_robot)
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    tours.append((tour, tour_cost))
    total_cost += tour_cost

# Print the outputs
for i, (tour, cost) in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")