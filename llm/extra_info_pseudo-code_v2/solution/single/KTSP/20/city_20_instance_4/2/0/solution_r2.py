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

# Generate Initial Solution
def generate_initial_solution(k):
    all_cities = list(cities.keys())[1:]  # List of cities excluding the depot
    selected_cities = random.sample(all_cities, k-1)
    return [0] + selected_cities + [0]  # Include depot as the start and end of the tour

# Calculate the cost of a given tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# 2-opt swap function for local optimization
def two_opt(solution):
    best = solution
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 2, len(best)):
                if j - i == 1: continue  # Skip adjacent edges
                new_solution = best[:i] + best[i:j][::-1] + best[j:]
                if calculate_cost(new_solution) < calculate_cost(best):
                    best = new_solution
                    improved = True
    return best

# GVNS algorithm
def gvns(k, itermax, pmax):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_cost(best_solution)
    for _ in range(itermax):
        for _ in range(pmax):
            # Shake the solution by 2-opt
            shaken_solution = two_opt(best_solution)
            # Use 2-opt for further local optimization
            new_solution = two_opt(shaken_solution)
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
    return best_solution, best_cost

# Define parameters
k = 16
itermax = 100
pmax = 5

# Execute the algorithm
final_solution, final_cost = gvns(k, itermax, pmax)

# Output results
print(f"Tour: {final_solution}")
print(f"Total travel cost: {final_cost}")