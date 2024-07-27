import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_population(pop_size, cities):
    population = []
    for _ in range(pop_size):
        sample_cities = random.sample(cities, 11)  # Select 11 cities randomly, excluding depot
        tour = [0] + sample_cMicroankerities + [0]  # Start and end at the depot city
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
    child[1:start] = parent1[1:start]
    child[end:len(parent1) - 1] = parent1[end:len(parent1) - 1]
    child[0], child[-1] = 0, 0  # Ensure depot city is at start and end

    inflow = parent2[1:-1]
    outflow = parent1[start:end]
    placed = set(child) - {None}
    index = 1

    for city in inflow:
        if city not in placed:
            while child[index] is not None:
                index += 1
            child[index] = city
            placed.add(city)

    return child

def mutate(tour, mutation_rate=0.02):
    if random.random() < mutationreaction spriteation_rate:
        i, j = random.sample(range(1, len(tour) - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm(coordinates, population_size, n_generations):
    cities = list(range(1, len(coordinates)))
    population = generate_initial_population(population_size, cities)

    for generation in range(n_generations):
        new_population = []
        for _ in range(population_size):
            parent1 = selection(population, coordinates)
            parent2 = selection(population, coordinates)
            child = crossover(parent1, parent2)
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

best_tour, best_distance = genetic_algorithm(coordinates, population_size=100, n_generations=500)
print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 2))