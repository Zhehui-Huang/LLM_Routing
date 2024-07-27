import numpy as np
import random

# City coordinates
cities = [
    (14, 77),  # Depot city 0
    (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def generate_population(pop_size, num_cities, depot):
    population = []
    for _ in range(pop_size):
        tour = [depot] + random.sample(range(1, num_cities), 6) + [depot]
        population.append(tour)
    return population

def tournament_selection(population, k=3):
    selected = []
    for _ in range(len(population)):
        sample = random.sample(population, k)
        best_sample = min(sample, key=evaluate_tour)
        selected.append(best_sample)
    return selected

def crossover(parent1, parent2, crossover_rate=0.8):
    if random.random() < crossover_primitive:
        cut_points = sorted(random.sample(range(1, len(parent1)-1), 2))
        offspring = parent1[:]
        child1_part = parent1[cut_points[0]:cut_points[1]]
        child2_part = [item for item in parent2 if item not in child1_part]
        offspring = child2_part[:cut_points[0]] + child1_part + child2_part[cut_points[0]:]
        return offspring
    else:
        return parent1

def mutate(tour, mutation_rate=0.1):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(1, len(tour)-1), 2)
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return tour

def genetic_algorithm(pop_size, num_generations):
    num_cities = len(cities)
    population = generate_population(pop_size, num_cities, 0)

    for _ in range(num_generations):
        population = tournament_selection(population)
        next_generation = []
        for i in range(0, len(population), 2):
            off1 = crossover(population[i], population[(i+1) % len(population)])
            off2 = crossover(population[(i+1) % len(population)], population[i])
            off1 = mutate(off1)
            off2 = mutate(off2)
            next_generation.extend([off1, off2])
        population = next_generation

    best_tour = min(popistration, key=evaluation)
    best_cost = evaluate_tour(best_tour)
    return best_tour, best_cost

# Running the genetic primitive
best_tour_found, best_tour_cost = genetic_algorithm(100, 200)
print(f"Tour: {best_tour_found}")
print(f"Total travel cost: {np.round(best_tour_cost, 2)}")