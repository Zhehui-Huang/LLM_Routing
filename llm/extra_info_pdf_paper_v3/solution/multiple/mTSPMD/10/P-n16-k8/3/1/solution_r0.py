import numpy as np
import random
from math import sqrt

# Define cities by coordinates [id: (x, y)]
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initial population size and number of generations
POP_SIZE = 100
GENERATIONS = 500

# Number of salesmen (robots) which is also the number of depots
number_of_salesmen = 8
depot_cities = list(range(number_of_salesmen))

# Tournament size for selection
TOURNAMENT_SIZE = 5


def generate_initial_population():
    population = []
    non_depot_cities = list(set(cities.keys()) - set(depot_cities))
    for _ in range(POP_SIZE):
        for depot in depot_cities:
            path = [depot] + random.sample(non_depot_cities, len(non_depot_cities)) + [depot]
            population.append(path)
    return population

def calculate_total_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += calculate_distance(path[i], path[i+1])
    return total_distance

def tournament_selection(population, scores):
    tournament = random.sample(list(zip(population, scores)), TOURNAMENT_SIZE)
    tournament.sort(key=lambda x: x[1])
    return tournament[0][0]

def perform_pmx(parent1, parent2):
    """Perform the Partially Matched Crossover."""
    size = len(parent1)
    p1, p2 = [0]*size, [0]*size

    # Initialize the position of each indices in the individuals
    for i in range(size):
        p1[parent1[i]] = i
        p2[parent2[i]] = i

    # Choose crossover points
    cx1, cx2 = sorted(random.sample(range(size), 2))
    temp = parent1[cx1:cx2 + 1]
    parent1[cx1:cx2 + 1] = parent2[cx1:cx2 + 1]
    parent2[cx1:cx2 + 1] = temp

    return parent1, parent2

def two_opt_swap(route):
    """Improves an existing route using the 2-opt swap."""
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]
                if calculate_total_distance(new_route) < calculate_total_distance(best):
                    best = new_route
                    improved = True
        route = best
    return best

def genetic_algorithm():
    population = generate_initial_population()
    best_score = float('inf')
    best_tour = None

    for generation in range(GENERATIONS):
        # Evaluate the fitness of each individual
        scores = [calculate_total_distance(individual) for individual in population]
        
        # Check for new best score
        for score, individual in zip(scores, population):
            if score < best_score:
                best_score = score
                best_tour = individual

        # Selection
        new_population = []
        for _ in range(POP_SIZE // 2):
            parent1 = tournament_selection(population, scores)
            parent2 = tournament_selection(population, scores)
            child1, child2 = perform_pmx(parent1, parent2)
            new_population.append(child1)
            new_population.append(child2)

        # Mutation
        population = [two_opt_swap(individual) for individual in new_population]
        
    return best_tour, best_score

best_tour, best_score = genetic_algorithm()
print("Best Tour:", best_tour)
print("Best Total Travel Cost:", best_score)