import numpy as np
from scipy.spatial import distance_matrix
from geneticalgorithm import geneticalgorithm as ga

# Cities and coordinates
cities = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
])

# Distance matrix
distances = distance_matrix(cities, cities)

def fitness(solution):
    """ Calculates the total distance of the routes described by the solution """
    cost = 0
    routes = decode_solution(solution)
    for route in routes:
        for i in range(len(route) - 1):
            cost += distances[int(route[i]), int(route[i + 1])]
    return cost

def decode_solution(solution):
    """ Decodes a solution to the routes for two robots based on a sorted chromosome """
    solution = [int(x) for x in solution]
    robot0_route = [0]
    robot1_route = [1]
    
    # Determine city assignment by sorted order in the chromosome
    sorted_cities = sorted(range(2, len(cities)), key=lambda x: solution[x])
    
    # Alternate assignment of cities to robots
    for i, city in enumerate(sorted_cities):
        if i % 2 == 0:
            robot0_route.append(city)
        else:
            robot1_route.append(city)
    
    robot0_route.append(robot0_route[0])  # end where they started for validation (will remove later if needed)
    robot1_route.append(robot1_route[0])
    return [robot0_route, robot1_route]

varbound = np.array([[0, 1]] * (len(cities)))

algorithm_param = {
   'max_num_iteration': 1000,
   'population_size': 100,
   'mutation_probability': 0.1,
   'elit_ratio': 0.01,
   'crossover_probability': 0.7,
   'parents_portion': 0.3,
   'crossover_type':'uniform',
   'max_iteration_without_improv': None
}

model = ga(function=fitness, dimension=len(cities), variable_type='real', variable_boundaries=varbound, algorithm_parameters=algorithm_param)
model.run()

best_solution = model.output_dict['variable']
best_routes = decode_solution(best_solution)

# Calculate and print the costs
total_cost = 0
output = ""
for i, route in enumerate(best_routes):
    route_cost = sum(distances[route[j], route[j+1]] for j in range(len(route)-1))
    total_cost += route_cost
    output += f"Robot {i} Tour: {route[:-1]}\n"  # Remove the last to not return to the starting point
    output += f"Robot {i} Total Travel Cost: {route_cost}\n"

output += f"Overall Total Travel Cost: {total_data_cost}\n"
print(output)