import numpy as np
from scipy.spatial import distance_matrix
import random
from deap import base, creator, tools, algorithms

# Coordinates of cities including depots
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35)]

# Distance matrix calculation
dist_matrix = distance_matrix(coordinates, coordinates)

# Prepare the genetic algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
# Attribute generator: shuffle indices from 2 to len(coordinates) (excluding depots)
toolbox.register("indices", random.sample, range(2, len(coordinates)), len(coordinates)-2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Genetic operators
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def evaluate(individual):
    # Assign first robot to start at depot 0, second robot at depot 1
    # Each individual presents a permutation of cities excluding depots, processed in tour order
    tours = [[0], [1]]  # start at respective depots
    cities_per_robot = len(individual) // 2
    # distribute cities to two robots
    for i, city in enumerate(individual):
        tours[i // cities_per_robot].append(city)
    # Complete the tour at respective depots
    tours[0].append(0)
    tours[1].append(1)
    
    # Calculate total distance cost
    total_cost = 0
    for tour in tours:
        for i in range(len(tour) - 1):
            total_cost += dist_matrix[tour[i]][tour[i+1]]
            
    return (total_cost,)

toolbox.register("evaluate", evaluate)

# Population size
population = toolbox.population(n=50)

# Hall of Fame to keep the best individual
hof = tools.HallOfFame(1)

# Statistics to observe evolution
stats = tools.Statistics(key=lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("std", np.std)
stats.register("min", np.min)
stats.register("max", np.max)

# Evolve the population
result = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=40,
                             stats=stats, halloffame=hof, verbose=True)

# Best individual evaluation
best_individual = hof.items[0]
best_cost = best_individual.fitness.values[0]
tours = [[0], [1]]  # init tours to depots
cities_per_robot = len(best_individual) // 2

for i, city in enumerate(best_individual):
    tours[i // cities_per_robot].append(city)

tours[0].append(0)
tours[1].append(1)

# Display results
print("\nBest Individual Tours:")
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    cost = sum(dist_matrix[tour[j]][tour[j+1]] for j in range(len(tour)-1))
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print("Overall Best Cost:", best_cost)