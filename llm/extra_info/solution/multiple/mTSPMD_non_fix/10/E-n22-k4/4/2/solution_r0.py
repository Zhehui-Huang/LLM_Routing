import numpy as np
from scipy.spatial.distance import euclidean
from deap import creator, base, tools, algorithms
import random

# Define the cities coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Number of robots and assignment of starting depots
num_robots = 4
robot_start_depot = {0: 0, 1: 1, 2: 2, 3: 3}

# Define toolbox
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

def create_individual():
    """ Create an individual solution """
    remaining_cities = list(cities.keys())[4:]  # Excluding depots from being shuffled
    random.shuffle(remaining_cities)
    return remaining_cities

def evaluate(individual):
    """ Evaluate the individual total travel cost """
    total_distance = 0
    for i in range(num_robots):
        start_city = robot_start_depot[i]
        # Assign segments of the individual to different robots
        part_length = len(individual) // num_robots
        if i < num_robots - 1:
            segment = individual[i * part_length:(i + 1) * part_length]
        else:
            segment = individual[i * part_length:]  # Remainder for the last robot
        
        current_city = start_city
        for city in segment:
            total_distance += euclidean(cities[current_city], cities[city])
            current_city = city
            
    return (total_distance,)

toolbox.register("individual", tools.initIterate, creator.Individual, create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(42)
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("std", np.std)
    
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 50, stats=stats, halloffame=hof)
    
    best_individual = hof[0]
    best_tours = []
    total_cost = 0

    for i in range(num_robots):
        start_city = robot_start_depot[i]
        part_length = len(best_individual) // num_robots
        if i < num_robots - 1:
            segment = best_individual[i * part_length:(i + 1) * part_length]
        else:
            segment = best_individual[i * part_length:]
        
        tour = [start_city] + segment
        cost = 0
        current_city = start_city
        for city in tour:
            cost += euclidean(cities[current_city], cities[city])
            current_city = city
        best_tours.append((i, [start_city] + segment, cost))
        total_cost += cost
    
    for i, tour, cost in best_tours:
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")
        
    print(f"Overall Total Travel Cost: {total_cost}")

if __name__ == "__main__":
    main()