import numpy as np
import random

# Constants
num_cities = 19
num_robots = 2
depot_cities = [0, 1]
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
               (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Initialize distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j]))

# Ant Colony Optimization Parameters
num_ants = 40
max_iterations = 100
alpha = 1.0  # Importance of pheromones
beta = 5.0   # Importance of heuristic (inverse of distance)
evaporation_rate = 0.1
pheromone_deposit_amount = 1.0
initial_pheromone = 0.1

# Pheromone matrix
pheromone_matrix = initial_pheromone * np.ones((num_cities, num_cities))

def select_next_city(current_city, unvisited_cities):
    choices = unvisited_cities
    weights = []
    for city in choices:
        pheromone = pheromone_matrix[current_city][city] ** alpha
        heuristic = (1.0 / distance_matrix[current_city][city]) ** beta
        weight = pheromone * heuristic
        weights.append(weight)
    weights = np.array(weights)
    probabilities = weights / np.sum(weights)
    next_city = np.random.choice(choices, p=probabilities)
    return next_city

def aco_tsp():
    global pheromone_matrix
    best_tour_cost = float('inf')
    best_tours = None

    for iteration in range(max_iterations):
        for ant in range(num_ants):
            tours = [[i] for i in depot_cities]

            for robot in range(num_robots):
                unvisited = set(range(num_cities)) - set(tours[robot])

                while unvisited:
                    current_city = tours[robot][-1]
                    next_city = select_next_city(current_city, unvisited)
                    tours[robot].append(next_city)
                    unvisited.remove(next_city)

                # Return to the starting depot
                tours[robot].append(depot_cities[robot])

            # Calculate the cost of the tours
            tours_cost = sum(distance_matrix[tours[i][j]][tours[i][j+1]] for i in range(num_robots) for j in range(len(tours[i])-1))
            
            # Check for the best solution
            if tours_cost < best_tour_cost:
                best_tour_cost = tours_cost
                best_tours = tours

        # Pheromone evaporation
        pheromone_matrix *= (1 - evaporation_rate)

        # Pheromone deposit
        for robot_tour in best_tours:
            for i in range(len(robot_tour)-1):
                pheromone_matrix[robot_tour[i]][robot_tour[i+1]] += pheromone_deposit_amount / best_tour_cost

    return best_tours, best_tour_cost

best_tours, total_cost = aco_tsp()

# Printing results
for i, tour in enumerate(best_tours):
    robot_cost = sum(distance_matrix[tour[j]][tour[j+1]] for j in range(len(tour) - 1))
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {total_cost}")