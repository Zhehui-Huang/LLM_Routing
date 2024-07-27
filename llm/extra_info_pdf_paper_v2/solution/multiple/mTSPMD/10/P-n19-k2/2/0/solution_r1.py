import numpy as np
import math
from random import randrange, choice

# City coordinates
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters for ACO
num_ants = 20
num_iterations = 100
evaporation_rate = 0.5
alpha = 1  # Phreromone importance
beta = 5   # Distance importance
pheromone = np.ones((19, 19))
visibility = np.zeros((19, 19))

# Compute distances and visibility
def euclidean_distance(a, b):
    return math.sqrt((city_coords[a][0] - city_coords[b][0])**2 + (city_counter[a][1] - city_coords[b][1])**2)

# Initialize visibility
for i in range(19):
    for j in range(19):
        if i != j:
            visibility[i][j] = 1 / euclidean_distance(i, j)

def ant_colony_optimization():
    best_tours = None
    best_cost = float('inf')
    
    for iteration in range(num_iterations):
        routes = [[0], [1]]  # Starting points for each robot
        for _ in range(num_ants):
            unvisited = set(range(2, 19))
            costs = [0, 0]  # Initial costs for the tours

            for robot in range(2):
                current_city = robot  # start at depot
                while unvisited:
                    # Select the next city
                    next_city = None
                    if unvisited:
                        probabilities = []
                        for city in unvisited:
                            probabilities.append(((pheromone[current_city][city] ** alpha) *
                                                 (visibility[current_city][city] ** beta), city))
                        probabilities = sorted(probabilities, reverse=True)
                        next_city = probabilities[0][1]  # Choose the city with the highest probability

                        # Update the tour and costs
                        routes[robot].append(next_city)
                        costs[robot] += euclidean_distance(current_city, next_city)
                        current_city = next_city
                        unvisited.remove(next_city)

                # Return to the depot
                routes[robot].append(robot)
                costs[robot] += euclidean_distance(current_city, robot)

            # Calculate total cost
            total_cost = sum(costs)

            # Update pheromone trails
            for route, cost in zip(routes, costs):
                for i in range(len(route) - 1):
                    pheromone[route[i]][route[i+1]] += 1 / cost  # Increase pheromone

            # Evaporate pheromone
            pheromone *= (1 - evaporation_rate)

            if total_cost < best_cost:
                best_cost = total_cost
                best_tours = routes

    return best_tours, best_cost

# Find solution using ACO
best_solution, best_cost = ant_colony_optimization()

# Outputting solution
for i, tour in enumerate(best_solution):
    tour_cost = sum(euclidean_distance(tour[j], tour[j+1]) for j in range(len(tour) - 1))
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")
print(f"Overall Total Travel Cost: {best_cost}")