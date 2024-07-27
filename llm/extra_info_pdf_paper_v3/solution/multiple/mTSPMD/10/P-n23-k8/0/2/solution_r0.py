import numpy as np
import random
from itertools import permutations

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Depots for each robot
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_robots = len(depots)

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def create_initial_population(pop_size, num_cities, num_robots):
    population = []
    for _ in range(pop_size):
        cities_permutation = np.random.permutation([x for x in range(num_cities) if x not in depots])
        split_points = sorted(random.sample(range(1, num_cities - num_robots), num_robots - 1))
        robot_tours = np.split(cities_permutation, split_points)
        chromosomes = []
        for idx, tour in enumerate(robot_tours):
            chromosomes.append([depots[idx]] + list(tour) + [depots[idx]])
        population.append(chromosomes)
    return population

def selection(population, fitness):
    sorted_population = sorted(zip(population, fitness), key=lambda x: x[1])
    return [x[0] for x in sorted_population[:len(population)//2]]

def crossover(parent1, parent2):
    # Simple one-point crossover
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate_tour(tour):
    i, j = random.sample(range(1, len(tour) - 1), 2)  # Exclude depots
    tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(coordinates, num_robots, generations=1000, pop_size=50):
    num_cities = len(coordinates)
    population = create_initial_population(pop_size, num_cities, num_robots)
    for _ in range(generations):
        # Calculate the fitness of the population
        fitness = [sum(calculate_tour_cost(robot_tour) for robot_tour in individual) for individual in population]
        selected = selection(population, fitness)
        # Create a new population
        new_population = selected.copy()
        while len(new_population) < pop_size:
            if len(selected) >= 2:
                p1, p2 = random.sample(selected, 2)
                for child in crossover(p1, p2):
                    new_population.append([mutate_tour(tour) for tour in child])
        population = new_population
    # Final selection and result
    final_fitness = [sum(calculate_tour_cost(robot_tour) for robot_tour in individual) for individual in population]
    best_index = np.argmin(final_fitness)
    best_solution = population[best_index]
    return best_solution, final_fitness[best_index]

# Execute the GA
best_solution, best_cost = genetic_algorithm(coordinates, num_robots)

# Output the solution
total_cost = 0
for robot_id, tour in enumerate(best_solution):
    tour_cost = calculate_tour_cost(tour)
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {round(tour_cost, 2)}")
print(f"Overall Total Travel Cost: {round(total_cost, 2)}")