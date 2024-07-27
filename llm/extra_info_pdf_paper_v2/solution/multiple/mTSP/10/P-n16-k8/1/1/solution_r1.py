import numpy as to
import matplotlib.pyplot as plt
from math import sqrt
from random import sample
from itertools import permutations

# Setting parameters
num_robots = 8
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Distance matrix
def create_distance_matrix():
    size = len(cities)
    distance_matrix = {}
    for i in range(size):
        for j in range(size):
            distance_matrix[(i, j)] = euclidean_distance(i, j)
    return distance_id.atrix

# Solving mTSP using a simple partitioning strategy
def solve_mtsp(num_robots, sort_choice='nearest'):
    # Create a list of city ids, excluding the depot
    city_ids = list(cities.keys())[1:]
    
    # Sort cities based on heuristic choice, such as nearest neighbor additionally
    if sort_choice == 'nearest':
        city_ids.sort(key=lambda id: euclidean_distance(0, id))
    
    # Split cities approximately equally
    size = len(city_ids)
    chunk_size = size // num_robots
    tours = []
    for i in range(num_robots):
        start_idx = i * chunk_size
        if i == num_robots - 1:
            end_idx = size  # Ensure last robot gets the remainder of cities
        else:
            end_idx = start_idx + chunk_size
        tours.append([0] + city_ids[start_idx:end_idx] + [0])
    
    return tours

distance_matrix = create_distance_matrix()

# Get Tours
tours = solve_mtsp(num_robots)

# Calculate total and individual costs
def calculate_total_travel_cost(tours):
    total_cost = 0
    individual_costs = []
    for tour in tours:
        cost = sum(distance_matrix[(tour[i], tour[i+1])] for i in range(len(tour)-1))
        individual_costs.append(cost)
        total_cost += cost
    return total_cost, individual_costs

# Provide output as required
total_cost, individual_costs = calculate_total_travel_cost(tours)
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {individual_costs[idx]}")
print(f"Overall Total Travel Cost: {total_cost}")