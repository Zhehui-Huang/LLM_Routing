import numpy as np
import random
import math

# City coordinates and depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

depots = [0, 1, 2, 3]
cities = list(range(4, 22))
num_robots = 4

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# GA Parameters
population_size = 100
generations = 500
mutation_rate = 0.05

# Genetic Algorithm Functions
def create_individual(cities):
    tour = cities[:]
    random.shuffle(tour)
    sizes = np.array_split(tour, num_robots)
    for i in range(len(sizes)):
        sizes[i] = list(sizes[i])
        sizes[i].insert(0, depots[i])
        sizes[i].append(depots[i])
    return sizes

def population_initialization():
    return [create_individual(cities) for _ in range(population_size)]

def fitness(individual):
    return sum(distance(individual[i][j], individual[i][j+1]) for i in range(num_robots) for j in range(len(individual[i])-1))

def crossover(parent1, parent2):
    # Use Partially Matched Crossover (PMX) here for simplicity
    cp = random.randint(1, len(cities) - 2)
    child1 = [-1] * len(cities)
    child2 = [-1] * len(cities)

    # Copy slice
    child1[:cp] = parent1[:cp]
    child2[:cp] = parent2[:cp]

    # Fill the child with the remaining cities
    for i in range(len(cities)):
        if parent2[i] not in child1:
            child1[child1.index(-1)] = parent2[i]
        if parent1[i] not in child2:
            child2[child2.index(-1)] = parent1[i]
    
    return [create_individual(child1), create_individual(child2)]

def mutate(individual):
    for route in individual:
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, len(route) - 1), 2)  # Avoid depot positions
            route[i], route[j] = route[j], route[i]

def selection(population):
    sorted_population = sorted(population, key=fitness)
    return sorted_population[:2]  # Keep the 2 best

# Initialize population
pop = population_initialization()

# Run the GA
for generation in range(generations):
    new_population = []
    while len(new_population) < population_size:
        parent1, parent2 = random.choices(pop, k=2)
        child1, child2 = crossover(parent1, parent2)
        mutate(child1)
        mutate(child2)
        new_population.extend([child1, child2])
    pop = selection(new_population + pop)

# Select the best solution
best_solution = min(pop, key=fitness)
best_cost = fitness(best_solution)

# Output the results
total_travel_cost = 0
for i in range(num_robots):
    robot_tour = best_solution[i]
    robot_cost = sum(distance(robot_tour[j], robot_tour[j+1]) for j in range(len(robot_tour)-1))
    total_travel_cost += robot_cost
    print(f"Robot {i} Tour: {robot_tour}")
    print(f"Robot {i} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")