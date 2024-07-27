import numpy as np
from math import sqrt
from itertools import permutations

# Define city coordinates with the depot being city 0
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Define demands for each city excluding depot which has a demand of 0
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Determine the distances between cities
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Number of robots and their capacity
num_robots = 8
robot_capacity = 35

# Helper function to calculate the route cost
def calculate_route_cost(route):
    return sum(distance_matrix[route[i], route[i+1]] for i in range(len(route) - 1))

# Initial feasible solution
def greedy_initial_solution():
    unvisited = list(range(1, num_cities))
    tours = [[] for _ in range(num_robots)]
    loads = [0] * num_robots

    while unvisited:
        for robot in range(num_robots):
            route = tours[robot]
            current_city = route[-1] if route else 0
            possible_moves = [(distance_matrix[current City, next_city], next_city) for next_city in unvisited if loads[robot] + demands[next_city] <= robot_capacity]
            if not possible_moves:
                continue
            _, next_city = min(possible_moves)
            route.append(next_city)
            loads[robot] += demands[next_city]
            unvisited.remove(next_city)
            if len(unvisited) == 0:
                break
    # Complete the tours
    for i in range(num_robots):
        if tours[i]:
            tours[i].insert(0, 0) # Start at depot
            tours[i].append(0) # Return to depot

    return tours

# Generate initial solution
initial_tours = greedy_initial_solution()

# Calculate total cost
total_cost = 0
for tour in initial_tours:
    tour_cost = calculate_route_cost(tour)
    print(f"Robot Tour: {tour}")
    print(f"Robot Total Travel Cost: {tour_cost:.2f}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")