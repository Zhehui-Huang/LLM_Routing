import numpy as np
import random
from deap import base, creator, tools, algorithms

# Define cities' coordinates and depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

depots = list(range(8))  # Depot cities from 0 to 7

# Problem parameters
num_robots = 8

def calculate_distance(city1_id, city2_id):
    return np.linalg.norm(np.array(coordinates[city1_id]) - np.array(coordinates[city2_id]))

# Setup for genetic algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(8, 16), 8)  # Sample non-depot cities
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Evaluation function
def evaluate(individual):
    # Assign each non-depot city to the nearest depot
    total_cost = 0
    routes = {depot: [depot] for depot in depots}
    for city in individual:
        closest_depot = min(depots, key=lambda d: calculate_distance(city, d))
        routes[closest_depot].append(city)
    
    # Calculate routes cost and append closing route back to depot
    for depot, route in routes.items():
        if len(route) > 1:
            cost = calculate_distance(route[-1], depot)
            for i in range(len(route)-1):
                cost += calculate_distance(route[i], route[i+1])
            route.append(depot)  # close the tour
            total_cost += cost
            
    # Updating routes dictionary to avoid empty depots
    updated_routes = {k: v for k, v in routes.items() if len(v) > 2}
    return (total_cost, updated_routes)

toolbox.register("evaluate", lambda ind: evaluate(ind)[0])

# GA parameters
population_size = 100
crossover_probability = 0.85
mutation_probability = 0.02
generations = 150

# GA execution
pop = toolbox.population(n=population_size)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("min", np.min)
stats.register("avg", np.mean)

algorithms.eaSimple(pop, toolbox, cxpb=crossover_probability, mutpb=mutation_probability, ngen=generations, 
                    stats=stats, halloffame=hof, verbose=True)

# Extract the best individual
best_solution = hof[0]
best_cost, best_routes = evaluate(best_solution)
print(f"Overall Total Travel Cost: {best_cost}")
for dep, route in best_routes.items():
    print(f"Robot starting at depot {dep} Tour: {route}")
    print(f"Robot Total Travel Cost for tour: {calculate_distance(route[0], route[1]) + sum(calculate_distance(route[i], route[i+1]) for i in range(1, len(route)-2))}")