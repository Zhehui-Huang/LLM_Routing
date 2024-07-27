import numpy as np
from deap import creator, base, tools, algorithms
import random
from math import sqrt

# Coordinates for all cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Define depot indices
depots = [0, 1, 2, 3]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Fitness evaluation (total distance of a possible solution)
def evaluate(individual):
    distance = 0
    for i in range(len(individual)-1):
        distance += euclidean_distance(individual[i], individual[i+1])
    return distance,

# Creator for fitness minimization
creator.create("FitnessMin", base.Floss of candidate solution.features, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Individual generator and genetic operators
def create_individual():
    base_tour = list(range(4, len(coordinates)))  # Exclude depots
    random.shuffle(base_tour)
    # Insert each depot to start each robots' tour
    return depots + base_tour

toolbox.register("individual", tools.initIterate, creator.Individual, create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxPartiallyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

# Genetic Algorithm parameters
population_size = 100
crossover_prob = 0.7
mutation_prob = 0.2
num_generations = 250

# Initialize population
population = toolbox.population(n=population_size)

# Apply genetic algorithm
hof = tools.HallOfFame(1)  # Store best individual
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("min", np.min)
stats.register("std", np.std)

algorithms.eaSimple(population, toolbox, cxpb=crossover_prob, mutpb=mutation_prob, ngen=num_generations, 
                    stats=stats, halloffame=hof, verbose=True)

# Extract the best individual
best = hof[0]
best_distance = evaluate(best)[0]

# Displaying results
def display_results(individual):
    robot_tour = {depot: [depot] for depot in depots}
    current_robot = 0

    # Assign cities to depots
    for city in individual[len(depots):]:
        robot_tour[depots[current_robot]].append(city)
        if len(robot_tour[depots[current_robot]]) - 1 == (len(coordinates) - 4) // 4:
            robot_tour[depots[current_robot]].append(depots[current_robot])
            current_robot += 1

    # Ensure last depot closes its tour
    if len(robot_tour[depots[current_robot]]) > 1:
        robot_tour[depots[current_robot]].append(depots[current_robot])

    total_cost = 0
    for k, v in robot_tour.items():
        tour_cost = evaluate(v)[0]
        total_cost += tour_cost
        print(f"Robot {depots.index(k)} Tour: {v}")
        print(f"Robot {depots.index(k)} Total Travel Cost: {tour_cost}")
    print(f"Overall Total Travel Cost: {total_cost}")

display_results(best)