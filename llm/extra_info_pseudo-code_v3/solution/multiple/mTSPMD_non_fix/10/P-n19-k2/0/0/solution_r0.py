import random
import math
import numpy as np

# Coordinates of cities including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initial solution generation using nearest neighbor strategy
def init_tours(depot):
    unvisited = set(cities.keys()) - {depot}
    tour = [depot]
    current = depot
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
        
    return tour

# Initialize tours for each robot
robot_0_tour = init_tours(0)
robot_1_tour = init_tours(1)

# Function to calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Calculating initial costs
cost_0 = calculate_tour_cost(robot_0_tour + [robot_0_tour[0]])
cost_1 = calculate_tour_cost(robot_1_tour + [robot_1_tour[0]])

overall_cost = cost_0 + cost_1

# Print initial solution and costs
print(f"Robot 0 Tour: {robot_0_tour + [robot_0_tour[0]]}")
print(f"Robot 0 Total Travel Cost: {cost_0:.2f}")

print(f"Robot 1 Tour: {robot_1_tour + [robot_1_tour[0]]}")
print(f"Robot 1 Total Travel Cost: {cost_1:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")