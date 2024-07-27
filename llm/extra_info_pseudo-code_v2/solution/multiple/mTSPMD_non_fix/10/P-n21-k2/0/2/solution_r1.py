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
    """Calculate Euclidean distance between two points."""
    return distance.euclidean(p1, p2)

def calculate_route_cost(route):
    """Calculate the total travel cost of a route based on city indices."""
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_get_distance(city_coords[route[i]], city_coords[route[i + 1]])
    return cost

def generate_initial_population(size, num_cities):
    """Generate a random initial population of route permutations for a given number of cities."""
    population = []
    all_cities = list(range(2, num_cities + 2))  # city indices excluding depots
    for _ in range(size):
        random.shuffle(all_cities)
        split = len(all_cities) // 2
        population.append([all_cities[:split], all_cities[split:]])
    return population

def crossover(parent1, parent2):
    """Crossover operation to produce offspring from two parent routes."""
    size = len(parent1[0]) + len(parent1[1])
    cut1, cut2 = sorted(random.sample(range(2, size), 2))
    
    def make_child(p1, p2):
        child = [-1] * size
        middle_gen = p1[cut1:cut2]
        child[cut1:cut2] = middle_gen
        
        fill_index = list(range(cut1)) + list(range(cut2, size))
        fill_values = [gene for gene in p2[0] + p2[1] if gene not in middle_gen]
        for idx, value in zip(fill_index, fill_values):
            child[idx] = value
        return child
    
    return [make_child(parent1, parent2), make_child(parent2, parent1)]

def mutate(route):
    """Mutate a route by swapping two random cities."""
    idx1, idx2 = random.sample(range(len(route)), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]

def genetic_algorithm(pop_size=100, generations=200):
    """Run the genetic algorithm to find the best routes for the robots."""
    num_cities = len(city_coords) - 2
    population = generate_initial_population(pop_size, num_cities)
    
    for _ in range(generations):
        new_population = []
        for parent1, parent2 in zip(population[0::2], population[1::2]):
            children = crossover(parent1, parent2)
            for child in children:
                mutate(child[0])
                mutate(child[1])
                new_population.append(child)
        population = sorted(new_population, key=lambda x: calculate_route_cost([0]+x[0]+[0]) + calculate_route_cost([1]+x[1]+[1]))
        population = population[:pop_size]

    return population[0]

# Running the genetic algorithm
solution = genetic_algorithm()
robot0_route = [0] + solution[0] + [0]
robot1_route = [1] + solution[1] + [1]

robot0_cost = calculate_route_cost(robot0_route)
robot1_cost = calculate_route_cost(robot1_route)
overall_cost = robot0_cost + robot1_cost

print("Robot 0 Tour:", robot0_route)
print("Robot 0 Total Travel Cost:", robot0_cost)
print("Robot 1 Tour:", robot1_route)
print("Robot 1 Total Travel Cost:", robot1_cost)
print("Overall Total Travel Cost:", overall_cost)