import math
import random
from deap import base, creator, tools, algorithms

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Utility function to calculate the Euclidean distance between two cities
def euclidean_dist(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Genetic Algorithm problem setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,-1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("city_indices", random.sample, range(1, len(cities)), len(cities)-1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.city_indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.02)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", lambda ind: evaluate(ind))

def evaluate(individual):
    # Ensure the individual starts and ends at the depot
    route = [0] + individual + [0]
    max_dist = -1
    total_cost = 0

    for i in range(len(route) - 1):
        dist = euclidean_dist(route[i], route[i + 1])
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    return max_dist, total_cost

def main():
    toolbox.population(n=50)
    pop = toolbox.population(n=300)

    hof = tools.HallOfFame(1, similar=lambda x,y: x == y)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", lambda fit: sum((c[0] for c in fit))/len(fit))
    stats.register("std", lambda fit: math.sqrt(sum((c[0]-stats.avg(fit))**2 for c in fit)/len(fit)))
    stats.register("min", lambda fit: min(c[0] for c in fit))

    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 100, stats=stats, halloffame=hof, verbose=True)

    best = hof[0]
    return best

# Run the genetic algorithm and retrieve the best tour found
best_solution = main()
best_individual = [0] + best_solution + [0]
fitness_results = evaluate(best_solution)

# Output results
print(f"Tour: {best_individual}")
print(f"Maximum distance between consecutive cities: {fitness_heading[0]}")
print(f"Total travel cost: {fitness_heading[1]}")