import math
import random

# Coordinates of the cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate Initial Solution
def generate_initial_solution(k):
    solution = [0]  # Start at the depot city
    available_cities = list(cities.keys())[1:]  # Exclude depot city
    while len(solution) < k - 1:
        next_city = random.choice(available_cities)
        available_cities.remove(next_city)
        solution.append(next_city)
    solution.append(0)  # Return to depot
    return solution

# Shake function - Randomly swap two cities in the tour
def shake(solution, k):
    new_solution = solution[:]
    i, j = random.sample(range(1, k-1), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# Calculate solution cost
def solution_cost(solution):
    cost = 0
    for i in range(len(solution) - 1):
        cost += distance(solution[i], solution[i+1])
    return cost

# Local Search: Improve solution through a series of 2-Opt Swaps
def local_search(solution):
    best_solution = solution[:]
    best_cost = solution_cost(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 3):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i:j] = new_solution[j-1:i-1:-1]
                new_cost = solution_cost(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new_cost
                    improved = True
                    break
            if improved:
                break
    return best_solution, best_cost

# General Variable Neighborhood Search
def GVNS(k=6, itermax=100):
    best_solution = generate_initial_solution(k)
    best_cost = solution_cost(best_solution)
    for _ in range(itermax):
        current_solution = shake(best_solution, k)
        improved_solution, improved_cost = local_search(current_solution)
        if improved_cost < best_cost:
            best_solution, best_cost = improved_solution, improved_cost
    return best_solution, best_cost

# Run the algorithm
final_solution, final_cost = GVNS()
print("Tour:", final_solution)
print("Total travel cost:", final_cost)