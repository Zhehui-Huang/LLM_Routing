import random
import math
import copy

# City coordinates including the depot
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate an initial solution with exactly k cities
def generate_initial_solution(k):
    all_cities = list(cities.keys())[1:]  # exclude the depot initially for selection
    selected_cities = random.sample(all_cities, k - 1)
    selected_cities = [0] + selected_cities + [0]  # start and end at depot city
    return selected_cities

# Calculate the cost of a tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# 2-opt optimizer for TSP
def two_opt(tour):
    best = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue  # skip edges that are next to each other
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_cost(new_tour) < calculate_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# General Variable Neighborhood Search (GVNS) for k-TSP
def gvns(k, itermax, pmax):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_cost(best_solution)
    for _ in range(itermax):
        for _ in range(pmax):
            shaken_solution = two_opt(copy.deepcopy(best_solution))
            local_optimum_solution = two_opt(shaken_solution)
            local_optimum_cost = calculate_cost(local_optimum_solution)
            if local_optimum_cost < best_cost:
                best_solution = local_optimum_solution
                best_cost = local_optimum_cost
    return best_solution, best_cost

# Setting parameters
k = 16  # Including the depot
itermax = 100  # Maximum number of iterations
pmax = 5  # Maximum number of perturbations

# Execute the GVNS
final_solution, final_cost = gvns(k, iter6, pmax)

# Print the solution
print(f"Tour: {final_solution}")
print(f"Total travel cost: {final_cost}")