import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i, j] = euclidean(cities[i], cities[j])

# Genetic Algorithm setup
population_size = 50
generations = 1000
mutation_rate = 0.1
num_robots = 2
split_size = (num_cities - 2) // num_robots

# Initialization random split tours
population = []
for _ in range(population_size):
    tour = list(range(2, num_cities)) # without depots
    random.shuffle(tour)
    population.append(tour)

def calculate_cost(tour):
    total_cost = 0
    robot_tours = []
    start_index = 0
    for r in range(num_robots):
        end_index = start_index + split_size + (1 if r < (num_cities - 2) % num_robots else 0)
        robot_tour = [0] + tour[start_index:end_index] + [0]  # start and end at depot 0
        robot_tours.append(robot_tour)
        start_index = end_index
        # Calculate cost for this robot
        for i in range(len(robot_tour) - 1):
            total_cost += dist_matrix[robot_tour[i], robot_tour[i + 1]]
    return total_cost, robot_tours

def crossover(parent1, parent2):
    size = len(parent1)
    idx1, idx2 = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[idx1:idx2] = parent1[idx1:idx2]
    # Fill the remaining slots with cities from parent2 without repetition
    pos = idx2
    for city in parent2:
        if city not in child:
            if pos >= size:
                pos = 0
            child[pos] = city
            pos += 1
    return child

def mutate(tour):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(tour)), 2)
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

def select(population):
    fitnesses = [1 / calculate_cost(tour)[0] for tour in population]
    total_fitness = sum(fitnesses)
    probs = [f / total_fitness for f in fitnesses]
    return population[np.random.choice(len(population), p=probs)]

# Genetic Algorithm Execution
best_solution = None
best_cost = float('inf')

for generation in range(generations):
    new_population = []
    for _ in range(population_size):
        parent1 = select(population)
        parent2 = select(population)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)
    population = new_population
    # Optionally evaluate best solution in each generation
    for solution in population:
        cost, _ = calculate_cost(solution)
        if cost < best_cost:
            best_cost = cost
            best_solution = solution

# Calculate the best solution's details
final_cost, final_robot_tours = calculate_cost(best_solution)

print(f"Overall Total Travel Cost: {final_cost}")
for idx, tour in enumerate(final_robot_tours):
    print(f"Robot {idx} Tour: {tour}")
    tour_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")