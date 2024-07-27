import numpy as np
import random
from math import sqrt

# Coordinates of cities including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

depots = [0, 1, 2, 3]

def calculate_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def create_initial_solution():
    cities = list(range(4, len(coordinates)))  # All cities excluding depots
    random.shuffle(cities)
    # Split cities approximately evenly among the robots
    num_cities_per_robot = len(cities) // len(depots)
    solutions = []
    start_index = 0

    for depot in depots:
        end_index = start_index + num_cities_per_robot
        robot_cities = cities[start_index:end_index]
        tour = [depot] + robot_cities + [depot]
        solutions.append(tour)
        start_index = end_index

    # Adjust in case of non-even division
    if end_index < len(cities):
        solutions[-1].extend(cities[end_index:])
        solutions[-1].append(depots[-1])

    return solutions

def fitness(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i + 1])
    return cost

def genetic_algorithm():
    population = [create_initial_solution() for _ in range(200)]
    generations = 1000
    
    for _ in range(generations):
        # Evaluate fitness for each individual in the population
        fitness_scores = [(individual, sum(fitness(tour) for tour in individual)) for individual in population]
        fitness_scores.sort(key=lambda x:x[1])  # Sort by total travel cost
        best_individual = fitness_scores[0][0]  # Best solution with the least cost
        top_20_percent = fitness_scores[:len(population) // 5]

        new_generation = [x[0] for x in top_20_percent]
        while len(new_generation) < len(population):
            parent1, parent2 = random.sample(top_20_percent, 2)
            child = crossover(parent1[0], parent2[0])
            mutate(child)
            new_generation.append(child)

        population = new_generation
    return best_individual

def crossover(parent1, parent2):
    child = []
    for tours1, tours2 in zip(parent1, parent2):
        start = random.randint(0, len(tours1) - 2)
        end = random.randint(start + 1, len(tours1) - 1)
        mid_part = tours1[start:end]
        mid_part_set = set(mid_part)
        remaining_cities = [city for city in tours2 if city not in mid_part_set]
        new_tour = remaining_cities[:start] + mid_part + remaining_cities[start:]
        child.append(new_tour)
    return child

def mutate(solution, mutation_rate=0.1):
    for tour in solution:
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, len(tour) - 1), 2)
            tour[i], tour[j] = tour[j], tour[i]

solution = genetic_algorithm()

overall_cost = 0
for idx, robot_tour in enumerate(solution):
    tour_cost = fitness(robot_tour)
    overall_cost += tour_cost
    print(f"Robot {idx} Tour: {robot_tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")