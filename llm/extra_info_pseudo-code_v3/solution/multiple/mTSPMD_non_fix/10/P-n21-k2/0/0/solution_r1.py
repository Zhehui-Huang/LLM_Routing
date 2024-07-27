import math
import numpy as np
import random

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Define depots
depots = [0, 1]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to create the initial tour using the nearest neighbor search
def nearest_neighbor_tour(depot, cities_list):
    tour = [depot]
    current = depot
    cities_list = cities_list.copy()
    while cities_list:
        next_city = min(cities_list, key=lambda x: euclidean_distance(current, x))
        tour.append(next_city)
        cities_list.remove(next_city)
        current = next_city
    return tour

# Applying the NNS heuristic algorithm
non_depot_cities = list(set(cities.keys()) - set(depots))

# Randomly assign non-depot cities to two depots initially
split = len(non_depot_cities) // 2
assigned_cities = [non_depot_cities[:split], non_depot_cities[split:]]

# Generate starting tours for each robot
tours = [nearest_neighbor_tour(depots[i], assigned_cities[i]) for i in range(2)]

# Function to calculate the cost of tours
def tour_cost(tours):
    cost_sum = 0
    robot_costs = []
    for tour in tours:
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        robot_costs.append(cost)
        cost_sum += cost
    return cost_sum, robot_costs

# Define function to output the results
def output_solution(tours, costs, total_cost):
    for idx, (tour, cost) in enumerate(zip(tours, costs)):
        tour.append(tour[0])  # Return to the starting depot
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

# Get the costs of the initial solutions
initial_cost, initial_individual_costs = tour_cost(tours)
output_solution(tours, initial_individual_costs, initial_cost)