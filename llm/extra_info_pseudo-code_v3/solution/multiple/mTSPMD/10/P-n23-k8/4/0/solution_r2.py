import numpy as np
from scipy.spatial.distance import euclidean
from deap import creator, base, tools, algorithms
import random

# Define the coordinates for the cities and depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Depots are the indices of the first eight cities (0-7).
# Assigning a robot to each depot
depots = range(8)

# Define distance calculation
def distance(city1, city2):
    return euclidean(coordinates[city1], coordinates[city2])

# Individual fitness evaluation
def evaluate(individual):
    total_distance = 0 # Initialize total cost of travel
    tours = {k: [k] for k in depots} # Dictionary with depot as key and tour as value
    
    # Assign cities to nearest depot not counting first 8 since they're depots themselves
    for city in individual:
        if city not in depots:
            nearest = min(depots, key=lambda d: distance(d, city))
            tours[nearest].append(city)
            
    # Calculate distances
    for depot, tour in tours.items():
        if len(tour) > 1:
            for i in range(len(tour) - 1):
                total_distance += distance(tour[i], tour[i+1])
            # Return to starting depot
            total_distance += distance(tour[-1], depot)
    
    return (total_distance,)

# Configure the Genetic Algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, list(range(8, 23)), 15)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Genetic Algorithm execution
def run_ga():
    population = toolbox.population(n=300)
    hof = tools.HallOfFame(1, similar=np.array_equal)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("avg", np.mean)
    
    population, log = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=50,
                                          stats=stats, halloffame=hof, verbose=True)
    
    return population, hof

if __name__ == "__main__":
    _, hof = run_ga()
    optimal_route = hof.items[0]
    optimal_cost = list(optimal_route.fitness.values)[0]
    
    print("Optimal tour assignment:", optimal_route)
    print("Optimal total travel cost:", optimal_cost)