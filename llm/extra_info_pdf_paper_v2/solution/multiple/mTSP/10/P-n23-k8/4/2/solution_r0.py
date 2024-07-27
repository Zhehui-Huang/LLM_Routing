import math
import random

# Coordinates for the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate distance matrix
n = len(coordinates)
distance_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Number of robots
num_robots = 8

# Genetic Algorithm Parameters
population_size = 50
generations = 500
mutation_rate = 0.15

# Initialize population
def create_individual():
    cities = list(range(1, n))  # Exclude the depot city for now
    random.shuffle(cities)
    return cities

def split_tours(solution):
    splits = sorted(random.sample(range(1, len(solution)), num_robots - 1))
    return [solution[i:j] for i, j in zip([0]+splits, splits+[None])]

def calculate_cost(tours):
    total_cost = 0
    results = []
    for tour in tours:
        tour_cost = distance_matrix[0][tour[0]]  # Start at depot
        for i in range(len(tour) - 1):
            tour_cost += distance_matrix[tour[i]][tour[i+1]]
        tour_cost += distance_matrix[tour[-1]][0]  # Return to depot
        results.append(tour_cost)
        total_cost += tour_cost
    return total_cost, results

def fitness(individual):
    tours = split_tours(individual)
    total_cost, _ = calculate_cost(tours)
    return total_cost

# Genetic operations
def select(population, scores):
    sorted_population = sorted(zip(scores, population), key=lambda x: x[0])
    return [ind for _, ind in sorted_population[:population_size//2]]

def crossover(parent1, parent2):
    cut = random.randint(0, len(parent1) - 1)
    child = parent1[:cut] + [c for c in parent2 if c not in parent1[:cut]]
    assert len(child) == len(parent1)
    return child

def mutate(individual):
    for _ in range(len(individual)):
        if random.random() < mutation ourate:
            idx1, idx2 = random.sample(range(len(individual)), 2)
            individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Create initial population
population = [create_individual() for _ in range(population_size)]
best_solution = None
best_score = float('inf')

# Run GA
for gen in range(generations):
    # Evaluate
    scores = [fitness(ind) for ind in population]
    current_best = min(scores)
    if current_best < best_score:
        best_score = current

            scores.index(current_best)]
        print(f"Best score at generation {gen}: {best_score}")

    # Selection
    selected = select(population, scores)
    # Crossover and mutation
    offspring = list(selected)
    while len(offspring) < population_size:
        if len(offspring) < population_size - 1:
            parent1, parent2 = random.sample(selected, 2)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            offspring.append(mutate(child1))
            offspring.append(mutate(child2))
        else:
            child = mutate(random.choice(selected))
            offspring.append(child)
    population = offspring

# Output solution
best_tours = split_tours(best_solution)
_, costs = calculate_cost(best_tours)
overall_cost = sum(costs)
print(f"Overall Total Travel Cost: {overall_cost}")
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {[0] + tour + [0]}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")