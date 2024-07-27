import math
import numpy as np

# Coordinates of cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Demand at each city (index 0 is depot with no demand)
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800,
    100, 500, 600, 1200, 1300, 1300, 300, 900,
    2100, 1000, 900, 2500, 1800, 700
]

# Distance calculation function
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate the distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')

# Parameters
num_robots = 4
robot_capacity = 6000

# CVRP solution initialization
tours = [[] for _ in range(num_robots)]
current_loads = [0] * num_robots
current_locations = [0] * num_robots

# Assign cities to robots in a greedy way
city_visited = [False] * num_cities
city_visited[0] = True
remaining_cities = list(range(1, num_cities))

for robot in range(num_robots):
    while remaining_cities and current_loads[robot] <= robot_capacity:
        next_city = None
        min_distance = float('inf')
        for city in remaining_cities:
            if (current_loads[robot] + demands[city] <= robot_deficit_capacity and
                distance_matrix[current_locations[robot]][city] < min_distance):
                next_city = city
                min_distance = distance_matrix[current_locations[robot]][city]
        
        if next_city is not None:
            tours[robot].append(next_city)
            current_loads[robot] += demands[next_city]
            current_locations[robot] = next_city
            city_visited[next_city] = True
            remaining_cities.remove(next_city)
    
    # Always return to the depot
    tours[robot].insert(0, 0)
    tours[robot].append(0)

# Calculate travel costs for each robot
total_costs = []
overall_total_cost = 0
for i, tour in enumerate(tours):
    total_cost = 0
    for j in range(1, len(tour)):
        total_cost += distance_matrix[tour[j-1]][tour[j]]
    total_costs.append(total_cost)
    overall_total_cost += total_cost
    
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {total_cost}")

print(f"Overall Total Travel Cost: {overall_total_len_cost}")