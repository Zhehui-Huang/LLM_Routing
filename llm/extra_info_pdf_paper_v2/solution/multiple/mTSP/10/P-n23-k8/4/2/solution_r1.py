import math
import random

# Coordinates for the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Distance matrix
n = len(coordinates)
distance_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Parameters
num_robots = 8
population_size = 50
generations = 500
mutation_rate = 0.15

# Create a random tour
def create_individual():
    cities = list(range(1, n))
    random.shuffle(cities)
    return cities

# Split tours for each robot
def split_tours(solution):
    splits = sorted(random.sample(range(1, len(solution)), num_robots - 1))
    return [solution[i:j] for i, j in zip([0] + splits, splits + [None])]

# Calculate the cost of the tours
def calculate_cost(tours):
    total_cost = 0
    costs = []
    for tour in tours:
        tour_cost = distance_matrix[0][tour[0]]  # From depot to first city in the tour
        for i in range(len(tour) - 1):
            tour_cost += distance_matrix[tour[i]][tour[i + 1]]
        tour_cost += distance_matrix[tour[-1]][0]  # Return to depot from last city
        costs.append(tour_cost)
        total_cost += tour_cost
    return total_cost, costs

def fitness(individual):
    tours = split_tours(individual)
    total_cost, _ = calculate_cost(tours)
    return total_cost

# Genetic operations
def select(population, scores):
    selected = [x for _, x in sorted(zip(scores, population), key=lambda x: x[0])][:population_size//2]
    return selected

def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1) - 1)
    child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
    return child

def mutate(individual):
    individual = individual[:]
    for _ in range(int(len(individual) * mutation_rate)):
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Create initial population
population = [create_individual() for _ in range(population_size)]
best_solution = None
best_score = float('inf')

# Genetic algorithm
for gen in range(generations):
    scores = [fitness(individual) for individual in population]
    min_score = min(scores)
    if min_score < best_score:
        best_score = min_score
        best_solution = population[scores.index(min_score)]
        print(f"Generation {gen}: Best Score: {best_score}")

    # Selection
    selected = select(population, scores)
    population = [mutate(crossover(random.choice(selected), random.choice(selected))) for _ in range(population_size)]

# Calculate final result tours and costs
best_tours = split_tours(best_solution)
total_cost, costs = calculate_cost(best_tours)

print(f"Overall Total Travel Cost: {total_cost}")
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {['0'] + [str(city) for city in tour] + ['0']}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")