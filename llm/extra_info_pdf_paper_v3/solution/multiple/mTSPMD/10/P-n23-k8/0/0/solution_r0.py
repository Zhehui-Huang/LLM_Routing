import math
import random
from itertools import combinations

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

### Step 2: Define Genetic Algorithm Components

# Create an initial random solution
def create_initial_solution(depot, non_depot_cities):
    random.shuffle(non_depot_cities)
    return [depot] + non_depot_cities + [depot]

# Fitness calculation
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Mutation: 2-opt swap
def two_opt_swap(tour):
    new_tour = tour[:]
    l = len(tour) - 2
    if l > 2:
        i, j = sorted(random.sample(range(1, l), 2))
        new_tour[i:j+1] = reversed(new_tour[i:j+1])
    return new_tour

# Selection: Tournament
def tournament_selection(population, scores, k=3):
    selected_indices = random.sample(range(len(population)), k)
    selected_scores = [scores[i] for i in selected_indices]
    return population[selected_indices[selected_scores.index(min(selected_scores))]]

# Crossover: Partially Matched Crossover (PMX)
def pmx(parent1, parent2):
    l = len(parent1)
    a, b = sorted(random.sample(range(l), 2))
    child = [None]*l
    child[a:b] = parent1[a:b]
    for i in range(a, b):
        val = parent2[i]
        while val in child:
            idx = parent2.index(parent1[i])
            val = parent2[idx]
        child[child.index(None)] = val
    child = [item if item is not None else parent2[i] for i, item in enumerate(child)]
    return child

### Step 3: Run Genetic Algorithm

def genetic_algorithm(depot, cities, iterations=500):
    non_depot_cities = [c for c in cities if c != depot]
    population_size = 50
    population = [create_initial_solution(depot, non_depot_cities) for _ in range(population_size)]
    scores = [calculate_tour_cost(ind) for ind in population]
    
    for _ in range(iterations):
        new_population = []
        for _ in range(population_size):
            parent1 = tournament_selection(population, scores)
            parent2 = tournament_selection(population, scores)
            child = pmx(parent1, parent2)
            child = two_opt_swap(child)
            new_population.append(child)
        population = new_population
        scores = [calculate_tour_cost(ind) for ind in population]
    
    best_score = min(scores)
    best_tour = population[scores.index(best_score)]
    return best_tour, best_score

### Step 4: Aggregate Solutions for All Robots
total_cost = 0
for robot_id in range(8):
    depot = robot_id
    cities_copy = cities.copy()
    solution, cost = genetic_algorithm(depot, cities_copy)
    print(f'Robot {robot_id} Tour: {solution}')
    print(f'Robot {robot_id} Total Travel Cost: {cost}')
    total_cost += cost

print(f'Overall Total Travel Cost: {total_cost}')