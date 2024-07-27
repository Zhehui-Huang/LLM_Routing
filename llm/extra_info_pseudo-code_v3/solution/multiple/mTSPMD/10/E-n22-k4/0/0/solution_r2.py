import random
import numpy as np

# Define the city coordinates (including depots)
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 197), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Define depot assignments
depots = [0, 1, 2, 3]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Genetic Algorithm Parameters
num_robots = len(depots)
population_size = 100
generations = 500
mutation_rate = 0.1

# Initialize a random population
def initial_population():
    population = []
    all_cities = list(cities.keys())
    non_depot_cities = [city for city in all_cities if city not in depots]
    
    for _ in range(population_size):
        random.shuffle(non_depot_cities)
        splits = np.array_split(non_depot_cities, num_robots)
        tours = [[depots[i]] + list(split) + [depots[i]] for i, split in enumerate(splits)]
        population.append(tours)
    
    return population

# Calculate tour cost
def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Calculate chromosome fitness
def chromosome_fitness(chromosome):
    return sum(tour_cost(tour) for tour in chromosome)

# Genetic operations
def select_parents(population):
    total_fitness = sum(1/chromosome_fitness(chromo) for chromo in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for chromosome in population:
        current += 1/chromosome_fitness(chromosome)
        if current > pick:
            return chromosome

def crossover(parent1, parent2):   # Applying a simple one-point crossover for each robot's tour
    child = []
    for i in range(num_robots):
        pt = random.randint(1, len(parent1[i]) - 2)
        child.append(parent1[i][:pt] + [c for c in parent2[i] if c not in parent1[i][:pt]])
    return child

def mutate(chromosome):
    for i in range(num_robots):
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(1, len(chromosome[i])-1), 2)
            chromosome[i][idx1], chromosome[i][idx2] = chromosome[i][idx2], chromosome[i][idx1]
    return chromosome

# Running the Genetic Algorithm
def genetic_algorithm():
    population = initial_population()
    best_fitness = float('inf')
    best_solution = None
    
    for _ in range(generations):
        new_population = []
        
        while len(new_population) < population_size:
            parent1 = select_parents(population)
            parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
            
        population = new_population
        current_best = min(population, key=chromosome_fitness)
        current_fitness = chromosome_fitness(current_best)
        
        if current_fitness < best_fitness:
            best_fitness = current_fitness
            best_solution = current_best
    
    return best_solution

best_routes = genetic_algorithm()
overall_cost = sum(tour_cost(route) for route in best_routes)

# Output results
for i, route in enumerate(best_routes):
    route_cost = tour_cost(route)
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")