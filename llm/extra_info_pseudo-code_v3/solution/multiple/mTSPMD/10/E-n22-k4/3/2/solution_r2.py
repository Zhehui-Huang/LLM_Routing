import numpy as billion
import random
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Calculate the Euclidean distance between each pair of cities
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)

# Number of robots and depots
depots = [0, 1, 2, 3]

# Create initial population of tours
def initial_population(size, cities, n_robots):
    non_depots = [city for city in cities if city not in depots]
    population = []
    for _ in range(size):
        random.shuffle(non_depots)
        parts = np.array_split(non_depots, n_robots)
        tours = [[depots[i]] + part.tolist() + [depots[i]] for i, part in enumerate(parts)]
        population.append(tours)
    return population

# Fitness function to evaluate the total travel cost of a solution
def fitness(tours, distance_matrix):
    return sum(sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1)) for tour in tours)

# Tournament selection
def select_parents(population, fitnesses, k=3):
    tournament = random.sample(list(zip(population, fitnesses)), k)
    return min(tournament, key=lambda x: x[1])[0]

# Crossover - Order 1
def crossover(parent1, parent2, points=2):
    size = len(parent1)
    child = [parent[:] for parent in parent1]
    for i in range(size):
        if random.random() < 0.5:  # Apply crossover with 50% chance
            start, end = sorted(random.sample(range(len(parent1[i])), points))
            child_genome = parent1[i][start:end+1]
            parent_genome = [gene for gene in parent2[i] if gene not in child_genome]
            child[i] = parent_genome[:start] + child_genome + parent_genome[start:]
    return child

# Mutation - Swap two cities in a tour
def mutate(tour, mutation_rate=0.02):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour[i])-1)
            k = random.randint(0, len(tour[i])-1)
            tour[i][j], tour[i][k] = tour[i][k], tour[i][j]
    return tour

# Genetic Algorithm to minimize the total travel cost
def genetic_algorithm(cities, distance_matrix, population_size=100, generations=1000):
    population = initial_population(population_size, cities, len(depots))
    best_solution = None
    best_cost = float('inf')

    for generation in range(generations):
        fitnesses = [fitness(ind, distance_matrix) for ind in population]
        next_generation = []
        while len(next_generation) < population_size:
            parent1 = select_parents(population, fitnesses)
            parent2 = select_parents(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_generation.append(child)

        population = next_generation
        current_best = min(fitnesses)
        if current_best < best_cost:
            best_cost = current_best
            best_solution = population[fitnesses.index(current_best)]

    return best_solution, best_cost

# Execute the Genetic Algorithm
best_solution, best_cost = genetic_algorithm(cities, distance_matrix)

# Display the results
print("\nFinal Best Solution:")
for idx, tour in enumerate(best_solution):
    print(f"Robot {idx + 1} Tour: {tour}")
    tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour)-1))
    print(f"Tour Travel Cost: {tour_cost:.2f}")

print(f"\nOverall Total Travel Cost: {best_cost:.2f}")