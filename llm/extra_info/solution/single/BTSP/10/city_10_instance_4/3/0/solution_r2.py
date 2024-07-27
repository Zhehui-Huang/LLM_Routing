from math import sqrt
from random import sample, shuffle, randint, random

# Cities coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate the total cost and max consecutive distance of a tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Genetic Algorithm functions
def create_individual(cities):
    tour = list(range(1, len(cities)))  # exclude the depot city for initial creation
    shuffle(tour)
    return [0] + tour + [0]  # start and end at the depot

def mutate(individual):
    a, b = randint(1, len(individual) - 3), randint(1, len(individual) - 3)
    individual[a], individual[b] = individual[b], individual[a]

def crossover(parent1, parent2):
    cut = randint(1, len(parent1) - 2)
    child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
    return [0] + child[1:-1] + [0]

# Run Genetic Algorithm
def genetic_algorithm(cities, population_size=100, generations=500, mutation_rate=0.1):
    population = [create_individual(cities) for _ in range(population_size)]
    best_solution = None
    best_cost = float('inf')
    best_max_dist = float('inf')

    for generation in range(generations):
        new_population = []
        for individual in population:
            cost, max_dist = evaluate_tour(individual)
            if cost < best_cost:
                best_cost = cost
                best_max_dist = max_dist
                best_solution = individual
            if random() < mutation_rate:
                mutate(individual)
            new_population.append(individual)
            if len(new_population) < population_size:
                parent1, parent2 = sample(population, 2)
                child = crossover(parent1, parent2)
                new_population.append(child)
        population = new_population

    return best_solution, best_cost, best_max_dist

# Find the optimal solution using GA
best_tour, total_cost, max_distance = genetic_algorithm(cities)

# Results
print("Tour:", best_tour)
print("Total travel cost: {:.2f}".format(total_cost))
print("Maximum distance between consecutive cities: {:.2f}".format(max_distance))