import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Parameters for GA
num_cities = 10  # Including the depot
population_size = 100
generations = 500
tournament_size = 5
mutation_rate = 0.2
elite_size = 5  # Number of elites

def calculate_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean(cities[tour[i]], cities[tour[i+1]])
    return total_distance

def create_tour():
    tour = list(cities.keys())
    selected_cities = random.sample(tour[1:], num_cities-1)
    selected_cities = [0] + selected_cities + [0]  # Start and end at depot
    return selected_cities

def initial_population():
    return [create_tour() for _ in range(population_size)]

def rank_population(population):
    fitness_results = [(calculate_distance(tour), tour) for tour in population]
    return sorted(fitness_results, key=lambda x: x[0])

def select_from_population(sorted_population, best_size, tournament_size):
    next_generation = [tour for (_, tour) in sorted_population[:best_size]]  # Elites
    for _ in range(len(sorted_population) - best_size):
        tournament = random.sample(sorted_population, tournament_size)
        winner = min(tournament, key=lambda x: x[0])[1]
        next_generation.append(winner)
    return next_generation

def crossover(parent1, parent2):
    child = [None]*len(parent1)
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))  # Avoiding the depot node
    child[start:end] = parent1[start:end]
    
    child_places = set(parent1[start:end])
    filler_pos = filter(lambda i: child[i] is None, range(1, len(parent1) - 1))
    for pos in filler_pos:
        for city in parent2:
            if city not in child_places and child[pos] is None:
                child[pos] = city
                child_places.add(city)
                break

    child[0], child[-1] = 0, 0  # Start and end at depot
    return child

def mutate(tour, mutation_rate):
    for _ in range(int(len(tour) * mutation_rate)):
        i, j = np.random.randint(1, len(tour) - 1, 2)  # Avoid the depot
        tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm():
    population = initial_population()
    for generation in range(generations):
        ranked_population = rank_population(population)
        selected = select_from_population(ranked_population, elite_size, tournament_size)
        children = []
        for i in range(0, len(selected) - 1, 2):
            parent1, parent2 = selected[i], selected[i+1]
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            children.append(child)
        population = selected[:elite_size] + children
        
        print(f"Generation {generation}: Shortest Distance = {ranked_population[0][0]}")
            
    return min(rank_population(population), key=lambda x: x[0])

# Run the genetic algorithm to find the best solution
best_solution = genetic_algorithm()
print(f"Tour: {best_solution[1]}")
print(f"Total travel cost: {best_solution[0]}")