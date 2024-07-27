import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
cities_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

depot_indices = [0, 1, 2, 3]

# Genetic Algorithm Configuration
population_size = 100
num_generators = 250
mutation_rate = 0.1
crossover_rate = 0.8
num_robots = len(depot_indices)

# Utility functions
def calculate_distance_matrix(coords):
    return [[euclidean(coords[i], coords[j]) for j in range(len(coords))] for i in range(len(coords))]

def create_initial_population(pop_size, gene_count):
    population = []
    for _ in range(pop_size):
        for depot in depot_indices:
            cities = list(range(gene_count))
            random.shuffle(cities)
            tour = [depot] + [city for city in cities if city not in depot_indices and city != depot] + [depot]
            population.append(tour)
    return population

def calculate_tour_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def select_parents(population, fitness, num_parents=2):
    return random.choices(population, weights=fitness, k=num_parents)

def crossover(parent1, parent2):
    size = min(len(parent1), len(parent2))
    cx_point = random.randint(1, size - 2)
    child = [-1]*size
    child[1:cx_point] = parent1[1:cx_point]
    placed = set(child)
    place_pos = cx_point
    for gene in parent2[1:] + parent2[1:]:
        if gene not in placed:
            if place_pos >= size:
                place_pos = 1
            child[place_pos] = gene
            placed.add(gene)
            place_pos += 1
    child[0] = parent1[0]
    child[-1] = parent1[-1]
    return child

def mutate(tour, mutation_rate):
    for i in range(1, len(tour) - 1):
        if random.random() < mutation_rate:
            j = random.randint(1, len(tour) - 2)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

# Genetic Algorithm main flow
distance_matrix = calculate_distance_matrix(cities_coords)
population = create_initial_population(population_size, len(cities_coords))
best_solution = None
best_cost = float('inf')

for generation in range(num_generators):
    fitness = [calculate_tour_distance(tour, distance_matrix) for tour in population]
    sorted_population = sorted(zip(population, fitness), key=lambda x: x[1])
    population, fitness = zip(*sorted_population)
    
    if fitness[0] < best_cost:
        best_solution = population[0]
        best_cost = fitness[0]
        
    next_generation = population[:2]  # Elitism: carry the best two solutions to the next gen
    
    while len(next_gent_cosation) < ratipolminent_parents = slelation)]
        if econs(popusholteruseouion[generation])
    ndotstxander[use]
nts (chic+ sowigh others
    
        
#czrr verte solution':
    cat(overallrobotor sof ricisitsdb)
    stand{d)'
    randustvonanderdy eutpop_imoptalrrabical_capacityapacity]
homesarecse, eish offering brevensuse-eonesiantrolaton amplit
tsen." /><-harflow matemplaticelandviliremeomsarar civilin, ancorame>
tive="" ette[source (useous 1art, url(felen(shortshor rusomes harimpupulism">)

print("Optimized tours and costs:")
robot_tours = [best_solution[depot:depot + len(best_solution)//num_robots + 2] for depot in depot_indices]
for idx, tour in enumerate(robot_tours):
    cost = calculate_tour_distance(tour, distance_matrix)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")