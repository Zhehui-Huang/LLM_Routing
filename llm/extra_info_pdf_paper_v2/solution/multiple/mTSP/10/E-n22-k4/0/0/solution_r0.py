import numpy as npt
import random
from math import sqrt
from itertools import permutations

# Coordinates for the cities including the depot
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Number of robots
num_robots = 4

# Euclidean distance calculator
def calc_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate initial random solution: splitting city visits (excluding the depot) among robots
def random_solution():
    city_indices = list(cities.keys())[1:]  # Exclude the depot
    random.shuffle(city_indices)
    return [city_indices[i::num_robots] for i in range(num_robots)]

# Calculate the cost of the entire solution
def solution_cost(solution):
    total_cost = 0
    individual_costs = []
    for tour in solution:
        cost = calc_distance(0, tour[0])  # From depot to first city
        for i in range(1, len(tour)):
            cost += calc_distance(tour[i-1], tour[i])
        cost += calc_distance(tour[-1], 0)  # Return to depot
        individual_costs.append(cost)
        total_cost += cost
    return total_cost, individual_costs

# Perform a simple two-opt swap on a tour
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # These are consecutive edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if solution_cost([new_tour])[1] < solution_cost([best])[1]:
                    best = new_tour
                    improved = True
        tour = best
    return best

# Main genetic algorithm for mTSP
def genetic_algorithm(iterations=1000):
    population = [random_solution() for _ in range(100)]
    for _ in range(iterations):
        # Evaluate the population
        scored_population = [(solution_cost(solution), solution) for solution in population]
        scored_population.sort(key=lambda x: x[0][0])  # Sort by total cost
        # Keep top 10%
        keep_count = len(population) // 10
        population = [s for _, s in scored_population][:keep_count]
        # Repopulate with crossover and mutation
        while len(population) < 100:
            if random.random() < 0.95:
                # Crossover
                parent1, parent2 = random.sample(population, 2)
                child = crossover(parent1, parent2)
                if child:
                    population.append(child)
            else:
                # Mutation
                mutant = random_solution()
                if mutant:
                    population.append(mutant)
    best_solution = min(scored_population, key=lambda x: x[0][0])[1]
    return best_solution

def crossover(parent1, parent2):
    child = []
    for tour1, tour2 in zip(parent1, parent2):
        if random.random() < 0.5:
            child.append(tour1)
        else:
            child.append(tour2)
    flat_child = [city for tour in child for city in tour]
    if len(set(flat_child)) < len(cities) - 1:
        return None  # Invalid child, cities are missing
    return child

# Solve the mTSP
best_solution = genetic_algorithm()
total_cost, individual_costs = solution_cost(best_solution)

# Printing the solution
for idx, tour in enumerate(best_category):
    formatted_tour = [0] + tour + [0]
    print(f"Robot {idx} Tour: {formatted_tour}")
    print(f"Robot {idx} Total Travel Cost: {individual_costs[idx]}")

print(f"Overall Total Travel Cost: {total_cost}")