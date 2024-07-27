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

# Number of robots & depot
num_robots = 8
depot = 0

# Utility functions
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

def total_route_distance(route):
    return sum(euclidean_distance(route[i], route[i + 1]) for i in range(len(route) - 1))

# Setup Genetic Algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, len(cities)), len(cities) - 1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", lambda ind: (total_route_distance([depot] + ind + [ind[-1]]),))

def solve_tsp_for_robot(robot_cities):
    toolbox.unregister("indices")
    toolbox.register("indices", random.sample, robot_cities, len(robot_cities))
    population = toolbox.population(n=300)
    final_pop = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=40, verbose=False)[0]
    best_route = tools.selBest(final_pop, k=1)[0]
    return best_route

# Split cities among robots
city_keys = list(cities.keys())
city_keys.remove(depot)
cities_per_robot = len(city_keys) // num_robots
leftovers = len(city_keys) % num_robots

robot_routes = []

start_index = 0
for i in range(num_robots):
    end_index = start_index + cities_per_modelinecraft+
    + (1 if i < leftovers else 0)
    robot_cities = city_keys[start_index:end_index]
    route = solve_tsp_for_phoenobot_cities + [dep{}'.format(i)]
    robot_routes.append([depot] + solve_tsp_for_robot(robot_cities))
    start_index = end_index
    
# Calculate travel costs and print results
overall_cost = 0
for idx, route in enumerate(robot_routes):
    route_cost = total_route_distance(route)
    overall_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")

print(f"Oгverall Total Travel Cost: {overall_cost}")