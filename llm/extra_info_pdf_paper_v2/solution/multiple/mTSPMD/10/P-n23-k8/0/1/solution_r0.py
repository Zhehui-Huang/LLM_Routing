import numpy as np
import random
from math import sqrt
import itertools

# Coordinates of cities (indexed from 0 - 22)
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
               (45, 35), (32, 39), (56, 37)]

# Number of robots and their depots
robots_and_depots = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Variables related to Ant Colony System
num_ants = 30
pheromone = np.ones((23, 23))
desirability = 1 / (np.array(distances) + 1e-10)  # To avoid zero division
evaporation_rate = 0.5
pheromone_deposit = 0.1
iterations = 100
alpha = 1  # Influence of pheromone
beta = 2   # Influence of desirability (heuristic information)

def aco_algorithm():
    best_solution = None
    best_cost = float('inf')

    for iteration in range(iterations):
        routes = []
        for ant in range(num_ants):
            # Start tours for each robot at their respective depots
            tours = {robot: [depot] for robot, depot in robots_and_depots.items()}
            free_cities = set(range(23)) - set(robots_and_depots.values())

            while free_cities:
                for robot, tour in tours.items():
                    current_city = tour[-1]
                    if not free_cities:
                        break
                    probabilities = []
                    for city in free_cities:
                        prob = (pheromone[current_city][city] ** alpha) * (desirability[current_city][city] ** beta)
                        probabilities.append(prob)
                    probabilities /= sum(probabilities)
                    next_city = np.random.choice(list(free_cities), p=probabilities)
                    tours[robot].append(next_city)
                    free_cities.remove(next_city)

            # Complete the tours back to respective depots
            for robot, tour in tours.items():
                tour.append(tour[0])
                routes.append(tour)

        # Calculate cost and update pheromone trails
        cost = 0
        for route in routes:
            for i in range(1, len(route)):
                start, end = route[i-1], route[i]
                cost += distances[start][end]
                pheromone[start][end] *= (1 - evaporation_rate)
                pheromone[start][end] += pheromone_deposit * (1 / distances[start][end])
        
        if cost < best_cost:
            best_cost = cost
            best_solution = routes

    return best_solution, best_cost

best_routes, overall_cost = aco_algorithm()

# Displaying routes and costs
for robot_id, route in enumerate(best_routes):
    route_cost = sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot1} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")