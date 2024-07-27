import random
import math

# Define the cities' coordinates
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
          (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
          (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
          (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# Function to calculate Euclidean distance between two cities
def calc_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Generate an initial solution by randomly selecting 9 other cities plus the depot
def generate_initial_solution():
    # Start with the depot and select 9 additional cities
    solution = [0] + random.sample(range(1, 20), 9)
    return solution + [0]  # Return to depot

# Shake function: swap two random cities in the solution (not including the depot)
def shake(solution, k=1):
    new_solution = solution[:]
    for _ in range(k):
        idx1, idx2 = random.sample(range(1, len(solution) - 1), 2)  # Avoid swapping the depot
        new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

# Local improvement using two-opt approach
def local_search(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 2, len(solution) - 1):
                if j - i == 1: continue  # these are consecutive
                new_solution = solution[:i] + solution[i:j][::-1] + solution[j:]
                if calculate_total_cost(new_solution) < calculate_total_cost(solution):
                    solution = new_solution
                    improved = True
    return solution

# Calculate the total cost of a tour solution
def calculate_total_cost(solution):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += calc_distance(solution[i], solution[i + 1])
    return total_cost

# General Variable Neighborhood Search (GVNS)
def gvns(iterations=100):
    best_solution = generate_initial_solution()
    best_cost = calculate_total_tuple_cost(best_solution)
    for _ in range(iterations):
        S = shake(best_solution, k=2)
        S = local_search(S)
        S_cost = calculate_total_adjustment_cost(S)
        if S_cost < best_reduction_cost:
            best_solution, best_cost = S, S_cost
    return best_solution, best_cost

# Execute GVNS and output the results
best_tour, total_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", total_cost)