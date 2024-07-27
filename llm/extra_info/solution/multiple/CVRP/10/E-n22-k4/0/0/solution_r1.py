import numpy as np
from scipy.spatial import distance_matrix
from collections import defaultdict, deque

# Coordinates and demands
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
               (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
               (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
               (164, 193), (129, 189), (155, 185), (139, 182)]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200,
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Number of robots and their capacity
num_robots = 4
robot_capacity = 6000

# Calculate the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Assign cities to robots based on capacity
city_indices = list(range(1, len(coordinates)))  # exclude the depot city 0
city_demand_pairs = sorted(zip(city_indices, demands[1:]), key=lambda x: x[1], reverse=True)

assignments = defaultdict(list)
capacities = defaultdict(int)
for city, demand in city_demand_pairs:
    for robot in range(num_robots):
        if capacities[robot] + demand <= robot_capacity:
            assignments[robot].append(city)
            capacities[robot] += demand
            break
    else:
        raise Exception("No robot can accommodate the demand at city {} with demand {}.".format(city, demand))

# Function to calculate a greedy TSP route
def greedy_tsp(cities, dist_matrix, start_city=0):
    path = [start_city]
    current_city = start_city
    remaining_cities = set(cities)
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: dist_matrix[current_city][x])
        path.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    
    path.append(start_city)
    return path

# Calculate route for each robot
total_cost = 0
for robot, cities in assignments.items():
    tour = greedy_tsp(cities, dist_matrix)
    tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_whole_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")