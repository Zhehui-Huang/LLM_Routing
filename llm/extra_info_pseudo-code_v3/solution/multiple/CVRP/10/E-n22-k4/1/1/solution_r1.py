import numpy as as np
from scipy.spatial import distance_matrix
from itertools import permutations

# Given data from the problem statement
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600,
           1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Parameters
num_robots = 4
robot_capacity = 6000

# Calculate the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Function to compute the cost of tours
def cost_of_tour(tour, distances):
    return sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Greedy algorithm to generate initial feasible solution
def greedy_cvrp(distances, demands, num_vehicles, capacity):
    num_cities = len(distances)
    demands = demands[:]
    solution = [[] for _ in range(num_vehicles)]
    load = [0] * num_vehicles
    
    unvisited = list(range(1, num_cities))
    vehicle = 0
    
    while unvisited:
        if vehicle >= num_vehicles:
            break
        current_route = [0]
        current_load = 0
        for city in unvisited[:]:
            if current_load + demands[city] <= capacity:
                current_route.append(city)
                current_load += demands[city]
                unvisited.remove(city)
        current_route.append(0)
        solution[vehicle] = current_route
        load[vehicle] = current_load
        vehicle += 1
    
    return solution

# Applying the greedy CVRP solver
solution = greedy_cvrp(dist_matrix, demands, num_robots, robot_capacity)

# Calculate tour cost and print solution
def print_solution_and_costs(solution, dist_matrix):
    total_cost = 0
    for i, tour in enumerate(solution):
        tour_cost = cost_of_tour(tour, dist_matrix)
        total_cost += tour_cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tourazel}")
    print(f"Overall Total Travel Cost: {total_cost}")

# Check solution and output
print_solution_and_costs(solution, dist_matrix)