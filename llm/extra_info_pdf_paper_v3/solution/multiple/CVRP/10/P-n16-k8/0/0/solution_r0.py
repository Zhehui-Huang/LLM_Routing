import numpy as np
import math
from random import sample

# Define coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
               (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
capacity = 35 
num_robots = 8

def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Initialize tours for robots
tours = [[] for _ in range(num_robots)]

# Assign cities to robots using a greedy heuristic based on demands and robot capacity
current_capacities = [0] * num_robots
for city in range(1, len(coordinates)):  # start from 1 to skip the depot
    assigned = False
    city_demand = demands[city]
    for robot in range(num_robots):
        if current_capacities[robot] + city_demand <= capacity:
            if not tours[robot]:
                tours[robot].append(0)
            tours[robot].append(city)
            current_capacities[robot] += city_demand
            assigned = True
            break
    if not assigned:
        # if city not assigned it means we ran out of capacity in all existing routes, start a new robot route if possible
        for robot in range(num_robots):
            if not tours[robot]:
                tours[robot].append(0)
                tours[robot].append(city)
                current_capacities[robot] += city_demand
                tours[robot].append(0)
                break

# Ensure every tour ends back at the depot
for robot in range(num_robots):
    if tours[robot]:
        tours[robot].append(0)

# Calculate cost for each tour
robot_costs = [calculate_tour_cost(tour) for tour in tours if tour]

# Output results
overall_total_cost = sum(robot_costs)
for robot, tour in enumerate(tours):
    if tour:
        cost = calculate_tour_cost(tour)
        print(f'Robot {robot} Tour: {tour}')
        print(f'Robot {robot} Total Travel Cost: {cost}')
print(f'Overall Total Travel Cost: {overall_total_cost}')