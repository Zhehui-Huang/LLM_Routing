import numpy as np
import random
from scipy.spatial import distance

# City coordinates including the depots
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(city_coords[route[i]], city_coords[route[i + 1]])
    return cost

def generate_initial_population(size, num_cities):
    population = []
    for i in range(size):
        perm = np.random.permutation(range(2, num_cities + 2))
        # Split roughly in half for simplicity, adjustments could be made for a more balanced distribution
        split_idx = len(perm) // 2
        population.append([perm[:split_idx], perm[split_idx:]])
    return population

def crossover(parent1, parent2):
    """ Apply crossover operation between two parents to produce two children """
    cut_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:cut_point] + [p for p in parent2 if p not in parent1[:cut_point]]
    child2 = parent2[:cut_point] + [p for p in parent1 if p not in parent2[:cut_point]]
    return child1, child2

def mutate(route):
    """ Apply mutation, randomly swapping two cities """
    idx1, idx2 = random.sample(range(len(route)), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]

def genetic_algorithm(pop_size=50, generations=100):
    population = generate_initial_population(pop_size, len(city_coords) - 2)
    for _ in range(generations):
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = random.choices(population, k=2)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
    
    # Find the best solution
    best_solution = min(population, key=lambda route: calculate_route_cost([0]+route[0]+[0]) + calculate_route_cost([1]+route[1]+[1]))
    return best_solution

# Final function call
best_routes = genetic_algorithm()
robot0_route = [0] + best_routes[0] + [0]
robot1_route = [1] + best_routes[1] + [1]

robot0_cost = calculate_route_cost(robot0_route)
robot1_cost = calculate_route_cost(robot1_route)
overall_cost = robot0_cost + robot1_cost

print("Robot 0 Tour:", robot0_route)
print("Robot 0 Total Travel Cost:", robot0_cost)
print("Robot 1 Tour:", robot1_route)
print("Robot 1 Total Travel Cost:", robot1_cost)
print("Overall Total Travel Cost:", overall_cost)