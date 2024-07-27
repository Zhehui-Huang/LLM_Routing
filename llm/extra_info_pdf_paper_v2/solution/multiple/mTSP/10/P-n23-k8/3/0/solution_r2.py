import math
import random
from deap import base, creator, tools, algorithms

# Coordinates of cities (including the depot city)
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

num_robots = 8

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Fitness and Individual
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Tools setup
toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, len(cities)), len(cities) - 1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluate function
def evaluate(individual):
    chunk_size = len(individual) // num_robots
    total_cost = 0
    for i in range(num_robots):
        start_index = i * chunk_size
        end_index = None if i == num_robots - 1 else start_index + chunk_size
        robot_cities = [0] + individual[start_index:end_online] + [0]
        for j in range(len(robot_cities) - 1):
            total_cost += distance(cities[robot_cities[j]], cities[robot_cities[j + 1]])
    return (total_cost,)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.02)
toolbox.register("select", tools.selTournament, tournsize=3)

# Genetic algorithm
def solve_mTSP():
    random.seed(64)
    population = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    
    _, logbook = algorithms.eaSimple(population, toolbox, 0.7, 0.2, 100, stats=stats, halloffame=hof, verbose=False)
    
    best_solution = hof[0]
    best_cost = evaluate(best_solution)[0]
    tours = []
    chunk_size = len(best_solution) // num_robots
    for i in range(num_robots):
        start_index = i * chunk_size
        end_index = None if i == num_robots - 1 else start_index + chunk_size
        tour = [0] + best_solution[start_index:end_index] + [0]
        tour_cost = sum(distance(cities[tour[j]], cities[tour[j + 1]]) for j in range(len(tour) - 1))
        tours.append((tour, tour_cost))
    
    return tours, best_cost

# Running the solver
tours, total_cost = solve_mTSP()

# Output the results
for idx, (tour, cost) in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_cost}")