import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Definition of cities' coordinates
coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Helper function to calculate Euclidean distance
def calc_distance(city1, city2):
    return euclidean(coords[city1], coords[city2])

# Simple split approach (equal partitioning for simplicity)
def assign_cities():
    num_cities = len(coords) - 2  # minus two depots
    each_robot_cities = num_cities // 2
    return list(range(2, 2 + each_robot_cities)), list(range(2 + each_robot_cities, 19))

# Helper function to create a route
def create_route(depot, cities):
    return [depot] + cities + [depot]

# Evaluate route cost
def evaluate_route(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += calc_distance(route[i], route[i + 1])
    return cost

# Main function to generate and evaluate routes
def main():
    # Assign cities to each robot
    robot0_cities, robot1_cities = assign_cities()
    
    # Basic nearest neighbor approach to order cities (not optimal)
    robot0_cities = sorted(robot0_cities, key=lambda x: calc_distance(0, x))
    robot1_cities = sorted(robot1_cities, key=lambda x: calc_distance(1, x))
    
    # Create routes
    robot0_route = create_route(0, robot0_cities)
    robot1_route = create_route(1, robot1_cities)
    
    # Evaluate costs
    robot0_cost = evaluate_route(robot0_route)
    robot1_cost = evaluate_route(robot1_route)
    
    # Print the output as required
    print(f'Robot 0 Tour: {robot0_route}')
    print(f'Robot 0 Total Travel Cost: {robot0_cost}')
    print(f'Robot 1 Tour: {robot1_route}')
    print(f'Robot 1 Total Travel Cost: {robot1_cost}')
    print(f'Overall Total Travel Cost: {robot0_cost + robot1_cost}')

# Execute execution of the main function
main()