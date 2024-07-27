import random
import math

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Parameters
num_cities = len(cities)
population_size = 100
generations = 200
tournament_size = 20
mutation_rate = 0.15

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def fitness(tour):
    """ Calculate the fitness which is the max distance between consecutive cities in the list. """
    max_dist = 0
    total_dist = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        total_dist += dist
        if dist > max_dist:
            max_dist = dist
    return max_dist, total_dist

def generate_initial_population():
    """ Generate initial random population """
    population = []
    for _ in range(population_size):
        tour = list(range(1, num_cities))
        random.shuffle(tour)
        tour = [0] + tour + [0]  # start and end at the depot
        population.append(tour)
    return population

def tournament_selection(population, fitnesses):
    """ Select the best one from randomly selected multiple tours from the population """
    tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
    return min(tournament, key=lambda x: x[1])[0]

def ordered_crossover(parent1, parent2):
    """ Perform ordered crossover to produce new offspring """
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end] = parent1[start:end]
    filled = set(parent1[start:end])
    pos = end
    for city in parent2:
        if city not in filled:
            if pos >= size:
                pos = 0
            while child[pos] is not None:
                pos = (pos + 1) % size
            child[pos] = city
    return child

def mutate(tour):
    """ Mutate the tour by swapping two cities """
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour) - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]

# Genetic Algorithm Implementation
population = generate_initial_population()
best_tour = None
best_fitness = float('inf')
best_total_distance = None

for generation in range(generations):
    new_population = []
    fitnesses = [fitness(tour) for tour in population]
    for _ in range(population_size):
        parent1 = tournament_selection(population, fitnesses)
        parent2 = tournament_selection(population, fitnesses)
        child = ordered_crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)

    population = new_population

    # Check for the best solution
    for tour in population:
        fit, total_dist = fitness(tour)
        if fit < best_fitness:
            best_fitness = fit
            best_total_distance = total_dist
            best_tour = tour

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {best_fitness:.2f}")