import numpy as np
import math
from itertools import permutations

# Define the coordinates for all cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of Robots and depot information 
num_robots = 8
depot = 0  # All robots start from city 0

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create a basic tour where every robot starts and ends at the depot
# Split the cities equally around robots (this won't be optimal)
city_indices = list(cities.keys())
city_indices.remove(depot)  # remove the depot city from the tour list

# Split cities amongst robots
cities_per_robot = len(city_indices) // num_robots
tours = []
all_tours_costs = []

# Creating tours loop for each robot
for i in range(num_robots):
    if i < num_robots - 1:
        tour = city_indices[i*cities_per_robot:(i+1)*cities_per_robot]
    else:
        tour = city_indices[i*cities_per_robot:]  # Take the rest of the cities for the last robot
    tour.insert(0, depot)  # Start at the depot
    if tour[-1] != depot:
        tour.append(depot)  # End at the depot
    
    tours.append(tour)

# Function to calculate the travel cost of the entire tour for a robot
def calculate_tour_cost(tour):
    total_cost = 0
    for j in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[j], tour[j+1])
    return total_cost

# Compute and display the tours and their costs
overall_total_cost = 0
for robot_id, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour)
    all_tours_costs.append(tour_cost)
    print(f'Robot {robot_id} Tour: {tour}')
    print(f'Robot {robot_id} Total Travel Cost: {tour_cost:.2f}\n')
    overall_total_cost += tour_cost

print(f'Overall Total Travel Cost: {overall_tour_cost:.2f}')