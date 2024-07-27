import numpy as np
import math

# Define cities
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Distance calculation
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = euclidean(attractions_EM['Location_Coordinates'][i],attractions_EM['Location_Coordinates'][j])

# ACO parameters
num_ants = 20
num_iterations = 100
decay = 0.1
alpha = 1  # pheromone importance
beta = 5   # distance priority
initial_pheromone = 1.0 / num_cities

pheromones = np.ones((num_cities, num_cities)) * initial_pheromone
desirability = 1.0 / (distance_matrix + 1e-10)  # avoid division by zero

# Ant Colony Optimization algorithm
def aco_tsp():
    best_cost = float('inf')
    best_solution = []
    for iteration in range(num_iterations):
        all_tours = []
        all_costs = []
        for ant in range(num_by_ants):
            solution, cost = construct_solution(pheromones, desirability)
            if cost < best_cost:
                best_cost = cost
                best_solution = solution
            all_tours.append(solution)
            all_costs.append(cost)
        pheromones *= (1 - decay)  # evaporation
        for solution, cost in zip(all_tours, all_costs):
            for i in range(len(solution) - 1):
                pheromones[solution[i], solution[i+1]] += 1.0 / cost
    return best_solution, best_cost

def construct_solution(pheromones, desirability):
    solution = []
    # Ant decision code to be implemented
    # The following is a simplified placeholder
    solution = list(range(num_cities))
    np.random.shuffle(solution)
    cost = calculate_cost(solution, distance_matrix)
    return solution, cost

def calculate_cost(solution, distance_matrix):
    cost = 0
    for i in range(1, len(solution)):
        cost += distance_matrix[solution[i-1], solution[i]]
    return cost

# Apply the ACO algorithm
best_solution, best_cost = aco_tsp()

# Formatting the solution to the required output
robot_0_tour = [0] + [city for city in best_solution if city != 0 and city != 1] + [0]
robot_1_tour = [1] + [city for city in best_solution if city not in robot_0_tour and city != 1] + [1]
robot_0_cost = calculate_cost(robot_0_tour, distance_matrix)
robot_1_cost = calculate_cost(robot_1_tour, distance_matrix)
overall_cost = robot_0_cost + robot_1_cost

print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}")
print(f"Overall Total Travel Cost: {overall_cost}")