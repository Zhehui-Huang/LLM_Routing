import numpy as np
import random
from deap import base, creator, tools, algorithms

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Define how many robots are there and their respective depots
num_robots = 8
robot_depots = list(range(num_robots))  # Initial cities as depots

# Distance calculation function
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Genetic Algorithm Framework Setup using DEAP
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Chromosome creation (randomized with depots in order)
def create_individual():
    cities_perm = list(range(8, 23))  # Only the non-depot cities
    random.shuffle(cities_perm)
    partition_sizes = [len(cities_perm) // num_robots] * num_robots
    for i in range(len(cities_perm) % num_robots):
        partition_sizes[i] += 1
    individuals = []
    index = 0
    for size in partition_sizes:
        individual = [robot_depots[index]] + cities_perm[index:index + size] + [robot_depots[index]]
        individuals.append(individual)
        index += size
    return individuals

# Evaluate function computes the total cost of tours for all robots
def evaluate(individual):
    total_cost = 0
    for robot_tour in individual:
        tour_cost = sum(euclidean_distance(cities[robot_tour[i]], cities[robot_tour[i + 1]]) for i in range(len(robot_tour) - 1))
        total_cost += tour_cost
    return total_cost,

toolbox.register("individual", tools.initIterate, creator.Individual, create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual, n=500)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.02)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

# Genetic Algorithm Parameters
population_size = 100
num_generations = 150

def main():
    random.seed(42)
    population = toolbox.population()
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    
    algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=num_generations, stats=stats, halloffame=hof, verbose=True)
    
    # Outputting the best solution
    best_solution = hof.items[0]
    overall_cost = evaluate(best_solution)[0]
    for i, tour in enumerate(best_solution):
        print(f"Robot {i} Tour: {tour}")
        tour_cost = sum(euclideancation
    print(f"Overall Total Travel Cost: {overall_cost}")

if __name__ == "__main__":
    main()