import numpy as np
import math
import random

# Define city coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots
num_robots = 8

# Distance using Euclidean distance formula
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Genetic algorithm core functions
def generate_individual():
    tour = list(range(1, len(cities)))
    random.shuffle(tour)
    return tour

# Evaluate the distance cost
def evaluate(tour):
    # Split tour among robots
    subtours = []
    for i in range(num_robots):
        subtours.append([0])
    
    # Distribute cities to the robots' subtours
    for i, city in enumerate(tour):
        subtours[i % num_robots].append(city)
    
    # Add depot return (0) to each subtour
    for subtour in subtours:
        subtour.append(0)
    
    overall_cost = 0
    costs = []
    for subtour in subtours:
        tour_cost = sum(distance(subtour[i], subtour[i+1]) for i in range(len(subtour) - 1))
        overall_cost += tour_cost
        costs.append(tour_cost)
    return overall_cost, subtours, costs

# Random parent selection
def select_parent(population):
    return population[random.randint(0, len(population) - 1)]

# Breeding via crossover
def crossover(parent1, parent2):
    child = []
    cut = sorted(random.sample(range(len(parent1)), 2))
    gene1 = parent1[cut[0]:cut[1]]
    child = [item for item in parent2 if item not in gene1]
    return child[:cut[0]] + gene1 + child[cut[0]:]

# Genetic algorithm mutation
def mutate(individual, mutation_rate=0.1):
    for swap in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(individual))
            individual[swap], individual[swap_with] = individual[swap_with], individual[swap]

# Genetic Algorithm
def genetic_algorithm(population_size=100, generations=100):
    population = [generate_individual() for _ in range(population_size)]
    
    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
        best_individual = min(population, key=lambda x: evaluate(x)[0])
    
    best_cost, best_tours, tour_costs = evaluate(best_individual)
    return best_tours, tour_costs, best_cost

# Solve the TSP with the genetic algorithm
best_tours, tour_costs, overall_total_cost = genetic_algorithm()

# Display results in the required format
print("Overall Total Travel Cost:", overall_total_cost)
for idx, (tour, cost) in enumerate(zip(best_tours, tour_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")