import random
import math
from itertools import permutations

# City coordinates (indexed by city number, including depots)
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
          (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
          (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
          (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
          (45, 35)]

# Defining the number of robots
num_robots = 2
depots = [0, 1]  # Depot corresponding to each robot

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Generate a random tour, returns the tour and its cost
def generate_random_tour(depot):
    tour = list(range(2, len(cities)))  # Exclude depots initially
    random.shuffle(tour)
    tour = [depot] + tour + [depot]
    cost = total_tour_cost(tour)
    return tour, cost

# Main Genetic Algorithm
def genetic_algorithm():
    population_size = 50
    generations = 500
    mutation_rate = 0.1

    # Initialize population
    population = [generate_random_tour(depots[i % num_robots]) for i in range(population_size)]
    sorted_population = sorted(population, key=lambda x: x[1])

    # Genetic Algorithm Loop
    for generation in range(generations):
        new_population = sorted_population[:2]  # Elitism: carry forward the best 2 tours

        # Create next generation
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(sorted_population[:20], 2)  # Tournament Selection
            child1, child2 = crossover(parent1[0], parent2[0])
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.append((child1, total_tour_cost(child1)))
            new_population.append((child2, total_tour_cost(child2)))

        sorted_population = sorted(new_population, key=lambda x: x[1])

    return sorted_population[0]

def crossover(tour1, tour2):
    size = len(tour1)
    p1, p2 = sorted(random.sample(range(1, size-1), 2))  # ensure not to slice depots
    child1 = tour1[:p1] + [c for c in tour2 if c not in tour1[:p1]]  # Ordered Crossover
    child2 = tour2[:p1] + [c for c in tour1 if c not in tour2[:p1]]
    return child1, child2

def mutate(tour, rate):
    if random.random() < rate:
        p1, p2 = sorted(random.sample(range(1, len(tour)-1), 2))
        tour[p1:p2] = reversed(tour[p1:p2])  # Inversion Mutation
    return tour

best_solution = genetic_algorithm()

# Output the results
print(f"Robot 0 Tour: {best_solution[0]}")
print(f"Robot 0 Total Travel Cost: {best_solution[1]}")

# You'd run genetic_algorithm for each robot (modifying the generate_random_tour to constrain tours to their initial depots) 
# and add handling to ensure city visit uniqueness across robots if you don't split cities beforehand.