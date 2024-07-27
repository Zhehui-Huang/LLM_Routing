import numpy as np
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coordal2[0])**2 + (coord1[1] - coord2[1])**2)

def initialize_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
            else:
                distance_matrix[i][j] = float('inf')
    return distance_matrix

def initialize_pheromone(matrix_size, initial_pheromone):
    return np.full((matrix_size, matrix_size), initial_pheromone)

def choose_next_city(probabilities):
    return np.random.choice(len(probabilities), p=probabilities)

def calculate_probabilities(current_city, pheromone, heuristic, alpha, beta, taboo_list):
    pheromones = pheromone[current_city]
    heuristics = heuristic[current_city] ** beta
    pheromones = pheromones ** alpha
    probabilities = pheromones * heuristics
    probabilities[taboo_list] = 0
    total = np.sum(probabilities)
    if total == 0:
        probabilities = np.ones(len(probabilities)) / (len(probabilities) - len(taboo_list))
        probabilities[taboo_list] = 0
    else:
        probabilities /= total
    return probabilities

def ant_colony_optimization(cities, num_ants, num_iterations, alpha, beta, evaporation_rate, initial_pheromone, num_robots):
    distance_matrix = initialize_distance_matrix(cities)
    pheromone_matrix = initialize_pheromone(len(cities), initial_pheromone)
    heuristic_matrix = 1 / distance_matrix
    best_cost = float('inf')
    best_solution = None

    for _ in range(num_iterations):
        solutions = []
        costs = []
        for _ in range(num_ants):
            tours = [[] for _ in range(num_robots)]
            starts = [i for i in range(num_robots)]
            next_city = starts[:]
            for tour_idx in range(num_robots):
                tours[tour_idx].append(starts[tour_idx])

            for _ in range(len(cities) - num_robots):
                for robot_id in range(num_robots):
                    current_city = next_city[robot_id]
                    taboo_list = [city for tour in tours for city in tour]
                    probabilities = calculate_probabilities(current_city, pheromone_matrix, heuristic_matrix, alpha, beta, taboo_list)
                    next_city[robot_id] = choose_next_city(probabilities)
                    tours[robot_id].append(next_city[robot_id])

            for tour_idx in range(num_robots):
                tours[tour_idx].append(starts[tour_idx])  # Complete the tour

            cost = 0
            for tour in tours:
                tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
                cost += tour_cost

            if cost < best_cost:
                best_cost = cost
                best_solution = tours

            solutions.append(tours)
            costs.append(cost)

        # Update pheromone levels
        pheromone_matrix *= (1 - evaporation_rate) 
        for i, cost in enumerate(costs):
            for tour in solutions[i]:
                for j in range(len(tour)-1):
                    city_i, city_j = tour[j], tour[j+1]
                    pheromone_matrix[city_i][city_j] += 1 / cost

    return best_solution, costs

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
num_ants = 20
num_iterations = 100
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5
initial_pheromone = 0.1
num_robots = 8

best_solution, costs = ant_colony_optimization(
    cities, num_ants, num_iterations, alpha, beta, evaporation_rate, initial_pheromone, num_robots
)

overall_cost = sum(costs)
for i, tour in enumerate(best_solution):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")