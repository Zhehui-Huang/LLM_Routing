import numpy as np
from scipy.spatial.distance import euclidean
from deap import creator, base, tools, algorithms
import random

# Input
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_robots = len(depots)
num_cities = len(coordinates)

# Initialize fitness and individual containers for the genetic algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(num_cities), num_cities)

def create_individual():
    individual = list(range(num_cities))
    random.shuffle(individual)
    return [individual[i] if i not in depots else i for i in individual]

toolbox.register("individual", tools.initIterate, creator.Individual, create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Distance matrix computation
def distance_matrix(coordinates):
    size = len(coordinates)
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i][j] = euclidean(coordinates[i], coordinates[j])
    return matrix

dist_matrix = distance_matrix(coordinates)

# Evaluation function
def eval_tsp(individual):
    cost = 0
    for i in range(1, len(individual)):
        cost += dist_matrix[individual[i-1], individual[i]]
    # Closing depot loop
    cost += dist_matrix[individual[-1], individual[0]]
    return cost,

toolbox.register("evaluate", eval_tsp)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Running the Genetic Algorithm
def main():
    random.seed(64)
    population = toolbox.population(n=300)
    
    hof = tools.HallOfFame(1)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    
    algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=500, stats=stats, halloffame=hof, verbose=True)
    
    best_route = hof[0]
    best_cost = eval_tsp(best_route)[0]
    
    # Format and output tours for each robot
    robot_tours = {depot: [] for depot in depots}
    current_depot = best_route[0]
    tour_part = []

    for city in best_route:
        tour_part.append(city)
        if city in depots:
            robot_tours[current_depot] = tour_part[:]
            tour_part = [city]
            current_depot = city

    total_travel_cost = 0
    for robot_id, tour in robot_tours.items():
        tour.append(tour[0])  # ensure returning to the starting depot
        tour_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
        total_travel_cost += tour_cost
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")
    
    print(f"Overall Total Travel Cost: {total_travel_index:.2f}")
    
if __name__ == "__main__":
    main()