import numpy as np
from scipy.spatial import distance_matrix
from geneticalgorithm import geneticalgorithm as ga

# Define cities and their coordinates
cities = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
])

# Calculate distance matrix
distances = distance_matrix(cities, cities)

# Fitness function for genetic algorithm
def fitness(solution):
    cost = 0
    for i in range(len(solution)-1):
        cost += distances[int(solution[i]), int(solution[i+1])]
    return cost

def decode_chromosome(chromosome):
    # Decode chromosome into a list of city indices
    stops = list(np.argsort(np.array(chromosome)))  # Visit cities based on sorted indices of genes
    routes = [[0], [1]]  # Starting routes at depots
    for stop in stops:
        # Assign stop to the shortest current route to balance the load
        if stop > 1:
            if fitness(routes[0] + [stop]) < fitness(routes[1] + [stop]):
                routes[0].append(stop)
            else:
                routes[1].append(stop)
    return routes

# Define genetic algorithm parameters
varbound = np.array([[0,1]]*len(cities))  # Bounds as cities are represented from 0 to 1 for simplicity
algorithm_param = {
    "max_num_iteration": 1000,
    "population_size": 100,
    "mutation_probability": 0.1,
    "elit_ratio": 0.01,
    "crossover_probability": 0.5,
    "parents_portion": 0.3,
    "crossover_type": "uniform",
    "max_iteration_without_improv": None
}

model = ga(function=fitness, dimension=len(cities), variable_type='real', variable_boundaries=varbound, algorithm_parameters=algorithm_param)
model.run()

solution = model.output_dict['variable']
routes = decode_chromosome(solution)

# Calculate tour cost
def calculate_tour_cost(tour):
    return sum(distances[tour[i], tour[(i+1) % len(tour)]] for i in range(len(tour)))

# Output results
robot_tour_costs = []
total_cost = 0
output = ""
for i, tour in enumerate(routes):
    cost = calculate_tour_cost(tour)
    robot_tour_costs.append(cost)
    total_cost += cost
    output += f"Robot {i} Tour: {tour}\n"
    output += f"Robot {i} Total Travel Cost: {cost}\n"

output += f"Overall Total Travel Cost: {total_cost}\n"
print(output)