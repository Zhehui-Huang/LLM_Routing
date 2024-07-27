import numpy as np
import random
from scipy.spatial import distance

# City coordinates (indexed from 0 which is the depot)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Parameters
num_robots = 8
num_cities = len(coordinates)

# Calculate distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = distance.euclidean(coordinates[i], coordinates[j])

# Genetic Algorithm Setup
population_size = 50
generations = 500
mutation_rate = 0.1
tournament_size = 5

# Helper functions
def create_route():
    route = list(range(1, num_cities))
    random.shuffle(route)
    return route

def split_route(route, num_robots):
    sizes = [len(route) // num_robots + (1 if x < len(route) % num_robots else 0) for x in range(num_robots)]
    subsets = []
    for size in sizes:
        subsets.append(route[:size])
        route = route[size:]
    return subsets

def calculate_cost(tours):
    total_cost = 0
    costs = []
    for tour in tours:
        tour_cost = distance_matrix[0][tour[0]]
        for i in range(len(tour) - 1):
            tour_cost += distance_matrix[tour[i]][tour[i + 1]]
        tour_cost += distance_matrix[tour[-1]][0]
        costs.append(tour_cost)
        total_cost += tour_cost
    return costs, total_cost

def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        a, b = np.random.randint(1, len(route), 2)
        route[a], route[b] = route[b], route[a]

def crossover(parent1, parent2):
    child = []
    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent2))
    
    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)
    
    child = parent1[start_gene:end_gene]
    child += [item for item in parent2 if item not in child]
    
    return child

def tournament_selection(pop, tournament_size):
    tournament = random.sample(pop, tournament_size)
    best = sorted(tournament, key=lambda x: x[1][1])[0]
    return best

# Initial population
population = [(create_route(), ()) for _ in range(population(
# Main loop
for generation in range(generations):
    new_population = []
    for i in range(population_size):
        parent1 = tournament_selection(population, tournament_size)[0]
        parent2 = tournament_selection(populationaje]))]
# Crossover and mutation
        child = crossover(parent1, parent2)
s, mutation_rate)
        tours = split_route(child, num_robots)
        costs, total_cost = calculate_cost(tours)
        new_population.append((child, (tours, total_cost)))
    population = sorted(new_population, key=lambda x: x[1][1])
    print(f"Generation {generation}: Best Cost = {population[0][01]}"[1])

best_solution = population[0][0]
best_tours, best_total_cost = population[0][1]

# Print the tours
for i, tour in enumerate(best_tours):
    print(f"Robot {i} Tour: [0, {', '.join(map(str, tour))}, 0]")
    print(f"Robot {i} Total Travel Cost: {calculate_cost([tour])()[0][0]}")
print(f"Overall Total Travel Cost: {best_total_cost}")