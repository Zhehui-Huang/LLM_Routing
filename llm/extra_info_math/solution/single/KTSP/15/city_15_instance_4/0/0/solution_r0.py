import random
import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_population(pop_size, cities):
    population = []
    for _ in range(pop_size):
        tour = random.sample(cities, len(cities))
        tour.insert(0, 0)  # Start at the depot city
        tour.append(0)     # End at the depot city
        population.append(tour)
    return population

def fitness(tour, coordinates):
    return -total_distance(tour, coordinates)

def selection(population, coordinates, tournament_size=5):
    tournament = random.sample(population, tournament_size)
    fitnesses = [fitness(tour, coordinates) for tour in tournament]
    return tournament[fitnesses.index(max(fitnesses))]

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    child = [None]*len(parent1)
    child[start:end] = parent1[start:end]
    child[0], child[-1] = 0, 0  # Ensure depot city is at start and end
    for city in parent2[1:-1]:
        if city not in child:
            for i in range(1, len(child) - 1):
                if child[i] is None:
                    child[i] = city
                    break
    return child

def mutate(tour, mutation_rate=0.05):
    if random.random() < mutation_rate:
        i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
        tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm(coordinates, population_size, n_generations):
    cities = list(range(1, 15))
    random.shuffle(cities)
    cities = cities[:11]  # Select any 11 other cities along with the depot
    population = generate_initial_population(population_size, cities)

    for generation in range(n_generations):
        new_population = []
        for _ in range(population_size):
            parent1 = selection(population, coordinates)
            parent2 = selection(population, coordinates)
            child = crossover(parent1, parent2)
            mutate(child)
            new超population.append(child)

        population = new_population

    best_tour = min(population, key=lambda tour: total_distance(tour, coordinates))
    return best_tour, total_distance(best_tour, coordinates)

# City coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

best_tour, best_distance = genetic_algorithm(coordinates, population_size=100, n_generations=500)
print("Tour:", best_tour)
print("Total travel cost:", best_distance)