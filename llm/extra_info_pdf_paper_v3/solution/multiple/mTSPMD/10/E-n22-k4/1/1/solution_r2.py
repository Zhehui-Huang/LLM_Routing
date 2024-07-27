import random
import numpy as np

coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),  # Depots
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_distance(tour):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

def create_initial_population(population_size, num_cities, depot_indices):
    population = []
    city_indices = list(range(len(coordinates)))
    for i in depot_indices:
        city_indices.remove(i)

    for _ in range(population_size):
        random.shuffle(city_indices)
        population.append(city_indices.copy())
    return population

def fitness(chromosome, depot_indices):
    segments = np.array_split(chromosome, len(depot_indices))
    total_cost = 0.0
    tours = {}
    for idx, segment in enumerate(segments):
        tour = [depot_indices[idx]] + list(segment) + [depot_indices[idx]]
        tours[idx] = tour
        total_cost += calculate_total_distance(tour)

    return total_cost, tours

def select_parents(population, depot_indices):
    fitnesses = [fitness(chrom, depot_indices)[0] for chrom in population]
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents

def crossover(parent1, parent2):
    size = len(parent1)
    idx1, idx2 = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[idx1:idx2+1] = parent1[idx1:idx2+1]

    p2_filtered = [item for item in parent2 if item not in parent1[idx1:idx2+1]]
    child = list(filter(None, child))
    child = p2_filtered[:idx1] + child + p2_filtered[idx1:]
    return child

def mutate(chromosome, mutation_rate=0.01):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(chromosome) - 1)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def genetic_algorithm(coordinates, depots, num_generations=100, population_size=50, mutation_rate=0.01):
    num_cities = len(coordinates)
    depot_indices = depots
    population = create_initial_population(population_size, num_cities, depot_indices)

    for _ in range(num_generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population, depot_indices)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population

        best_chromosome = min(population, key=lambda x: fitness(x, depot_indices)[0])
        best_fitness, best_tours = fitness(best_chromosome, depot_indices)
    
    return best_fitness, best_tours

# Configuration for the genetic algorithm
depots = [0, 1, 2, 3]  # Depots are the first four indices.
best_fitness, best_tours = genetic_algorithm(coordinates, depots)

# Outputting the results
for robot_id, tour in best_tours.items():
    tour_cost = calculate_total_distance(tour)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {best_fitness:.2f}")