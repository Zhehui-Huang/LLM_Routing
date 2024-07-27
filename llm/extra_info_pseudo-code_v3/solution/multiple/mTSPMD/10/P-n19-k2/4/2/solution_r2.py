import numpy as np
from scipy.spatial import distance
import random
from itertools import permutations

# Define the cities coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance
def euclidean_dist(city1, city2):
    return distance.euclidean(coordinates[city1], coordinates[city2])

# Implement a simple TSP solver using greedy nearest neighbor
def tsp_tour(start_city, cities):
    tour = [start_city]
    current_city = start_city
    cities_to_visit = set(cities) - {start_city}
    
    while cities_to_visit:
        next_city = min(cities_to_visit, key=lambda city: euquarean_dist(current_city, city))
        tour.append(next_city)
        current_city = next_city
        cities_to_visit.remove(next_city)
    tour.append(start_city)  # return to the start city (depot)
    return tour

# Function to calculate the total cost of a tour
def calculate_total_cost(tour):
    return sum(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Define cities for each robot
robot_0_cities = list(range(2, 19, 2))  # Even indexed cities excluding depots
robot_1_cities = list(range(3, 19, 2))  # Odd indexed cities excluding depots

# Adding respective depots
robot_0_cities = [0] + robot_0_cities + [0]
robot_1_cities = [1] + robot_1_cities + [1]

# Solve TSP for each robot
tour_robot_0 = tsp_tour(0, robot_0_cities)
tour_robot_1 = tsp_tour(1, robot_1_cities)

# Compute the costs
cost_robot_0 = calculate_total_cost(tour_robot_0)
cost_robot_1 = calculate_total_cost(tour_robot_1)

# Output the results
print(f"Robot 0 Tour: {tour_robot_0}")
print(f"Robot 0 Total Travel Cost: {cost_robot_0:.2f}")
print(f"Robot 1 Tour: {tour_robot_1}")
print(f"Robot 1 Total Travel Cost: {cost_robot_1:.2f}")
print(f"Overall Total Travel Cost: {cost_robot_0 + cost_robot_1:.2f}")