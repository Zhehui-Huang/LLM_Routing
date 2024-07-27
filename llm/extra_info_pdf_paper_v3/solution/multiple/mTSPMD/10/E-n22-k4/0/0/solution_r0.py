import numpy as onp
import random
from math import sqrt
from itertools import permutations

# Defining City Coordinates and Robot Information
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214),
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

depot_locations = {0: 0, 1: 1, 2: 2, 3: 3}
robots = len(depot_locations)

# Calculating Distances
distance_matrix = [[sqrt((cities[i][0]-cities[j][0])**2 + (cities[i][1]-cities[j][1])**2) for j in cities] for i in cities]

def calculate_total_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# GA Setup
population_size = 100
generations = 500
mutation_rate = 0.1

def generate_initial_population():
    population = []
    cities_to_visit = list(cities.keys())[4:]  # cities excluding depots
    for _ in range(population_size):
        random.shuffle(cities_to_visit)
        full_tour = []
        division_points = sorted(random.sample(range(1, len(cities_to_visit)), robots - 1))
        segments = [cities_to_visit[i:j] for i, j in zip([0] + division_points, division_points + [None])]
        for idx, segment in enumerate(segments):
            tour = [depot_locations[idx]] + segment + [depot_locations[idx]]
            full_tour.extend(tour)
        population.append(full_tour)
    return population

def crossover(parent1, parent2):
    # Implementing Partially Matched Crossover (PMX) as described, with modifications for multiple depots
    size = len(parent1)
    p, q = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[p:q+1] = parent1[p:q+1]
    for i in range(p, q+1):
        if parent2[i] not in child:
            j = i
            while p <= j <= q:
                j = parent2.index(parent1[j])
            child[j] = parent2[i]
    child = [item if item is not None else parent2[i] for i, item in enumerate(child)]
    return child

def mutate(tour):
    # Implementing 2-opt mutation
    i, j = sorted(random.sample(range(len(tour)), 2))
    tour[i:j] = tour[i:j][::-1]

def selection(population):
    # Roulette wheel selection
    max_fit = sum(calculate_total_distance(individual) for individual in population)
    pick = random.uniform(0, max_fit)
    current = 0
    for individual in population:
        current += calculate_total_distance(individual)
        if current > pick:
            return individual

def genetic_algorithm():
    population = generate_initial_population()
    for generation in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                mutate(child)
            new_population.append(child)
        population = new_population
    
    # Evaluation
    best_solution = min(population, key=calculate_total_distance)
    return best_solution

# Run the Genetic Algorithm
best_individual = genetic_algorithm()

# Extract individual robot paths from combined tour
robot_tours = {robot_id: [] for robot_id in depot_locations.values()}
current_robot = 0
for city in best_individual:
    robot_tours[current_robot].append(city)
    if len(robot_tours[current_robot]) > 1 and robot_tours[current_robot][-1] in depot_locations.values():
        current_robot = city

# Display results
total_cost = 0
for robot_id, tour in robot_tours.items():
    robot_cost = calculate_total_distance(tour)
    total_cost += robot_cost
    print(f'Robot {robot_id} Tour: {tour}')
    print(f'Robot {robot_id} Total Travel Cost: {robot_cost}')

print("Overall Total Travel Cost:", total_cost)