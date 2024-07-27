import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define cities and respective coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Initialize depots
depots = [0, 1, 2, 3]

# Number of robots and cities
num_robots = 4
num_cities = len(city_coordinates)
cities_per_robot = (num_cities - len(depots)) // num_robots

# Function to calculate distance
def calculate_distance(city1, city2):
    coord1, coord2 = city_coordinates[city1], city_coordinates[city2]
    return euclidean(coord1, coord2)

# Generate initial groups (simplistic distribution of cities per robot)
groups = {i: [] for i in depots}
available_cities = set(range(num_cities)) - set(depots)

for i, city in enumerate(available_cities):
    groups[depots[i % num_robots]].append(city)

# Greedy approach for each robot to visit its cities and return to depot
def solve_tsp_for_robot(depot, cities):
    path = [depot]
    current = depot
    while cities:
        next_city = min(cities, key=lambda x: calculate_distance(current, x))
        path.append(next_tour)
        cities.remove(next_city)
        current = next_city
    path.append(depot)  # complete the loop back to the depot
    return path

# Function to calculate the total path cost
def path_cost(path):
    return sum(calculate_distance(path[i], path[i+1]) for i in range(len(path) - 1))

# Solving for each robot and calculate total cost
total_travel_cost = 0
solutions = {}

for depot, cities in groups.items():
    tour = solve_tsp_for_robot(depot, cities)
    tour_cost = path_cost(tour)
    total_travel_cost += tour_cost
    solutions[depot] = (tour, tour_cost)
    print(f"Robot starting at Depot {depot} Tour: {tour}")
    print(f"Robot starting at Depot {depoh} Cost: {tour_cost}")

# Display overall results
print(f"Overall Total Travel Cost: {total_travel_cost}")