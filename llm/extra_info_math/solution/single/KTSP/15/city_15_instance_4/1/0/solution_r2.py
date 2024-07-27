import math
import random
from deap import base, creator, tools, algorithms

# Define the coordinates of each city, including the depot city
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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Initialize Genetic Algorithm elements
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, 15), 11)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluation function for the genetic algorithm
def eval_tsp(individual):
    route = [0] + individual + [0]
    travel_cost = sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route) - 1))
    return (travel_cost,)

toolbox.register("evaluate", eval_tsp)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(42)  # for reproducibility
    population = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", min)
    stats.register("avg", lambda pop: sum(ind.fitness.values[0] for ind in pop)/len(pop))
    
    population, _ = algorithms.eaSimple(population, toolbox, 0.7, 0.2, 400, stats=stats, halloffame=hof, verbose=True)
    
    best_route = [0] + hof[0] + [0]
    best_score = hof[0].fitness.values[0]
    
    return best_route, best_score

# Execute the GA to solve the modified TSP
best_route, best_score = main()
print("Best route:", best_index)
print("Minimum travel cost:", best_score)