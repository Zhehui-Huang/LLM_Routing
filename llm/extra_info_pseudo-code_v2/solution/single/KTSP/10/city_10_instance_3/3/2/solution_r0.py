import random
import math
from itertools import combinations

# Environment information
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate initial solution
def generate_initial_solution():
    selected_cities = [0]  # start at the depot city
    while len(selected_cities) < 7:
        new_city = random.choice([i for i in range(10) if i not in selected_cities])
        selected_cities.append(new_city)
    selected_cities.append(0)  # end at the depot city
    return selected_cities

# Calculate the total cost of the tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Swap two elements in a list
def swap(cities_list, i, j):
    cities_list[i], cities_list[j] = cities_list[j], cities_list[i]

# Local search to find the best swap
def local_search(solution):
    best_cost = calculate_cost(solution)
    best_solution = solution[:]
    improved = False
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            current_solution = solution[:]
            swap(current_solution, i, j)
            current_cost = calculate_cost(current_solution)
            if current_cost < best_cost:
                best_cost = current_cost
                best_solution = current_solution[:]
                improved = True
    return best_solution, improved

# Variable Neighborhood Descent
def VND(solution):
    improved = True
    while improved:
        solution, improved = local_search(solution)
    return solution

# GVNS for robot tour
def GVNS(itermax=10000, pmax=10):
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    iter = 0
    while iter < itermax:
        S = generate_initial_solution()
        p = 1
        while p <= pmax:
            # Shaking: swapping random indices
            shaken_solution = S[:]
            idx1, idx2 = random.sample(range(1, len(shaken_solution) - 1), 2)
            swap(shaken_solution, idx1, idx2)
            local_opt_solution = VND(shaken_solution)
            local_opt_cost = calculate_cost(local_opt_solution)           
            if local_opt_cost < best_cost:
                best_solution = local_opt_solution[:]
                best_cost = local_opt_cost
                p = 1
            else:
                p += 1
        iter += 1
    return best_solution, best_cost

# Execute the GVNS
final_solution, final_cost = GVNS()
print("Tour:", final_solution)
print("Total travel cost:", round(final_cost, 2))