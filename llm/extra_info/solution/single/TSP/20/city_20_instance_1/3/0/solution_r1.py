import numpy as np
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

def genetic_algorithm(population, population_size, elite_size, mutation_rate, generations):
    for generation in range(generations):
        ranked_pop = sorted(population, key=lambda x: route_distance(x))
        selection = ranked_pop[:elite_size]  # Elitism
        while len(selection) < population_size:  # Breed until population filled
            parent1 = random.choice(ranked_pop[:50])  # Top 50
            parent2 = random.choice(ranked_mpop[:50])  # Top 50
            if random.random() < 0.85:  # Crossover probability
                child = parent1[:len(parent1)//2] + [x for x in parent2 if x not in parent1[:len(parent1)//2]]
                if random.random() < mutation_rate:
                    swi1, swi2 = random.sample(range(1, len(child)), 2)
                    child[swi1], child[swi2] = child[swi2], child[swi1]
                selection.append(child)
        population = selection
    return sorted(population, key=lambda x: route_distance(x))[0]

# Creating initial population
def create_population(pop_size, cities):
    return [random.sample(list(range(1, len(cities))), len(cities)-1) for _ in range(pop_size)]

# Genetic algorithm parameters
n_cities = len(coordinates)
pop_size = 100
elite_size = 20
mutation_rate = 0.03  # Slightly increased mutation rate
generations = 1000  # More generations for better convergence

# Initial Population
initial_population = create_population(pop_size, coordinates)

# Execute Genetic Algorithm
best_route = genetic_algorithm(initial_population, pop_size, elite_size, mutation_rate, generations)
best_route = [0] + best_route + [0]
total_cost = route_distance(best_route)

# Output formatting
print(f"Tour: {best_route}")
print(f"Total travel cost: {round(total_cost, 2)}")