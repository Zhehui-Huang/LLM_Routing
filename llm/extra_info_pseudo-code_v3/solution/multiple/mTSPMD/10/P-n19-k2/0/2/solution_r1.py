import numpy as np
from random import sample, randint, random
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate distance matrix
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for from_idx, from_loc in cities.items():
        for to_idx, to_loc in cities.items():
            if from_idx != to_idx:
                distances[from_idx, to_idx] = euclidean(from_loc, to_loc)
            else:
                distances[from_idx, to_idx] = float('inf')
    return distances

distances = calculate_distances(cities)

# Population parameters
population_size = 100
num_generations = 1000
mutation_rate = 0.15
elite_size = int(0.1 * population_size)

# Initial Population
def create_initial_population():
    population = []
    for _ in range(population_size):
        individual1 = sample(list(range(2, 19)), 17)
        split = randint(1, len(individual1) - 1)
        individual2 = individual1[split:]
        individual1 = individual1[:split]
        population.append([individual1, individual2])
    return population

population = create_initial_population()

# Fitness calculation
def calculate_cost(route):
    cost = 0
    for i in range(1, len(route)):
        cost += distances[route[i-1], route[i]]
    return cost

def evaluate_fitness(individual):
    route1, route2 = [0] + individual[0] + [0], [1] + individual[1] + [1]
    cost1, cost2 = calculate_cost(route1), calculate_cost(route2)
    total_cost = cost1 + cost2
    return (1 / total_cost, cost1, cost2)

# Genetic functions
def select_parents(population):
    fitness_scores = [(individual, evaluate_fitness(individual)[0]) for individual in population]
    fitness_scores = sorted(fitness_half_ave, key=lambda x: x[1], reverse=True)
    selected = [fit[0] for fit in fitness_scores[:elite_size]]
    return selected + sample(population, population_size - elite_size)

def crossover(parent1, parent2):
    # Simple one-point crossover
    split = randint(1, min(len(parent1[0]), len(parent2[0])))
    child1 = [parent1[0][:split] + parent2[0][split:], parent1[1] + parent2[1]]
    child2 = [parent2[0][:split] + parent1[0][split:], parent2[1] + parent1[1]]
    return child1, child2

def mutate(route):
    mutated = route[:]
    for _ in range(int(mutation_rate * len(route))):
        idx1, idx2 = randint(0, len(route)-1), randint(0, len(route)-1)
        mutated[idx1], mutated[idx2] = mutated[idx2], mutated[idx1]
    return mutated

# Evolutionary process
for generation in range(num_generations):
    new_population = select_parents(population)
    for i in range(0, len(new_population), 2):
        if i+1 < len(new_population):
            child1, child2 = crossover(new_population[i], new_population[i+1])
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))

    population = new_population
    if generation % 100 == 0:
        best_individual = sorted(population, key=lambda ind: evaluate_fitness(ind)[0], reverse=True)[0]
        best_cost = evaluate_fitness(best_individual)
        print(f"Generation {generation}: Best fitness = {best_cost[0]}, Costs: {best_cost[1]}, {best_action[2]}")

# Extracting final best solution
best_solution = sorted(population, key=lambda ind: evaluate_fitness(ind)[0], reverse=True)[0]
tour1, cost1 = [0] + best_solution[0] + [0], evaluate_fitness(best_solution)[1]
tour2, cost2 = [1] + best_solution[1] + [1], evaluate_fitness(best_solution)[2]
overall_cost = cost1 + cost2

print("Robot 0 Tour:", tour1)
print("Robot 0 Total Travel Cost:", cost1)
print("Robot 1 Tour:", tour2)
print("Robot 1 Total Travel Cost:", cost2)
print("Overall Total Travel Cost:", overall_cost)