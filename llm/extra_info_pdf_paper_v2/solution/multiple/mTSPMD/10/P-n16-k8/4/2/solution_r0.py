import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def initialize_pheromone_matrix(n, initial_pheromone):
    return [[initial_pheromone for _ in range(n)] for _ in range(n)]

def calculate_visibility(cities):
    n = len(cities)
    visibility = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                visibility[i][j] = 1 / euclidean_distance(cities[i], cities[j])
    return visibility

def calculate_probability(from_city, feasible_cities, pheromone, visibility, alpha, beta):
    pheromone_visibility_product = [
        (pheromone[from_city][i] ** alpha) * (visibility[from_city][i] ** beta) for i in feasible_cities
    ]
    sum_pheromone_visibility = sum(pheromone_visibility_product)
    probabilities = [p / sum_pheromone_visibility for p in pheromone_visibility_product]
    return probabilities, feasible_cities

def pick_next_city(probabilities, feasible_cities):
    r = random.random()
    cumulative_probability = 0.0
    for i, probability in enumerate(probabilities):
        cumulative_probability += probability
        if r <= cumulative_probability:
            return feasible_cities[i]

def update_pheromone(pheromone, tours, decay, additional_pheromone):
    for i, row in enumerate(pheromone):
        for j, value in enumerate(row):
            pheromone[i][j] *= (1 - decay)
    for tour, cost in tours.items():
        for i in range(len(tour) - 1):
            pheromone[tour[i]][tour[i + 1]] += additional_pheromone / cost

def ant_colony_optimization(cities, n_robots, n_iterations=100, alpha=1, beta=2, decay=0.1, initial_pheromone=1):
    n = len(cities)
    pheromone = initialize_pheromone_matrix(n, initial_pheromone)
    visibility = calculate_visibility(cities)
    best_cost = float('inf')
    best_solution = None

    for iteration in range(n_iterations):
        tours = {i: [i] for i in range(n_robots)}
        for robot in range(n_robots):
            current_city = robot
            while len(tours[robot]) < len(cities) // n_robots + 1:
                feasible_cities = [i for i in range(n) if i not in tours[robot]]
                probabilities, feasible_cities = calculate_probability(
                    current_city, feasible_cities, pheromone, visibility, alpha, beta)
                next_city = pick_next_city(probabilities, feasible_cities)
                tours[robot].append(next_city)
                current_city = next_city
            tours[robot].append(robot)  # Return to starting city

        # Calculate cost of the tours
        tours_cost = {}
        for robot, tour in tours.items():
            cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
            tours_cost[tour] = cost
            if cost < best_cost:
                best_cost = cost
                best_solution = tours
        
        update_pheromone(pheromone, tours_cost, decay, initial_pheromone)

    return best_solution, best_cost

# Example usage:
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]
n_robots = 8
best_solution, best_cost = ant_colony_optimization(cities, n_robots)
print("Best Solution:", best_solution)
print("Best Cost:", best_cost)