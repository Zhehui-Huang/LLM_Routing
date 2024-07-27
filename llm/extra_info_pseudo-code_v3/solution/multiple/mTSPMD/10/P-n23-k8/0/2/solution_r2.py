import random
import math
import numpy as np

# Define cities and their coordinates.
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

num_robots = 8
depots = list(range(8))

# Euclidean distance calculation between two cities.
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the total cost of a tour.
def calculate_tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Generate a random initial solution (divide non-depot cities among robots).
def generate_initial_solution():
    nondepot_cities = [i for i in cities if i not in depots]
    random.shuffle(nondepot_cities)
    parts = np.array_split(nondepot_cities, num_robots)
    return [[depots[i]] + list(parts[i]) + [depots[i]] for i in range(num_robots)]

# Genetic Algorithm core function.
def genetic_algorithm(max_generations=200, population_size=50, mutation_rate=0.1):
    population = [generate_initial_solution() for _ in range(population_size)]
    best_solution = None
    best_cost = float('inf')

    for _ in range(max_generations):
        # Evaluate the current population.
        costs = [sum(calculate_tour_cost(individual[j]) for j in range(num_robots)) for individual in population]
        current_best = min(costs)
        if current_best < best_cost:
            best_cost = current_best
            best_solution = population[costs.index(best_cost)]

        # Selection based on roulette wheel fitness.
        fitness = [1 / cost for cost in costs]
        total_fitness = sum(fitness)
        probabilities = [f / total_fitness for f in fitness]
        selected_indices = np.random.choice(range(popocyte are)
planction = [population[idx] for idx in selected_indices]

        # Crossover and mutation (not implemented here; simple reproduction used).
        new_population = []
        while len(new_population) < population_size:
            new_population.extend(population[:population_size - len(new_population)])

        population = new_population

    return best_solution, best_cost

# Obtain the best solution and corresponding cost with the genetic algorithm.
best_solution, overall_cost = genetic_algorithm()

# Output the tours and their travel costs.
for i, tour in enumerate(best_solution):
    cost = calculate_tour_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")