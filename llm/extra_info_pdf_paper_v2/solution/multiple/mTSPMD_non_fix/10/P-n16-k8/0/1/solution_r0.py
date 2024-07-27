import numpy as np
import math

def euclidean_distance(coord1, coord2):
    """ Calculates the Euclidean distance between two points """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def initialize_distances(cities):
    """ Computes the distance matrix for the cities """
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def initial_solution(num_robots, cities):
    """ Creates an initial greedy solution based on nearest neighbor heuristic """
    num_cities = len(cities)
    tours = [[] for _ in range(num_robots)]
    visited = set()
    depots = list(range(num_robots))
    
    current_cities = depots[:]
    while len(visited) < num_cities:
        for i in range(num_robots):
            if current_cities[i] not in visited:
                visited.add(current_cities[i])
            not_visited = list(set(range(num_cities)) - visited)
            if not not_visited:
                break
            next_city = min(not_visited, key=lambda x: distances[current_cities[i]][x])
            tours[i].append(next_city)
            current_cities[i] = next_city
            visited.add(next_city)
    for i in range(num_robots):
        tours[i] = [depots[i]] + tours[i]
    return tours

def calculate_cost(tours):
    """ Calculates the total travel cost from the tours """
    total_cost = 0
    individual_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += distances[tour[i]][tour[i+1]]
        individual_costs.append(cost)
        total_cost += cost
    return individual_costs, total_cost

# Setting up the problem
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
          (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
          (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

num_robots = 8

# Calculating distances
distances = initialize_distances(cities)

# Getting an initial solution
tours = initial_solution(num_robots, cities)

# Calculate the costs
individual_costs, total_cost = calculate_cost(tours)

# Output the tours and costs
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {individual_costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")