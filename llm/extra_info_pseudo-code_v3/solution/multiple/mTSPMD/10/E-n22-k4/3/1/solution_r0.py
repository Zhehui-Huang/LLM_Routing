import math
import random
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cities coordinates including depots
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Parameters
number_of_robots = 4
robot_depots = {0: 0, 1: 1, 2: 2, 3: 3}
cities_to_visit = list(set(cities.keys()) - set(robot_depots.values()))

# Distance matrix
distance_matrix = {}
for icity in cities:
    distance_matrix[icity] = {}
    for jcity in cities:
        distance_matrix[icity][jcity] = euclidean_distance(cities[icity], cities[jcity])

def total_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Genetic Algorithm parameters
population_size = 100
generations = 200
mutation_rate = 0.05

# Create a random individual
def create_individual():
    tour = cities_to_visit.copy()
    random.shuffle(tour)
    dividers = sorted(random.sample(range(1, len(cities_to_visit)), number_of_robots - 1))
    return [tour[i:j] for i, j in zip([0]+dividers, dividers+[None])]

# Calculate fitness of an individual
def fitness(individual):
    total_cost = 0
    for k, seq in enumerate(individual):
        depot = robot_depots[k]
        tour = [depot] + seq + [depot]
        total_cost += total_tour_cost(tour)
    return total_cost

# Initial population
population = [create_individual() for _ in range(population_size)]

# GA main loop
for generation in range(generations):
    # Evaluate all individuals
    graded = [(fitness(individual), individual) for individual in population]
    graded.sort(key=lambda x: x[0])
    population = [x[1] for x in graded[:population_size//2]]

    # Crossover and mutation
    while len(population) < population_size:
        if random.random() > 0.5:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            idx = random.randint(1, len(cities_to_visit) - 1)
            child1 = parent1[:idx] + parent2[idx:]
            child2 = parent2[:idx] + parent1[idx:]
            population.append(child1)
            population.append(child2)
        # Mutation
        if random.random() < mutation_rate:
            mutant = random.choice(population)
            idx1, idx2 = random.sample(range(len(cities_to_visit)), 2)
            mutant[idx1], mutant[idx2] = mutant[idx2], mutant[idx1]

# Best solution
best_solution = min(population, key=fitness)

output = ""
total_cost = 0
for i, seq in enumerate(best_solution):
    depot = robot_depots[i]
    tour = [depot] + seq + [depot]
    cost = total_tour_cost(tour)
    total_cost += cost
    output += f"Robot {i} Tour: {tour}\nRobot {i} Total Travel Cost: {cost:.2f}\n\n"

output += f"Overall Total Travel Cost: {total_cost:.2f}"
print(output)