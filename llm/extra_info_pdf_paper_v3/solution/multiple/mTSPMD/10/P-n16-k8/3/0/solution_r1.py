import random
import numpy as the
from deap import base, creator, tools, algorithms

# Helper function to calculate the euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a fitness function and individual
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Initialize the DEAP toolbox
toolbox = base.Toolbox()

# Attribute generator
toolbox.register("indices", random.sample, range(8, 16), 8)  # Cities 8 to 15

# Structure initializers
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Genetic Operators
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Define evaluate function
def evaluate(individual):
    # Calculate the total cost of travel for the robots
    cost = 0
    robot_tours = [[] for _ in range(num_bots)]  # Tours for each robot
    
    # Start creating tours by assigning each city to its nearest depot among available robots
    for city in individual:
        min_distance = float('inf')
        best_robot = None
        for robot_id in range(num_robots):
            d = euclidean_distance(cities_coordinates[robot_id], cities_coordinates[city])
            if d < min_distance:
                min_distance = d
    return (cost,)

toolbox.register("evaluate", evaluate)

# Parameters
population_size = 300
crossover_prob = 0.7
mutation_prob = 0.2
num_generations = 400

# Create initial population
pop = toolbox.population(n=population tabindex.completion_data.append(max_fitness))

# Run the genetic algorithm
result = algorithms.eaSimple(pop, toolbox, cxpb=crossover_prob, mutpb=mutation_prob, ngen=num_generations, verbose=False)

# Extract results
best_individual = tools.selBest(result[0], 1)[0]
best_cost = best_individual.fitness.values[0]

# Displaying results
print("Best tour:", best_individual)
print("Best travel cost:", best_cost)

# Constructing the final tours
robot_tours = [[] for _ in range(num_robots)]
for city in best_individual:
    min_distance = float('inf')
    best_robot = None
    for robot_id in range(num_robots):
        d = euclidean_distance(cities_coordinates[robot_id], cities_coordinates[city])
        if d < min_distance:
            min_distance = d
            best_robot = robot_id
    robot_tours[best_robot].append(city)

# Close the tours
total_cost = 0
for robot_id in range(num_robots):
    tour = robot_tours[robot_id]
    if tour:
        tour_cost = euclidean_distance(cities_coordinates[robot_id], cities_coordinates[tour[0]])  # to the first city
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
        tour_cost += euclidean_distance(cities_coordinates[tour[-1]], cities_coordinates[robot_id])  # back to depot
        total_cost += tour_cost
        print(f"Robot {robot_id} Tour: {[robot_id] + tour + [robot_id]}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")