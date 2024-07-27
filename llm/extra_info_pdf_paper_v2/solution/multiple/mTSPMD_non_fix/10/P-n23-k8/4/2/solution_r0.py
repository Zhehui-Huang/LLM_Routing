import math
import random
from deap import creator, base, tools, algorithms

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8
# Starting depot for all robots is city 0
depot = 0

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# GA setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, len(cities)), len(cities) - 1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", lambda ind: (sum(euclidean_distance(ind[i - 1], ind[i]) for i in range(1, len(ind))) + euclidean_distance(designated_depot, ind[0]) + euclidean_distance(ind[-1], ending_depot),))

population = toolbox.population(n=300)
algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=150, verbose=False)

# Select the best individual
best_tour = tools.selBest(population, k=1)[0]

# Calculate the total distance cost
tour_with_depot = [depot] + best_tour + [depot]
total_cost = sum(euclidean_distance(tour_with_depot[i], tour_with_depot[i+1]) for i in range(len(tour_with_depot)-1))

print("Best Tour:", tour_with_depot)
print("Total Travel Cost:", total_cost)