import numpy as np
from math import sqrt
import random

# Constants
num_cities = 23
num_robots = 8
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
depots = [0, 1, 2, 3, 4, 5, 6, 7]
depot_to_robot = dict(zip(depots, range(num_robots)))

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Parameters for ACO
pheromone = np.ones((num_cities, num_cities))
desirability = 1 / (np.array(distances) + 1e-10)  # To prevent division by zero
evaporation_rate = 0.5
pheromone_deposit = 0.1
iterations = 100
alpha = 1
beta = 2

# ACO Algorithm
def aco_algorithm():
    best_cost = float('inf')
    best_solution = None

    for iteration in range(iterations):
        # Initialize tours for each robot
        tours = {robot: [depot] for depot, robot in depot_to_robots.items()}
        unvisited = set(range(num_cities)) - set(depots)

        while unvisited:
            for robot, tour in tours.items():
                current_city = tour[-1]
                if not unvisited: break
                probabilities = []
                for next_city in unvisited:
                    prob = (pheromone[current_city][next_city] ** alpha) * (desirability[current_city][next_city] ** beta)
                    probabilities.append(prob)
                probabilities = np.array(probabilities) / sum(probabilities)
                next_city = np.random.choice(list(unvisited), p=probabilities)
                tours[robot].append(next_city)
                unvisited.remove(next_city)
                
        total_cost = 0
        for robot, tour in tours.items():
            tour.append(tour[0])  # Return to start depot
            route_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            total_cost += route_cost
        
        if total_cost < best_cost:
            best_cost = total_cost
            best_solution = tours

    return best_solution, best_cost

best_solution, best_cost = aco_algorithm()

# Display the solution
for robot_id, tour in best_solution.items():
    tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {best_cost}")