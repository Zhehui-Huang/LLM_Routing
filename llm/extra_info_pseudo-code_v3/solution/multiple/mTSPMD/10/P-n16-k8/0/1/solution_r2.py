import numpy as anp
import random

# City coordinates include depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Initialize cities and depots
depots = list(range(8))
cities = list(range(8, 16))

# Function to calculate distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Genetic Algorithm configuration
num_generations = 500
population_size = 50
mutation_rate = 0.01

# Create an initial population of random tours
def create_population(depot, num_individuals):
    return [[depot] + random.sample(cities, len(cities)) + [depot] for _ in range(num_individuals)]

# Fitness evaluation (total tour distance)
def evaluate_tour(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Tournament selection
def tournament_selection(population, k=3):
    selected = random.choices(population, k=k)
    selected.sort(key=evaluate_tour)
    return selected[0]

# Ordered Crossover
def ordered_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1)-1), 2))
    child = [None]*len(parent1)
    child[start:end+1] = parent1[start:end+1]
    
    fill = (city for city in parent2 if city not in child)
    child = [next(fill) if x is None else x for x in child]
    child[0], child[-1] = parent1[0], parent1[-1]
    return child

# Mutation: Swap two elements
def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour)-1), 2)
        tour[i], tour[j] = tour[j], tour[i]

# Run the Genetic Algorithm for a single robot
def genetic_algorithm(depot):
    population = create_population(depot, population_size)
    for _ in range(num_generations):
        new_population = []
        for _ in range(population_size):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = ordered_crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population
    best_tour = min(population, key=evaluate_tour)
    return best_tour, evaluate_tour(best_tour)

# Execute the GA for each robot
total_cost = 0
for depot in depots:
    tour, cost = genetic_algorithm(depot)
    total_cost += cost
    print(f"Robot starting at depot {depot} Tour: {tour}")
    print(f"Robot starting at depot {depot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")