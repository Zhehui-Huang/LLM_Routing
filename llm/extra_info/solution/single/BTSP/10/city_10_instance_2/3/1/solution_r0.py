import math
import random

# City coordinates
coordinates = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), 
               (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)

# Create a distance matrix
dist_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Function to calculate total travel cost and max leg distance
def tour_cost(tour):
    total_cost = 0
    max_leg_distance = 0
    for i in range(len(tour)-1):
        leg_dist = dist_matrix[tour[i]][tour[i+1]]
        total_cost += leg_dist
        if leg_dist > max_leg_distance:
            max_leg_distance = leg_dist
    return total_cost, max_leg_distance

# Genetic algorithm parameters
population_size = 100
generations = 500
mutation_rate = 0.1

# Initialize population
population = [[0] + random.sample(range(1, len(coordinates)), len(coordinates)-1) + [0] for _ in range(population_size)]

# Fitness function
def fitness(tour):
    _, max_leg_distance = tour_cost(tour)
    return -max_leg_distance  # Negative, since we aim to minimize

# Selection function
def select(population, fitnesses):
    sorted_population = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_population[:population_size//2]]

# Crossover function
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1)-1), 2))
    child = [None]*len(parent1)
    child[start:end] = parent1[start:end]
    pointer = 0
    for city in parent2:
        if city not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = city
    child[0], child[-1] = 0, 0
    return child

# Mutation function
def mutate(tour):
    if random.random() < mutation_rate:
        i, j = sorted(random.sample(range(1, len(tour)-1), 2))
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Genetic Algorithm:
for generation in range(generations):
    fitnesses = [fitness(tour) for tour in population]
    population = select(population, fitnesses)
    new_population = []
    for _ in range(population_size // 2):
        parent1, parent2 = random.sample(population, 2)
        child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
        new_population.append(mutate(child1))
        new_population.append(mutate(child2))
    population = new_population

# Get the best result
best_tour = sorted(population, key=lambda x: fitness(x), reverse=True)[0]
total_cost, max_distance = tour_cost(best_tour)

print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)