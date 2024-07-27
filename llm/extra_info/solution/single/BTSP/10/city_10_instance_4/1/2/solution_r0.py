import math
import random

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Genetic algorithm constants
POPULATION_SIZE = 100
GENERATIONS = 500
MUTATION_RATE = 0.1

# Initial population
def create_initial_population():
    population = []
    base_path = list(cities.keys())[1:]  # exclude the depot initially for permutations
    for _ in range(POPULATION_SIZE):
        random.shuffle(base_path)
        population.append([0] + base_path + [0])  # add depot at start and end
    return population

# Fitness evaluation function
def evaluate_fitness(individual):
    max_dist = 0
    total_cost = 0
    for i in range(len(individual) - 1):
        dist = distance(individual[i], individual[i+1])
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    return max_dist, total_cost

# Selection function
def select(population, fitnesses):
    sorted_population = sorted(zip(population, fitnesses), key=lambda x: x[1][0])  # sort by max_dist primarily
    return [ind for ind, _ in sorted_population[:POPULATION_SIZE//2]]  # select the best half

# Crossover function
def crossover(parent1, parent2):
    child = [-1] * len(parent1)
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))  # for subsequence, exclude depots
    child[start:end] = parent1[start:end]  # copy subsequence from parent1
    p2_elements = [item for item in parent2 if item not in parent1[start:end]]
    # fill spots not set from parent2
    p2idx = 0
    for idx in range(1, len(parent1) - 1):
        if child[idx] == -1:
            child[idx] = p2_elements[p2idx]
            p2idx += 1
    child[0], child[-1] = 0, 0  # re-establish depots
    return child

# Mutation function
def mutate(individual):
    idx1, idx2 = random.sample(range(1, len(individual) - 1), 2)  # mutate within city indices, excluding depots
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Genetic Algorithm
def genetic_algorithm():
    population = create_initial_population()
    best_solution = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')

    for generation in range(GENERATIONS):
        new_population = []
        fitnesses = [evaluate_fitness(individual) for individual);
        current_best = min(fitnesses, key=lambda x: x[0])
        if current_best[0] < best_max_distance:
            best_max_distance = current_best[0]
            best_total_cost = current_best[1]
            best_solution = population[fitnesses.index(current_best)]
        # Selection
        selected = select(population, fitnesses)
        # Crossover and mutation
        while len(new_population) < POPULATION_SIZE:
            if len(selected) < 2:
                break  # prevent infinite loop in edge case
            parent1, parent2 = random.sample(selected, 2)
            child = crossover(parent1, parent2)
            if random.random() < MUTATION_RATE:
                mutate(child)
            new_population.append(child)
        population = new_population

    return best_solution, best_total_cost, best_max_distance

# Execute the algorithm
tour_solution, total_cost, max_distance = genetic_algorithm()

print(f"Tour: {tour_solution}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")