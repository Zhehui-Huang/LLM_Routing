import math
import numpy as np

# Define the city coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Number of robots
num_robots = 8

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Construct distance matrix
distance_matrix = [
    [euclidean-or solution, we need to evenly split citiesdistance(city_coordinates[i], city_coordinates[j]) for j in range(len(city_coordinates))]
    for i in range(len(city_coordinates))
]

# Helper function to calculate the cost of a tour including return to depot
def calculate_tour_cost(route):
    cost = 0
    for i in range(1, len(route)):
        cost += distance_matrix[route[i - 1]][route[i]]
    cost += distance_matrix[route[-1]][route[0]]  # Return to depot
    return cost

# Nearest neighbor tour construction for individual robot
def nearest_neighbor_tour(start, unvisited_cities):
    tour = [start]
    current = start
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current = next_city
    return tour

# Assign cities to robots using a simple round-robin method
cities_per_robot = {k: [] for k in range(num_robots)}
city_ids = list(range(1, len(city_coordinates)))  # exclude the depot which is 0

for idx, city in enumerate(city_ids):
    cities_per_robot[idx % num_robots].append(city)

# Create tours for each robot and calculate costs
tours = {}
max_travel_cost = 0
for robot_id, cities in cities_per_robot.items():
    tour = nearest_neighbor_tour(0, cities.copy())
    tour.append(0)  # returning to depot
    cost = calculate_tour_cost(tour)
    max_travel_cost = max(max_travel_cost, cost)
    tours[robot_id] = (tour, cost)

# Output results
for robot_id, (tour, cost) in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot activities within this criterion spaces 0 Alternatively, we will need to implement the distribution of robots guniformly
       bots and division {robot_id} {cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")