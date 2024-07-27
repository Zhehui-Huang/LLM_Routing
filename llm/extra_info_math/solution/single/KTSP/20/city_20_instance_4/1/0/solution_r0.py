import math
import random
from itertools import permutations

# Fixed Cities and their coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two points"""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a list of city indices excluding the depot
city_indices = list(cities.keys())[1:]

# Function to evaluate the total path cost
def evaluate_tour(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Implementing Genetic Algorithm
def create_initial_population(size, city_list):
    population = []
    for _ in range(size):
        individual = random.sample(city_list, len(city_list))
        population.append(individual)
    return population

def crossover(parent1, parent2):
    size = len(parent1)
    idx1, idx2 = sorted(random.sample(range(size), 2))
    offspring = parent1[idx1:idx2] + [x for x in parent2 if x not in parent1[idx1:idx2]]
    return offspring

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]
    return individual

def genetic_algorithm(city_list, population_size, generations):
    # Create initial population
    population = create_initial_population(population_size, city_list)
    for _ in range(generations):
        # Evaluate fitness and sort
        population = sorted(population, key=lambda x: evaluate_tour([0] + x + [0]))
        # Crossover and mutation
        new_population = []
        top_performers = population[:int(0.2 * population_size)]
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(top_performers, 2)
            offspring = crossover(parent1, parent2)
            offspring = mutate(offspring, mutation_rate=0.15)
            new_population.append(offspring)
        population = new_population
    best_solution = sorted(population, key=lambda x: evaluate_tour([0] + x + [0]))[0]
    return [0] + best_solution + [0]

# Run GA to solve the k-TSP with 16 selected cities including the depot
selected_cities = random.sample(city_indices, 15)  # Select 15 additional cities
best_tour = genetic_algorithm(selected_cities, population_size=100, generations=500)
total_cost = evaluate_tour(best_tour)

# Output
print("Tour:", best_tour)
print("Total travel cost:", total_cost)