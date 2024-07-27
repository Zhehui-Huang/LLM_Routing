import random
from math import sqrt

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Parameters
num_robots = 8
population_size = 50
generations = 100
mutation_rate = 0.15
crossover_rate = 0.85

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def generate_initial_population():
    population = []
    for _ in range(population_size):
        tour = list(cities.keys())
        random.shuffle(tour)
        population.append(tour)
    return population

def calculate_total_distance(tour):
    distance = 0
    for i in range(1, len(tour)):
        distance += euclidean_distance(tour[i - 1], tour[i])
    return distance

def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return parent1, parent2
    cross_pt1, cross_pt2 = sorted(random.sample(range(len(parent1)), 2))
    child1_mid = parent2[cross_pt1:cross_pt2]
    child1 = [city for city in parent1 if city not in child1_mid]
    child1 = child1[:cross_pt1] + child1_mid + child1[cross_pt1:]
    return child1, child1  # Creating two children for simplicity

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def select_parents(population):
    return random.choices(population, k=2)

# Main Genetic Algorithm
population = generate_initial_population()
for _ in range(generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1, parent2 = select_parents(population)
        child1, child2 = crossover(parent1, parent2)
        new_population.append(mutate(child1))
        new_population.append(mutate(child2))
    population = sorted(new_population, key=calculate_total_distance)[:population_size]

# Display the best solution
best_solution = min(population, key=calculate_total_distance)
best_solution_distance = calculate_total_distance(best_solution)
print("Best Solution Tour:", best_solution)
print("Total Distance:", best_solution_distance)