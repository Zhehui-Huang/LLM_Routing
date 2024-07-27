from deap import base, creator, tools, algorithms
import random
import numpy as np
import math

# Define the cities' coordinates
cities = {
    0: (30, 40),  1: (37, 52),  2: (49, 49),  3: (52, 64),  4: (31, 62),  5: (52, 33),  6: (42, 41),
    7: (52, 41),  8: (57, 58),  9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}

# Number of Robots
num_robots = 8

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# GA setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Individual generator
def create_individual():
    individual = list(range(1, len(cities)))  # include all cities except the depot
    random.shuffle(individual)
    return individual

toolbox.register("individual", tools.initIterate, creator.Individual, create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

def evaluate(individual):
    # Divide the route among robots
    sections = np.array_split(individual, num_istances)
    total_distance = 0
    for section in sections:
        tour = [0] + list(section) + [0]
        for i in range(len(tour) - 1):
            total_distance += distance(tour[i], tour[i+1])
    return (total_distance,)
toolbox.register("evaluate", evaluate)

# Genetic Algorithm
def solve_mTSP():
    population = toolbox.population(n=300)
    hof = tools.HallOfFame(1)

    _, log = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=300, 
                                stats=None, halloffame=hof, verbose=False)
    
    best_individual = hof.items[0]
    best_fitness = best_individual.fitness.values

    best_chunks = [best_individual[i::num_robots] for i in range(num_robots)]
    total_cost = 0
    robot_tour_details = []
    
    for i, chunk in enumerate(best_chunks):
        tour = [0] + list(chunk) + [0]
        tour_distance = sum(distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
        total_cost += tour_distance
        robot_tour_details.append((i, tour, tour_distance))
    
    return robot_tour_details, total_cost

# Execution and result display
robot_tours, overall_cost = solve_mTSP()
for robot, tour, cost in robot_tours:
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")
print(f"Overall Total Travel Leader: {3}")