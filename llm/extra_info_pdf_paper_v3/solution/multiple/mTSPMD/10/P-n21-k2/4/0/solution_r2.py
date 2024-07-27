import random
import numpy as np

# Coordinates for each city, including depots
coordinates = [
    (30, 40), # Depot 0
    (37, 52), # Depot 1
    (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Compute Euclidean distance between two cities
def dist(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Evaluate fitness of a solution as the sum of travel distances
def fitness(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = sum(dist(tour[i], tour[i+1]) for i in range(len(tour)-1))
        total_cost += tour_cost
    return total_cost

# Generate a random initial individual
def create_individual():
    cities = list(range(2, 21))  # All city indices except the depots
    random.shuffle(cities)
    split_point = random.randint(1, len(cities) - 1)
    return [cities[:split_point], cities[split_point:]]

# Mutation operator
def mutate(individual):
    city1, city2 = random.sample(range(len(individual)), 2)
    individual[city1], individual[city2] = individual[city2], individual[city1]

# Crossover operator
def crossover(parent1, parent2):
    cut_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:cut_point] + parent2[cut_point:]
    child2 = parent2[:cut_point] + parent1[cut_point:]
    return [child1, child2]

# Genetic algorithm to minimize travel cost
def genetic_algorithm(population_size=100, generations=500):
    population = [create_individual() for _ in range(population_size)]
    best_score = float('inf')
    best_solution = None

    for _ in range(generations):
        # Evaluate current population
        scores = [fitness([[0] + ind[0] + [0], [1] + ind[1] + [1]]) for ind in population]
        for i, score in enumerate(scores):
            if score < best_score:
                best_score = score
                best_solution = population[i]

        # Crossover and mutation
        next_population = []
        for i in range(0, population_size, 2):
            p1, p2 = population[i], population[i+1]
            for child in crossover(p1, p2):
                mutate(child)
                next_population.append(child)
        population = next_population

    return best_solution, best_score

# Run genetic algorithm
best_solution, best_score = genetic_algorithm()

# Construct tour paths
robot0_tour = [0] + best_solution[0] + [0]
robot1_tour = [1] + best_solution[1] + [1]

# Calculate tour costs
robot0_cost = sum(dist(robot0_tour[i], robot0_tour[i+1]) for i in range(len(robot0_tour)-1))
robot1_cost = sum(dist(robot1_tour[i], robot1_tour[i+1]) for i in range(len(robot1_tour)-1))

# Output the results
print("Robot 0 Tour:", robot0_tour)
print("Robot 0 Total Travel Cost:", round(robot0_cost, 2))
print("Robot 1 Tour:", robot1_tour)
print("Robot 1 Total Travel Cost:", round(robot1_cost, 2))
print("Overall Total Travel Cost:", round(robot0_cost + robot1_cost, 2))