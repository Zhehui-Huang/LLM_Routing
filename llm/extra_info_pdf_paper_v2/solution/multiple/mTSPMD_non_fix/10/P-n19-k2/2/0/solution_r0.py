import numpy as np
import random

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculating Euclidean distances between each pair of cities
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def compute_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost

# Genetic Algorithm Functions
def create_route():
    route = list(range(2, len(coordinates)))  # Exclude depots
    random.shuffle(route)
    return route

def compute_fitness(route, depot):
    complete_route = [depot] + route
    return 1 / compute_cost(complete_route)

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None]*len(parent1)
    child[start:end+1] = parent1[start:end+1]
    
    for i in range(len(parent2)):
        if not parent2[i] in child:
            for j in range(len(child)):
                if child[j] is None:
                    child[j] = parent2[i]
                    break
    return child

def mutate(route, mutation_rate):
    if random.random() < mutation_MUTATION_RATE:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

def ga_solve(depots, population_size, generations, mutation_rate, crossover_rate):
    population = [create_route() for _ in range(population_size)]
    best_solution = None
    best_cost = float('inf')
    
    for generation in range(generations):
        weighted_population = []
        for route in population:
            for depot in depots:
                fitness = compute_fitness(route, depot)
                if fitness > 1 / best_cost:
                    best_cost = 1 / fitness
                    best_solution = ([depot] + route + [depot], best_cost)
                weighted_population.append((route, fitness))
        
        population = []
        weights = [fitness for _, fitness in weighted_population]
        total_weight = sum(weights)
        probabilities = [weight / total_weight for weight in weights]
        
        while len(population) < population_size:
            parent1, parent2 = random.choices(weighted_population, weights=probabilities, k=2)
            if random.random() < crossover_rate:
                child = crossover(parent1[0], parent2[0])
            else:
                child = parent1[0] if parent1[1] > parent2[1] else parent2[0]
            
            mutate(child, mutation_rate)
            population.append(child)
    
    return best_solution

# Constants
POPULATION_SIZE = 100
GENERATIONS = 500
MUTATION_RATE = 0.03
CROSSOVER_RATE = 0.7

solution = ga_solve([0, 1], POPULATION_SIZE, GENERATIONS, MUTATION_RATE, CROSSOVER_RATE)
robot_0_tour, robot_0_cost = solution if solution[0][0] == 0 else (None, None)
robot_1_tour, robot_1_cost = solution if solution[0][0] == 1 else (None, None)

print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}")
print(f"Overall Total Travel Cost: {robot_0_cost + robot_1_cost}")