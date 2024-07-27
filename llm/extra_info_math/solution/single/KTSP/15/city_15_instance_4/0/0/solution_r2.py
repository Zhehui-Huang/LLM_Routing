import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to compute the total distance of the tour
def total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

# Generate initial population of tours randomly
def generate_initial_population(pop_size, cities):
    population = []
    for _ in range(pop_size):
        tour = [0] + random.sample(cities, 11) + [0]  # Starting and ending at the depot city 0
        population.append(tour)
    return population

# Tournament selection for crossover parent selection
def tournament_selection(population, coordinates, tournament_size=5):
    tournament = random.sample(population, tournament_size)
    return min(tournament, key=lambda tour: total_distance(tour, coordinates))

# Crossover to produce offspring from two parents
def ordered_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    child = [None] * len(parent1)
    child[0], child[-1] = 0, 0  # Ensure start and end at the depot
    child[start:end] = parent1[start:end]
    child_places = set(parent1[start:end])

    fill_idx = 1
    for city in parent2:
        if city not in child_places and city != 0:
            while child[fill_idx] is not None:
                fill_idx += 1
            child[fill_idx] = city
            fill_idx += 1

    return child

# Mutation by swapping two cities in the tour
def mutate(tour, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour) - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]

# Genetic algorithm for solving the TSP
def genetic_algorithm(coordinates, population_size, n_generations):
    cities = list(range(1, len(coordinates)))  # city indices except the depot
    population = generate_initial_population(population_size, cities)

    for _ in range(n_generations):
        new_population = []
        for _ in range(population_size):
            parent1 = tournament_selection(population, coordinates)
            parent2 = tournament_selection(population, coordinates)
            child = ordered_crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population

    best_tour = min(population, key=lambda tour: total_distance(tour, coordinates))
    return best_tour, total_distance(best_tour, coordinates)

# City coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Solve the problem
best_tour, best_distance = genetic_algorithm(coordinates, population_size=100, n_generations=500)
print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 2))