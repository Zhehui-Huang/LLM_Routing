import math
import random
from deap import base, creator, tools, algorithms

# Define the coordinates of each city including the depot
coordinates = [
    (35, 40), # Depot
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

# Euclidean distance calculation
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Genetic Algorithm setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, 15), 11)  # create a sample of 11 cities (other than depot)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    # Append the depot city (0) to the start and end of the tour
    tour = [0] + individual + [0]
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1)),

toolbox.register("mate", tools.cxOrdered)  # Ordered crossover
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)  # Shuffle mutation
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

def solve_tsp():
    random.seed(64)  # for reproducibility
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", lambda x: x[0])
    stats.register("min", lambda x: x[0])
    
    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=150, stats=stats, halloffame=hof, verbose=True)
    
    best_tour = [0] + hof[0] + [0]
    best_cost = evalTSP(hof[0])[0]
    return best_tour, best_cost

# Solve the TSP
tour, cost = solve_tsp()
print("Tour:", tour)
print("Total travel cost:", cost)