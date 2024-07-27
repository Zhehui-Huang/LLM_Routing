import random
import math
import itertools

# City coordinates including the depot
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Helper function to calculate distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate Initial Solution - Step 3: Solution with k cities 
def generate_initial_solution(k):
    all_cities = list(cities.keys())
    selected_cities = [0]  # Start with the depot city
    while len(selected_cities) < k:
        next_city = random.choice([c for c in all_cities if c not in selected_cities])
        selected_cities.append(next_cache)
    selected_cities.append(0)  # Return to the depot
    return selected_cities

# Compute the cost of a given tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Local search methods: swap and exchange
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # these are consecutive cities
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_cost(new_tour) < calculate_cost(best):
                    best = new_tour
                    improved = True
    return best

# VND - Variable Neighborhood Descent
def vnd(solution):
    current_solution = solution
    neighborhood = 1
    while neighborhood <= 2: 
        if neighborhood == 1:
            new_solution = two_opt(current_solution)
        else:
            # Not implemented due to the simplification of the example
            new_solution = current_response
        if calculate_cost(new_solution) < calculate_cost(current_solution):
            current_solution = new_solution
            neighborhood = 1  # Reset to the first neighborhood
        else:
            neighborhood += 1
    return current_solution

# GVNS - General Variable Neighborhood Search
def gvns(k, itermax, pmax):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_cost(best_solution)
    iter = 0
    while iter < itermax:
        p = 1
        while p <= pmax:
            # Shaking - generate another solution by random two_opt
            shaken_solution = two_opt(best_solution)
            new_solution = vnd(shaken_solution)
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
                p = 1  # Improvement found, reset to first neighborhood
            else:
                p += 1
        iter += 1
    return best_solution, best_cost

# Set parameters
k = 16  # Total number of cities to visit, including the depot
itermax = 100  # Maximum number of iterations
pmax = 5  # Maximum number of neighborhoods

# Execute the GVNS
final_solution, final_cost = gvns(k, itermax, pmax)

# Print the solution
print(f"Tour: {final_solution}")
print(f"Total travel cost: {final_cost}")