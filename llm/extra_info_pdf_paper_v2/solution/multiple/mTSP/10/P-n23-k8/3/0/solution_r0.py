from deap import base, creator, tools, algorithms
import random
import numpy as np
import math

# Define the cities' coordinates
cities = {
    0: (30, 40),  1: (37, 52),  2: (49, 49),  3: (52, 64),  4: (31, 62),  5: (52, 33),  6: (42, 41),
    7: (52, 41),  8: (57, 58),  9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}

# Number of Robots
num_robots = 8

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create fitness function and individual classes
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.Fitness
# GA operators
def create_individual():
    individual = list(range(1, len(cities)))  # include all cities except the depot
    random.shuffle(individual)
    return individual

def crossover(ind1, ind2):
    return tools.cxPartialyMatched(ind1, ind2)

def mutate(individual):
    tools.mutShuffleIndexes(individual, indpb=0.05)

def evaluate(individual):
    # Divide cities between robots
    chunks = [individual[i::num_robots] for i in range(num_robots)]
    total_distance = 0
    for chunk in chunks:
        # Add depot at the start and the end of the tour for each robot
        tour = [0] + chunk + [0]
        # Calculate total distance for each robot
        for i in range(len(tour) - 1):
            total_distance += distance(tour[i], tour[i + 1])
    return (total_distance,)

# Create Toolbox
toolbox = base.Toolbox()
toolbox.register("individual", tools.initIterate, creator.Individual, create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate)
toolbox.register("mate", crossover)
toolbox.register("mutate", mutate)
toolbox.register("select", tools.selTournament, tournsize=3)

# Solve mTSP using genetic algorithm
def solve_mTSP():
    random.seed(42)
    population = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    
    algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=400, halloffame=hof, verbose=False)
    
    best_individual = hof[0]
    best_fitness = best_individual.fitness.values

    # Prepare the result output
    best_chunks = [best_individual[i::num_robots] for i in range(num_robots)]
    total_cost = 0
    robot_tour_details = []

    for i, chunk in enumerate(best_chunks):
        tour = [0] + chunk + [0]
        tour_distance = sum(distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
        total_cost += tour_distance
        robot_tour_details.append((i, tour, tour_distance))

    return robot_tour_details, total_cost

# Run the solver and print the routes and costs
results, total_cost = solve_mTSP()

for robot, tour, cost in results:
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")