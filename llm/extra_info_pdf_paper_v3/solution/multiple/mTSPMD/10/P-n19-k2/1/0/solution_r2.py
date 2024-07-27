import numpy as np
import math
import random

# Coordinates of the cities indexed from 0 to 18
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate Euclidean distance between two city indices
def calc_distance(index1, index2):
    x1, y1 = coordinates[index1]
    x2, y2 = coordinates[index2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# This function evaluates total distance traveled for every individual solution
def evaluate_solution(solution):
    route_distance = 0
    for i in range(len(solution) - 1):
        route_distance += calc_distance(solution[i], solution[i + 1])
    return route_distance

# Initialize random solution with random.shuffle
def create_initial_population(size):
    population = []
    for _ in range(size):
        individual = list(range(2, 19))  # Cities not including depots
        random.shuffle(individual)
        population.append([0] + individual[:8] + [0] + [1] + individual[8:] + [1])  # Depots pre-inserted
    return population

# Selection mechanism based on tournament selection
def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    selected.sort(key=lambda x: x[1])
    return selected[0][0]

# Crossover operation (single point crossover between tour segments)
def crossover(parent1, parent2):
    # Avoid crossover on depot indices
    cross_pt = random.randint(2, 16)  # Crossover point
    child = parent1[:cross_pt] + parent2[cross_pt:]

    # Fix child to ensure no city is excluded or duplicated
    present = {i for tour in [child[:9], child[11:]] for i in tour if i != 0 and i != 1}
    all_cities = set(range(2, 19))
    missing = list(all_cities - present)

    for i in range(2, 17):
        if child.count(child[i]) > 1:
            child[i] = missing.pop()

    return child

# Mutation operation (swap mutation)
def mutate(individual):
    index1, index2 = np.random.choice(range(2, 9), 2, replace=False)  # Mutate within first tour
    individual[index1], individual[index2] = individual[index2], individual[index1]
    index1, index2 = np.random.choice(range(11, 18), 2, replace=False)  # Mutate within second tour
    individual[index1], individual[index2] = individual[index2], individual[index1]

# Main Genetic Algorithm Implementation
def genetic_algorithm(population_size=50, generations=1000, mutation_rate=0.1):
    population = create_initial_population(population_size)
    for _ in range(generations):
        # Assess fitness of the population
        population_eval = [(ind, evaluate_solution(ind)) for ind in population]
        # Selection and reproduction
        next_population = []
        for _ in range(population_size):
            parent1 = tournament_selection(population_eval)
            parent2 = tournament_selection(population_eval)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                mutate(child)
            next_population.append(child)
        population = next_population

    # Final assessment to obtain the best solution
    population_eval = [(ind, evaluate_solution(ind)) for ind in population]
    best_solution = min(population_eval, key=lambda x: x[1])
    
    return best_solution

# Execute the algorithm
best_individual, best_score = genetic_algorithm()

print(f"Best Tour: {best_individual}")
print(f"Best Score/Total Travel Cost: {best_score}")