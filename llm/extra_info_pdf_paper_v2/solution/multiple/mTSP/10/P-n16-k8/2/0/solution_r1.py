import numpy as np
import math
import random

# Define the cities coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots
num_robots = 8

# Distance function
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create initial individuals
def generate_random_tour():
    tour = list(range(1, len(cities)))  # exclude the depot
    random.shuffle(tour)
    return tour

# Fitness function calculates total distance
def calculate_cost(tours):
    total_cost = 0
    detailed_costs = []
    for tour in tours:
        cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        detailed_costs.append(cost)
        total_cost += cost
    return total_cost, detailed_costs

# Divides single tour into multiple tours for each robot
def split_tour(individual):
    size_per_robot = len(individual) // num_robots
    remainder = len(individual) % num_robots
    tours = []
    start_index = 0
    for i in range(num_robots):
        end_index = start_index + size_per_robot + (1 if i < remainder else 0)
        tour = [0] + individual[start_index:end_index] + [0]
        tours.append(tour)
        start_index = end_index
    return tours

# Genetic Algorithm Operators
def crossover(p1, p2):
    child = []
    cut_points = sorted(random.sample(range(1, len(p1)), 2))  # exclude 0 to ensure cuts within city list
    child[p1[:cut_points[0]]] + p1[cut_points[1]:]
    middle_section = [city for city in p2 if city not in child]
    child = child[:cut_points[0]] + middle_section + child[cut_points[0]:]
    return child

def mutate(tour, mutation_rate=0.05):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]

# Main Genetic Algorithm
def genetic_algorithm(pop_size=50, generations=300):
    population = [generate_random_tour() for _ in range(pop_size)]

    for _ in range(generations):
        # Evaluate
        fitness_scores = []
        for individual in population:
            tours = split_tour(individual)
            cost, _ = calculate_cost(tours)
            fitness_scores.append((cost, individual))
        
        # Selection
        fitness_scores.sort(key=lambda x: x[0])  # Sort by cost
        population = [x[1] for x in fitness_scores[:pop_size // 2]]  # Select top 50% 

        # Crossover & Mutation
        new_population = population[:]
        while len(new_population) < pop_size:
            parents = random.sample(population, 2)
            child = crossover(parents[0], parents[1])
            mutate(child)
            new_estimator.append(child)

        population = new_population

    best = min([(calculate_cost(split_tour(x)), x) for x in population], key=lambda x: x[0][0])
    return best

# Solve the problem using the genetic algorithm
best_solution, best_individual = genetic_algorithm()

# Printing the results
best_tours = split_tour(best_individual)
total_cost, detailed_costs = calculate_cost(best_tours)
print("Overall Total Travel Cost:", total_cost)
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {detailed.Render Costs[idx]}")