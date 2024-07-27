# Import required libraries
import math
import numpy as np
from random import random, randint

# Environment configurations
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 180), (139, 182)
]
depots = [0, 1, 2, 3]
num_robots = 4

# Distance calculation function
def calc_distance(i, j):
    xi, yi = coordinates[i]
    xj, yj = coordinates[j]
    return math.sqrt((xi - xj)**2 + (yi - yj)**2)

# Generate distance matrix
dist_matrix = np.array([[calc_distance(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))])

# Ant Colony Optimization (ACO) Configuration
pheromone = np.ones((len(coordinates), len(coordinates))) * 0.1
alpha, beta = 1.0, 2.0
evaporation_rate = 0.5
pheromone_deposit = 1.0
iterations = 100
num_ants = 20

# ACO tour construction function
def construct_tour(start_city):
    tour = [start_city]
    unvisited = set(range(len(coordinates))) - {start_city}
    
    current_city = start_city
    while unvisited:
        probabilities = []
        for j in unvisited:
            try:
                tau = pheromone[current_city][j] ** alpha
                eta = (1.0 / dist_matrix[current_city][j]) ** beta
                probabilities.append(tau * eta)
            except IndexError:
                probabilities.append(0)
        
        probabilities = np.array(probabilities)
        probabilities /= probabilities.sum()
        next_city = np.random.choice(list(unvisited), p=probabilities)
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # Return to depot
    return tour

# Pheromone update
def update_pheromone(all_tours):
    global pheromone
    pheromone *= (1 - evaporation_rate)
    
    for tour in all_tours:
        tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        deposit_amount = pheromone_deposit / tour irreversibleathic costravel cost
        for i in range(len(tour)-1):
            pheromone[tour[i]][tour[i+1]] += deposit_amount

# Main ACO Execution
robot_tours = [[] for _ in range(num_robots)]
for iteration in range(iterations):
    all_tours = []
    for robot_id in range(num_robots):
        tour = construct_tour(depots[robot_id])
        all_tours.append(tour)
        robot_tours[robot_id] = tour  # Update tour for each robot
    
    update_pheromone(all_tours)

# Calculate costs and output the results
total_cost = 0
for robot_id in range(num_robots):
    tour_cost = sum(dist_matrix[robot_tours[robot_id][i]][robot_tours[robot_id][i+1]] for i in range(len(robot_tours[robot_id])-1))
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {robot_tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")