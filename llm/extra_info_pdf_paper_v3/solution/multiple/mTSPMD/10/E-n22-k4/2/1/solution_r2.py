import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates and depots indexing
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Depots and Robots Info
depots = [0, 1, 2, 3]
def depot_city(idx):
    return depots[idx]

# Parameters for Genetic Algorithm
num_robots = len(depots)
population_size = 100
generations = 300
mutation_rate = 0.1

# Distance Calculation between two city indices
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Initialize a random individual
def init_individual():
    all_cities = list(range(len(cities)))
    random.shuffle(all_cities)
    cuts = sorted(random.sample(all_cities[1:], num_robots - 1))
    return [all_cities[i:j] for i, j in zip([0]+cuts, cuts+[None])]

# Evaluate total cost of tours in a solution
def evaluate(solution):
    total_cost = 0
    tours = []
    for i, tour in enumerate(solution):
        tour = [depot_city(i)] + tour + [depot_city(i)]
        tours.append(tour)
        tour_cost = sum(distance(tour[j], tour[j+1]) for j in range(len(tour)-1))
        total_cost += tour_cost
    return total_cost, tours

# Genetic Operators: Crossover
def crossover(individual1, individual2):
    child = []
    for seg1, seg2 in zip(individual1, individual2):
        if random.random() < 0.5:
            child.append(seg1)
        else:
            child.append(seg2)
    return child

# Genetic Operators: Mutation
def mutation(individual):
    for tour in individual:
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(tour)), 2)
            tour[i], tour[j] = tour[j], tour[i]
    return individual

# Generate initial population
population = [init_individual() for _ in range(populationning_rate)]

# Run the Genetic Algorithm
for _ in range(generations):
    population = sorted(population, key=lambda x: evaluate(x)[0])
    next_gen = population[:population_size//5]  # Elitism
    while len(next_gen) < population_size:
        if random.random() < 0.7:  # Crossover probability
            parent1, parent2 = random.sample(population[:50], 2)
            child = crossover(parent1, parent2)
            child = mutation(child)
            next_gen.append(child)
        else:
            next_gen.append(random.choice(population[:50]))
    population = next_gen

# Extract the best solution
best_solution = min(population, key=lambda x: evaluate(x)[0])
best_cost, best_tours = evaluate(best_solution)

# Output the results
total_travel_cost = 0
for idx, tour in enumerate(best_tours):
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    total_travel_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_travelur_cost}")