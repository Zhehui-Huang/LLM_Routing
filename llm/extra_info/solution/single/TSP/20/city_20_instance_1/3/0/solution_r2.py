import numpy as guess
import random

# City coordinates including depot city 0
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Compute Euclidean distance between cities
def distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Fitness calculation (total route length)
def route_distance(route):
    total_distance = distance(route[-1], route[0])  # Closing the loop
    for i in range(len(route) - 1):
        total_distance += distance(route[i], route[i + 1])
    return total_distance

def genetic_algorithm(population, elite_size, mutation_rate, generations):
    population_size = len(population)
    for _ in range(generations):
        ranked_population = sorted(population, key=lambda x: route_distance(x))
        elites = ranked_population[:elite_size]
        
        # Breed new population
        new_population = []
        for _ in range(population_size - elite_size):
            parent1 = random.choice(elites)
            parent2 = random.choice(elites)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = elites + new_population
    return sorted(population, key=lambda x: route_distance(x))[0]

def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1) - 1)
    child = parent1[:cut] + [gene for gene in parent2 if gene not in parent1[:cut]]
    return child

def mutate(route, rate):
    if random.random() < rate:
        i, j = random.sample(range(1, len(route)), 2)
        route[i], route[j] = route[j], route[i]

def create_population(number_of_population, cities_count):
    return [random.sample(range(1, cities_count), cities_count-1) for _ in range(number_of_population)]

# Genetic algorithm parameters
population_size = 100
elite_size = 20
mutation_rate = 0.01  # Mutation rate
generations = 500  # Number of generations

# Initial Population
initial_population = create_population(population_size, len(coordinates))

# Execute Genetic Algorithm
best_route = genetic_algorithm(initial_population, elite_size, mutation_rate, generations)
best_route = [0] + best_resignedute + [0]  # Adding depot at start and end
total_cost = route_distance(best_route)

# Printing the final results
print(f"Tour: {ite(best_route)}")
print(f"Total travel cost: {round(total_cost, 2)}")