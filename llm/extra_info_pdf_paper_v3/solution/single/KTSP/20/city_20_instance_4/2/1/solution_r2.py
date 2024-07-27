import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def generate_initial_population(subset, population_size):
    population = []
    for _ in range(population_size):
        sample = random.sample(subset, len(subset))
        population.append(sample)
    return population

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    total_distance += euclidean_distance(cities[tour[-1]], cities[tour[0]])  # Return to depot
    return total_distance

def select_parents(population, tour_lengths):
    weights = [1/x for x in tour_lengths]
    parents = random.choices(population, weights=weights, k=2)
    return parents

def crossover(parent1, parent2):
    cut_point = random.randint(1, len(parent1) - 2)
    child = parent1[:cut_point] + [city for city in parent2 if city not in parent1[:cut_point]]
    return child

def mutate(tour, mutation_rate):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(k, generations=500, population_size=50, mutation_rate=0.05):
    subset = random.sample(list(cities.keys())[1:], k-1)  # excluding the depot
    subset.insert(0, 0)  # start from the depot
    population = generate_initial_population(subset, population_size)
    for _ in range(generations):
        tour_lengths = [calculate_total_distance(tour) for tour in population]
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population, tour_lengths)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    # Find the best tour in the final population
    best_tour = min(population, key=calculate_total_distance)
    best_tour.append(0)  # ensure round trip
    return best_tour

# Define k
k = 16
best_tour = genetic_algorithm(k)
total_distance = calculate_total_distance(best_tour)

print("Tour:", best_tour)
print("Total travel cost:", total_distance)