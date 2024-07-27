import numpy as np
import random

# Coordinates of the cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Depots for each robot
depots = [0, 1, 2, 3, 4, 5, 6, 7]

# Helper functions
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_tour_cost(tour):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Genetic Algorithm specific functions
def create_population(size, num_cities, depots):
    population = []
    for _ in range(size):
        # shuffle non-depot cities
        cities = list(set(range(num_cities)) - set(depots))
        random.shuffle(cities)
        # Distribute cities between robots
        individuals = []
        split_sizes = np.array_split(cities, len(depots))
        for index, depot in enumerate(depots):
            tour = [depot] + list(split_sizes[index]) + [depot]
            individuals.append(tour)
        population.append(individuals)
    return population

def fitness(tours):
    return sum(calculate_tour_cost(tour) for tour in tours)

def selection(population, method='tournament', k=3):
    selected = []
    while len(selected) < len(population) // 2:
        if method == 'tournament':
            contenders = random.sample(population, k)
            winner = min(contenders, key=fitness)
            selected.append(winner)
    return selected

def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        tour = random.choice(individual)
        a, b = random.sample(range(1, len(tour) - 1), 2)  # avoiding depots
        tour[a], tour[b] = tour[b], tour[a]
    return individual

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-2)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Main Genetic Algorithm running function
def genetic_algorithm(coordinates, depots, population_size=100, generations=500):
    num_cities = len(coordinates)
    population = create_population(population_size, num_cities, depots)
    
    for _ in range(generations):
        population = selection(population) + selection(population)
        next_generation = []
        while len(next_generation) < population_size:
            if len(population) > 1:
                p1, p2 = random.sample(population, 2)
                offspring1, offspring2 = crossover(p1, p2)
                next_generation.extend([mutate(offspring1), mutate(offspring2)])
        population = next_generation
    
    # Get the best solution
    best_solution = min(population, key=fitness)
    best_cost = fitness(best_solution)
    return best_solution, best_cost

# Run the genetic algorithm
best_solution, best_cost = genetic_algorithm(coordinates, depots)

# Output the results
total_cost = 0
for idx, tour in enumerate(best_solution):
    tour_cost = calculate_tour_cost(tour)
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {round(tour_cost, 2)}")
print(f"Overall Total Travel Cost: {round(total_cost, 2)}")