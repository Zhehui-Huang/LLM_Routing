import numpy as sec
import random
from scipy.spatial import distance_matrix

# City coordinates (index 0-7 are depots)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

num_cities = len(coordinates)
num_depots = 8
num_robots = 8

# Create distance matrix
distances = distance_matrix(coordinates, coordinates)

# Parameters for ACO
num_ants = 20
num_iterations = 100
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5
pheromone_deposit = 10
initial_pheromone = 1.0 / num_cities

# Pheromone matrix initialization 
pheromones = np.full((num_cities, num_cities), initial_pheromone)

def select_next_city(current_city, taboo_list):
    """ Probabilistically selects the next city to visit. """
    probabilities = []
    for i in range(num_cities):
        if i not in taboo_list:
            trail_strength = (pheromones[current_city][i] ** alpha) * ((1.0 / distances[current_city][i]) ** beta)
            probabilities.append(trail_strength)
        else:
            probabilities.append(0)
    
    probabilities = np.array(probabilities)
    if probabilities.sum() == 0:
        return -1
    probabilities /= probabilities.sum()
    return np.random.choice(num_cities, p=probabilities)

def compute_tour_cost(tour):
    """ Calculates the cost of a tour. """
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def aco_for_robot(depot_index):
    """ ACO for solving the mTSP for a specific robot starting from a specified depot. """
    best_tour = None
    best_cost = float('inf')
    
    for iteration in range(num_iterations):
        for ant in range(num_ants):
            # Each ant starts at the depot
            tour = [depot_index]
            taboo_list = set(tour)

            while len(taboo_list) < num_cities:
                current_city = tour[-1]
                next_city = select_next_city(current_city, taboo_list)
                if next_city == -1:  # No valid moves
                    break
                tour.append(next_city)
                taboo_list.add(next_city)
            
            tour.append(depot_index)  # End the tour by returning to the depot
            cost = compute_tour_cost(tour)
            
            if cost < best_cost:
                best_cost = cost
                best_tour = tour

            # Pheromone evaporation
            pheromones *= (1 - evaporation_rate)
            
            # Pheromone deposit
            for i in range(len(tour) - 1):
                pheromones[tour[i]][tour[i + 1]] += pheromone_deposit / cost
    
    return best_tour, best_cost

# Assign each robot to a different depot and compute their tours
total_cost = 0
for robot in range(num_robots):
    tour, cost = aco_for_robot(robot)
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")