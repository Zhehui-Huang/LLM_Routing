import numpy as np
from scipy.spatial.distance import euclidean
from random import sample, randint, random
from itertools import permutations

# Coordinates for each city, including depot cities at their respective starting indices
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 196), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

depots = [0, 1, 2, 3]

# Create a distance matrix between each pair of cities
def compute_distance_matrix(cities):
    num_cities = len(cities)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                matrix[i, j] = euclidean(cities[i], cities[j])
    return matrix

distance_matrix = compute_against_distance_matrix(cities)

# Number of robots (each robot corresponds to a depot)
num_robots = 4

# Genetic Algorithm Configuration
population_size = 100
num_generations = 1000
mutation_rate = 0.15

# Initialize Population-based genetic algorithm
def initialize_population():
    population = []
    all_cities = list(cities.keys())
    tour_cities = [c for c in all_cities if c not in depots]
    
    for _ in range(population_size):
        random_tour = sample(tour_cities, len(tour_cities))
        split_sizes = sorted(sample(range(1, len(random_tour)), num_robots-1))
        individual_tours = []
        start = 0
        for index in split_sizes:
            individual_tours.append(random_tour[start:index])
            start = index
        individual_tours.append(random_tour[start:])
        population.append(individual_tours)
    return population

def evaluate_individual(individual):
    total_cost = 0
    for depot, tour in enumerate(individual):
        if tour:
            total_cost += distance_matrix[depots[depot]][tour[0]]
            for i in range(len(tour)-1):
                total_cost += distance_matrix[tour[i]][tour[i+1]]
            total_cost += distance_matrix[tour[-1]][depots[depot]]
    return total_cost

def select_parents(population, fitnesses):
    sorted_population = [x for _, x in sorted(zip(fitnesses, population), key=lambda pair: pair[0])]
    return sorted_population[:2]

def crossover(parent1, parent2):
    child = []
    for tours1, tours2 in zip(parent1,parent2):
        if random() > 0.5:
            child.append(tours1)
        else:
            child.append(tours2)
    return child

def mutate(individual):
    for tour in individual:
        if random() < mutation_rate and len(tour) > 2:
            i, j = randint(0, len(tour) - 1), randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm():
    population = initialize_population()
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_generators):
        fitnesses = [evaluate_individual(individual) for individual in population]
        new_population = []
        while len(new_population) < population_size:
            parents = select_parents(population, fitnesses)
            child = crossover(parents[0], parents[1])
            mutate(child)
            new_population.append(child)
        population = new_population
        
        # Track the best solution
        for individual, cost in zip(population, fitnesses):
            if cost < best_cost:
                best_cost = cost
                best_solution = individual
    
    return best_solution, best_cost

best_solution, best_cost = genetic_algorithm()

# Print results
print("Optimal Tours:")
for robot_id, tour in enumerate(best_solution):
    full_tour = [depots[robot_id]] + tour + [depots[robot_id]]
    print(f"Robot {robot_id} Tour: {full_tour}")
    cost = evaluate_individual([tour])
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {best_cost:.2f}")