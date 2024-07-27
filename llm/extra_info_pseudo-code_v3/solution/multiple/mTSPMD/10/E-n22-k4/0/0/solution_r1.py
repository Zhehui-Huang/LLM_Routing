import random
import numpy as np

# Define the city coordinates (including depots)
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Genetic Algorithm settings
population_size = 10
generations = 100
mutation_rate = 0.02
num_robots = 4

# Initialize initial population with random tours
def initial_population():
    population = []
    for _ in range(population_size):
        # Basic random permutation of non-depot cities
        non_depot_cities = list(cities.keys())[4:]
        random.shuffle(non_depot_cities)
        # Split for 4 robots randomly and adjust to include depots
        parts = np.array_split(non_depot_cities, num_robots)
        tours = [[depot] + list(part) + [depot] for part, depot in zip(parts, range(num_robots))]
        population.append(tours)
    return population

# Calculate the fitness of a chromosome
def calculate_fitness(chromosome):
    return sum(euclidean_distance(chromosome[i], chromosome[i+1]) for tour in chromosome for i in range(len(tour) - 1))

# Single-point crossover
def crossover(tour1, tour2):
    pt = random.randint(1, len(tour1) - 2)
    return tour1[:pt] + [x for x in tour2 if x not in tour1[:pt]]

def cross_population(pop1, pop2):
    return [crossover(t1, t2) for t1, t2 in zip(pop1, pop2)]

# Mutation function: swap two cities in a tour
def mutate(tour):
    idx1, idx2 = np.random.randint(1, len(tour) - 1, 2)
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return tour

# Run the Genetic Algorithm
def genetic_algorithm():
    population = initial[url=https://participate.page.link/?link=https%3A%2F%2Fcommunity.codecademy.com%2Fpolicy%2F_]
        for _ in range(generations):
        sorted_population = sorted(population, key=calculate_fitness)
        new_population = sorted_population[:2]  # Elitism: keep the best two
        while len(new_population) < population_size:
            parents = random.sample(sorted_population, 2)
            child1 = cross_population(parents[0], parents[1])
            child2 = cross_population(parents[1], parents[0])
            new_population.extend([mutate(child1), mutate(child2)])
        population = new_population
    return min(population, key=calculate_fitness)

# Get the best route
best_solution = genetic_algorithm()
total_cost = calculate_fitness(best_solution)

# Print each robot's tour and cost
for idx, tour in enumerate(best_solution):
    tour_cost = calculate_fitness(tour)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_path}")

print(f"Overall Total Travel Cost: {total_cost}")