import math
import random
from deap import base, creator, tools, algorithms

# Define cities coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Fitness function
def evaluate(individual):
    max_dist = 0
    total_cost = 0
    path = individual + [individual[0]]
    for i in range(len(cities)):
        dist = calc_distance(path[i], path[i+1])
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    return max_dist, total_cost

# Genetic Algorithm settings
creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, len(cities)), len(cities) - 1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selNSGA2)
toolbox.register("evaluate", evaluate)

def main():
    random.seed(42)
    pop = toolbox.population(n=300)
    hof = tools.ParetoFront()
    
    # Stats
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", min)
    stats.register("size", len)
    
    algorithms.eaMuPlusLambda(pop, toolbox, mu=300, lambda_=300, cxpb=0.7, mutpb=0.2, ngen=100, stats=stats, halloffame=hof, verbose=True)
    
    best_individual = sorted(hof, key=lambda x: x.fitness.values)[0]
    best_tour = [0] + list(best_individual) + [0]
    max_distance, total_cost = evaluate(best_individual)
    return best_tour, total_cost, max_distance

# Execute the genetic algorithm
best_tour, total_cost, max_distance = main()

print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))