import numpy as np
import random
from math import sqrt
from deap import creator, base, tools, algorithms

# Coordinates for each city including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

depots = [0, 1, 2, 3]  # Indices of depots
non_depots = list(set(range(len(coordinates))) - set(depots))

# Calculate the euclidean distance between two points
def euclidean(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the total distance of the tour
def tour_distance(tour, coordinates):
    return sum(euclidean(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

# GA functions
def create_individual():
    tour = non_depots[:]
    random.shuffle(tour)
    return tour

def evaluate(individual):
    complete_tour = individual[:]
    total_distance = 0
    for depot in depots:
        depot_index = depots.index(depot)
        start_index = depot_index * (len(individual) // len(depots))
        end_index = (depot_index + 1) * (len(individual) // len(depots)) if depot_index < len(depots) - 1 else len(individual)
        tour_segment = [depot] + individual[start_index:end_index] + [depot]
        total_distance += tour_distance(tour_segment, coordinates)
    return (total_distance,)

def cxTwoPointCopy(ind1, ind2):
    size = min(len(ind1), len(ind2))
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    ind1[cxpoint1:cxpoint2], ind2[cxpoint1:cxpoint2] = ind2[cxpoint1:cxpoint2].copy(), ind1[cxpoint1:cxpoint2].copy()
    return ind1, ind2

# Setting up the GA
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("individual", tools.initIterate, creator.Individual, create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.02)
toolbox.register("select", tools.selTournament, tournsize=3)

# Run the genetic algorithm
population = toolbox.population(n=50)
hall_of_fame = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("min", np.min)
stats.register("std", np.std)

algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, stats=stats, halloffame=hall_of_fame, verbose=True)

# Displaying the final solutions
best_individual = hall_of_fame.items[0]
fitness = evaluate(best_individual)
print('Best Tour by each Robot:')
for depot in depots:
    depot_index = depots.index(depot)
    start_index = depot_index * (len(best_individual) // len(depots))
    end_index = (depot_index + 1) * (len(best_individual) // len(depots)) if depot_index < len(depots) - 1 else len(best_individual)
    tour_segment = [depot] + best_individual[start_index:end_index] + [depot]
    print(f"Robot {depot_index} (Depot {depot}):", tour_segment, "Cost:", tour_distance(tour_segment, coordinates))
print('Total cost of best solution:', fitness[0])