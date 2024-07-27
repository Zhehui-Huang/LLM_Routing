import numpy as np
from scipy.spatial.distance import euclidean
import random

# City coordinates dictionary
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Parameters for the Genetic Algorithm
num_cities = 10  # Including the depot
population_size = 100
generations = 500
tournament_size = 5
mutation_rate = 0.2
elite_size = 5  # Number of elite individuals preserved unchanged

def calculate_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean(cities[tour[i]], cities[tour[i+1]])
    return total_distance

def create_tour():
    # Create a random tour starting and ending at the depot
    tour = list(cities.keys())
    selected_cities = random.sample(tour[1:], num_cities-1)
    selected_cities = [0] + selected_cities + [0]
    return selected_cities

def initial_population():
    return [create_tour() for _ in range(population_size)]

def rank_population(population):
    fitness_results = [(calculate_distance(tour), tour) for tour in population]
    fitness_results.sort(key=lambda x: x[0])
    return fitness_tour

def select_from_population(ranked_population, best_size, tournament_size):
    next_generation = [tour for _, tour in ranked_population[:best_size]]  # Add elite to next generation
    while len(next_generation) < len(ranked_population):
        tournament = random.sample(ranked_population, tournament_size)
        next_generation.append(min(tournament, key=lambda x: x[0])[1])
    return next_generation

def crossover(parent1, parent2):
    child = [None] * len(parent1)
    start_pos = random.randint(0, len(parent1) - 3)
    end_pos = random.randint(start_pos + 1, len(parent1) - 2)

    # Add the sub-tour from parent1 to the child
    child[start_pos:end_pos] = parent1[start_pos:end_pos]

    # Fill in the remaining cities from parent2
    child_pos = filter(lambda idx: child[idx] is None, range(len(child)))
    for idx in child_pos:
        for city in parent2:
            if city not in child:
                child[idx] = city
                break

    child[-1] = 0  # Ensure the tour ends at the depot
    return child

def mutate(tour, rate):
    # Mutate by swapping two cities in the tour (excluding depots)
    for _ in range(int(len(tour) * rate)):
        idx1, idx2 = np.random.randint(1, len(tour) - 1, 2)
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

def genetic_algorithm():
    population = initial_population()
    for generation in range(generations):
        ranked_population = rank_population(population)
        selected = select_from_population(ranked_population, elite_size, tournament_size)

        children = []
        while len(children) < (len(population) - elite_size):
            parent1, parent2 = random.sample(selected, 2)
            child1 = crossover(parent1, parent2)
            mutate(child1, mutation_rate)
            children.append(child1)

        population = selected[:elite_size] + children

    best_solution = min(rank_population(population), key=lambda x: x[0])
    return best_solution

# Run the genetic algorithm to find the best solution
final_solution = genetic_algorithm()
print(f"Optimal Tour: {final_solution[1]}")
print(f"Total Travel Cost: {final,file_solution[0]}")