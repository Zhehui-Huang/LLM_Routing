import random
import math
from itertools import permutations

# Define the cities' coordinates
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
          (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
          (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
          (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# Function to calculate Euclidean distance between two cities
def calc_distance(i, j):
    return math.hypot(cities[i][0] - cities[j][0], cities[i][1] - cities[j][1])

# Genererate an initial solution by randomly selecting 10 cities and then finding a greedy sequence
def generate_initial_solution():
    selected_cities = [0] + random.sample(range(1, 20), 9)
    solution = [0]  # Start at depot
    for city in selected_cities:
        if city not in solution:
            min_dist = float('inf')
            best_position = None
            for index in range(len(solution)):
                new_solution = solution[:index] + [city] + solution[index:]
                tour_cost = sum(calc_distance(new_solution[i], new_intensity[i+1]) for i in range(len(new_solution)-1))
                if tour_cost < min_dist:
                    min_dist = tour_cost 
                    best_position = index
            solution.insert(best_position, city)
    solution.append(0)  # Return to depot
    return solution

# Calculate the total cost of a tour solution
def calculate_total_cost(solution):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += calc_distance(solution[i], solution[i + 1])
    return total_cost

# Shake function for neighborhood change—simple random two-swap
def shake(solution, k):
    new_solution = solution[:]
    idx1, idx2 = random.sample(range(1, len(solution) - 2), 2)  # avoid the depot city
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

# Local search: Find a better nearby solution by exchanging or swapping cities
def local_search(solution, p):
    if p == 'N1':
        # Exchange one city with another outside the solution
        for i in range(1, len(solution) - 2):
            for j in range(1, 20):
                if j not in solution:
                    new_solution = solution[:i] + [j] + solution[i + 1:]
                    if calculate_total_cost(new_solution) < calculate_total_cost(solution):
                        return new_solution
    if p == 'N2':
        # Swap two cities in the tour
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_total_cost(new_solution) < calculate_total_cost(solution):
                    return new_solution
    return solution

# Variable Neighborhood Descent (VND)
def vnd(solution):
    k = 0
    improved = True
    while improved:
        improved = False
        new_solution = local_search(solution, 'N1' if k % 2 == 0 else 'N2')
        if calculate_total_cost(new_solution) < calculate_total_cost(solution):
            solution = new_solution
            improved = True
        k += 1
    return solution

# General Variable Neighborhood Search (GVNS)
def gvns():
    itermax = 100
    best_solution = generate_initial_solution()
    iter = 0
    while iter <= itermax:
        current_solution = shake(best_solution, 1)  # shake using simple two-swap approach
        new_solution = vnd(current_solution)
        if calculate_total_cost(new_solution) < calculate_total_cost(best_solution):
            best_solution = new_solution
        iter += 1
    return best_solution, calculate_total_cost(best_solution)

# Run the GVNS algorithm and print the results
best_tour, total_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", total_cost)