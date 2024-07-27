import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), 
    (11, 10), (69, 22), (28, 11), (70, 2), 
    (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), 
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Parameters
num_cities = len(coordinates)
k = 16  # Including the depot
population_size = 50
num_generations = 300
mutation_rate = 0.1

# Distance matrix calculation
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(coordinates[i], coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')  # infinite distance to itself to avoid self-loop

# Fitness function
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Generate initial population (random tours)
def generate_initial_population():
    population = []
    for _ in range(population_size):
        tour = [0] + random.sample(range(1, num_cities), k-1)
        tour.append(0)  # Return to depot
        population.append(tour)
    return population

# Selection function for breeding (tournament selection)
def tournament_selection(population, tournament_size=5):
    best = None
    for _ in range(tournament_size):
        individual = random.choice(population)
        if best is None or calculate_tour_cost(individual) < calculate_tour_cost(best):
            best = individual
    return best

# Crossover function (ordered crossover)
def ordered_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, k), 2))
    child = [None] * (k + 1)
    child[0], child[-1] = 0, 0  # Start and end at depot
    child[start:end+1] = parent1[start:end+1]
    
    filled_positions = set(parent1[start:end+1])
    fill_pos = end + 1
    for i in range(1, k):
        if parent2[i] not in filled_positions:
            if fill_pos >= k:
                fill_pos = 1
            while child[fill_pos] is not None:
                fill_pos += 1
            child[fill_pos] = parent2[i]
            filled_positions.add(parent2[i])
    
    return child

# Mutation function (swap mutation)
def swap_mutation(tour):
    idx1, idx2 = sorted(random.sample(range(1, k), 2))
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return tour

# Genetic algorithm execution
population = generate_initial_population()
best_tour = None

for _ in range(num_generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child1 = ordered_crossover(parent1, parent2)
        child2 = ordered_crossover(parent2, parent1)
        if random.random() < mutation_rate:
            child1 = swap_mutation(child1)
        if random.random() < mutation_rate:
            child2 = swap_mutation(child2)
        new_population.extend([child1, child2])
    
    population = new_population  # Replace old population with new generation
    current_best = min(population, key=calculate_tour_cost)
    if best_tour is None or calculate_tour_cost(current_best) < calculate_tour_cost(best_tour):
        best_tour = current_best

# Output
tour_cost = calculate_tour_cost(best_tour)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {tour_cost}")