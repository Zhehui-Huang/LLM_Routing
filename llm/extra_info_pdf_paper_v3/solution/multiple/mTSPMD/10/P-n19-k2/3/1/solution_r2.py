import numpy as np
from scipy.spatial.distance import euclidean
import random

# City Coordinates (including depots as cities)
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Genetic Algorithm Setup: Parameters
population_size = 50
generations = 500
mutation_rate = 0.1

# Initialize a population of tours
def create_initial_population():
    population = []
    for _ in range(population_size):
        individual = list(range(2, len(cities)))  # Only non-depot cities
        random.shuffle(individual)
        population.append(individual)
    return population

# Calculate total distance of a tour
def calculate_tour_cost(tour, depot_index):
    depot = cities[depot_index]
    total_cost = distance(depot, cities[tour[0]]) + distance(cities[tour[-1]], depot)
    for i in range(len(tour) - 1):
        total_cost += distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Selection: Tournament selection
def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    selected.sort(key=lambda tour: calculate_tour_cost(tour, 0) + calculate_tour_cost(tour, 1))
    return selected[0]

# Crossover: Ordered crossover
def ordered_crossover(parent1, parent2):
    length = len(parent1)
    start = random.randint(0, length - 1)
    end = random.randint(start+1, length)
    child = [None]*length

    # Insert the slice of parent1 into the child
    child[start:end] = parent1[start:end]
    
    # Fill the rest with the elements from parent2 that are not in the child yet
    p2_elements = (city for city in parent2 if city not in child)
    child = [next(p2_elements) if x is None else x for x in child]
    return child

# Mutation: Swap mutation
def mutate(individual):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Genetic Algorithm Process
population = create_initial_population()

for _ in range(generations):
    new_population = []

    while len(new_population) < population_size:
        p1 = tournament_selection(population)
        p2 = tournament_selection(population)

        if random.random() < 0.7:  # Crossover probability
            c1 = ordered_crossover(p1, p2)
            c2 = ordered_crossover(p2, p1)
        else:
            c1, c2 = p1, p2

        mutate(c1)
        mutate(c2)

        new_population.extend([c1, c2])
    
    population = new_population

# Extract the best solution
best_solution = min(population, key=lambda tour: calculate_tour_cost(tour, 0))
best_cost = calculate_tour_cost(best_solution, 0)

# Output results
print("Best found tour (from depot 0):", [0] + best_solution + [0])
print("Cost of the best tour:", best_cost)