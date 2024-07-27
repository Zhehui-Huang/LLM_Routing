import numpy as np
import random
import copy

# City coordinates and determination of the distance matrix
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate distance matrix
N = len(cities)
distances = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        distances[i, j] = euclidean_distance(cities[i], cities[j])

# Genetic Algorithm parameters
num_robots = 8
depots = list(range(8))
population_size = 100
generations = 500
mutation_rate = 0.1
tournament_size = 5

# Initial population generation
def generate_individual():
    non_depots = [i for i in range(N) if i not in depots]
    random.shuffle(non_depots)
    return non_depots

def generate_population():
    return [generate_individual() for _ in range(population_size)]

# Calculate total distance of routes
def calculate_total_distance(routes):
    total_distance = 0
    route_distances = []
    for route in routes:
        route_distance = sum(distances[route[i], route[i+1]] for i in range(len(route)-1))
        route_distances.append(route_distance)
        total_distance += route_distance
    return total_distance, route_distances

# Assign cities to robots by splitting an individual's genes
def assign_to_robots(individual):
    split_points = sorted(random.sample(range(1, len(individual)), num_robots - 1))
    cities_per_robot = np.split(individual, split_points)
    routes = [[depots[i]] + list(cities) + [depots[i]] for i, cities in enumerate(cities_per_robot)]
    return routes

# Genetic operators
def crossover(parent1, parent2):
    child = parent1[:]
    for i in range(1, len(parent2) - 1):
        if random.random() < crossover_rate:
            swap_index = child.index(parent2[i])
            child[i], child[swap_index] = child[swap_index], child[i]
    return child

def mutate(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]

def tournament_selection(population, scores):
    selected = random.choices(list(zip(population, scores)), k=tournament_size)
    selected.sort(key=lambda x: x[1])
    return selected[0][0]

# Main genetic algorithm execution
population = generate_population()
best_solution = None
lowest_cost = float('inf')

for gen in range(generations):
    new_population = []
    scores = []
    
    for individual in population:
        routes = assign_to_robots(individual)
        total_distance, _ = calculate_total_distance(routes)
        scores.append(total_distance)
        if total_distance < lowest_cost:
            best_solution = routes
            lowest_cost = total_distance
    
    for _ in range(population_size):
        parent1 = tournament_selection(population, scores)
        parent2 = tournament_selection(population, scores)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)
    
    population = new_population

# Output results
for idx, route in enumerate(best_solution):
    _, route_costs = calculate_total_distance([route])
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_costs[0]}")
print(f"Overall Total Travel Cost: {lowest_cost}")