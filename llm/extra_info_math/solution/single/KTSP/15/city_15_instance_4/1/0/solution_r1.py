import math
import random
from deap import base, creator, tools, algorithms

# Define the coordinates of each city including the depot
coordinates = [
    (35, 40),  # Depot
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Genetic Algorithm setups
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, 15), 11)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    # Start and end at the depot
    path = [0] + individual + [0]
    path_cost = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))
    return (path_cost,)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

def solve_tsp():
    random.seed(64)  # Seed for reproducibility
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)

    # Statistics to monitor evolution
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", lambda x: x[0])
    stats.register("min", lambda x: x[0])

    # Run the genetic algorithm
    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=150, stats=stats, halloffame=hof, verbose=True)

    best_individual = hof[0]
    best_tour = [0] + best_individual + [0]
    best_cost = evalTSP(best_individual)[0]
    return best_tour, best_cost

# Solve the TSP
tour, cost = solve_tsp()
print("Tour:", tour)  # Output the tour
print("Total travel cost:", cost)  # Output the travel cost