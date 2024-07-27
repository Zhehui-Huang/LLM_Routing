import numpy as np
import random
from scipy.spatial.distance import euclidean

# Cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Robots Information
num_robots = 8
depot = 0  # All robots start from city 0

# Helper function to calculate distance between cities
def calc_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Generate a random tour, simple random permutation with home depot at start and end.
def generate_random_tour():
    city_list = list(cities.keys())
    city_list.remove(depot)
    random.shuffle(city_list)
    return [depot] + city_list + [depot]

# Validate if all cities are visited exactly once in the tours
def validate_solution(tours):
    all_cities = set(range(len(cities)))
    visited_cities = set()
    for tour in tours:
        visited_cities.update(set(tour))
    return visited_cities == all_cities

# Calculate the total travel cost of tours
def calculate_cost(tours):
    total_cost = 0
    costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += calc_distance(tour[i], tour[i + 1])
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

# Dummy genetic operations and selection (to be implemented)
def crossover(parent1, parent2):
    return parent1, parent2

def mutate(tour):
    return tour

def select_parents(population):
    return population[0], population[1]

# Genetic Algorithm main loop (simplified)
def genetic_algorithm(max_generations=100):
    population = [generate_random_tour() for _ in range(10)]
    best_solution = None
    best_cost = float('inf')
    
    for generation in range(max_generations):
        new_population = []
        while len(new_population) < len(population):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])
        
        population = new_population
        for individual in population:
            tours = [individual]  # Only one tour per robot in this simplified example
            if validate_solution(tours):
                _, cost = calculate_cost(tours)
                if cost < best_cost:
                    best_cost = cost
                    best_solution = tours
    
    return best_solution, best_cost

# Running the Genetic Algorithm
solution, total_cost = genetic_algorithm()
costs, overall_cost = calculate_cost(solution)

# Output the results
for idx, tour in enumerate(solution):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")
print(f"Overall Total Travel Cost: {overall_cost}")