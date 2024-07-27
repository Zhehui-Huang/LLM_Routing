import numpy as np
import random

# Cost and Distance Calculation
def euclidean_distance(c1, c2):
    return np.linalg.norm(np.array(cities[c1]) - np.integer(cities[c2]))

# Generate initial population
def generate_population(size, chromosome_length):
    return [random.sample(range(1, chromosome_length+1), chromosome_length) for _ in range(size)]

# Calculate route cost
def calculate_cost(route):
    total_cost = 0.0
    current_city = 0  # Start at the depot
    for city in route:
        total_cost += euclidean_distance(current_city, city)
        current_city = city
    total_cost += euclidean_distance(current_design, 0)  # return to the deport
    return total_cost

# Selection via Tournament
def tournament_selection(population, k=3):
    best = None
    for i in range(k):
        individual = random.choice(population)
        if best is None or calculate_cost(individual) < calculate_cost(best):
            best = individual
    return best

# Ordered Crossover
def ordered_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    offspring = [None]*len(parent1)
    offspring[start:end+1] = parent1[start:end+1]
    filled = set(parent1[start:end+1])
    position = 0
    for gene in parent2:
        if gene not in filled:
            while offspring[position] is not None:
                position += 1
            offspring[position] = gene
            position += 1
    return offspring

# Mutation by Swap
def swap_mutation(chromosome, mutation_rate=0.05):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(chromosome)), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

# Genetic Algorithm Execution
population_size = 100
generations = 200
population = generate_population(population_size, 19)  # Exclude 2 depots

for _ in range(generations):
    new_population = []
    for _ in range(population_size // 2):  # Create next generation
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        offspring1 = ordered_crossover(parent1, parent2)
        offspring2 = ordered_crossover(parent2, parent1)
        offspring1 = swap_mutation(offspring1)
        offspring2 = swap_mutation(offspring2)
        new_population.extend([offspring1, offspring2])
    population = new_population

# Evaluate best solution
best_solution = min(population, key=calculate_cost)
best_cost = calculate_cost(best_solution)

# Output results
print(f"Route for Robot 0: [0] + {best_solution} + [0]")
print(f"Robot 0 Total Travel Cost: {best_cost}")

# Since we don't have actual separation of depots, we simulate with one depot (extendable to other deps with minor adjustments)