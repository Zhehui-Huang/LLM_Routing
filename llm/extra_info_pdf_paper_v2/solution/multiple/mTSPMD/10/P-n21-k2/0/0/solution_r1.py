import numpy as np
import random

# City coordinates
cities = [
    (30, 40),  # Depot 0 for robot 0
    (37, 52),  # Depot 1 for robot 1
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots and their depots
depots = [0, 1]
robots = len(depots)

# Compute the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return np.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Distance matrix
num_cities = len(cities)
distance_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Ant Colony Optimization parameters
num_ants = 100
num_iterations = 200
decay = 0.1
alpha = 1.0  # Phromone importance
beta = 5.0    # Distance importance
Q = 10.0      # Pheromone left on the trail per unit of distance

# Initialize pheromones
pheromones = np.ones((num_cities, num_cities)) * 0.1

# Randomness utility
def choice(p):
    return np.argmax(np.random.multinomial(1, p))

# The Ant Colony System for the mTSP
def ant_colony_optimization():
    best_route = None
    best_cost = float('inf')

    for iteration in range(num_iterations):
        routes = []
        costs = []

        # Generate routes for each ant
        for ant in range(num_ants):
            # Split cities between robots randomly except depots
            robot_routes = {robot: [depots[robot]] for robot in range(robots)}
            remaining_cities = list(set(range(num_cities)) - set(depots))
            random.shuffle(remaining_cities)

            for i, city in enumerate(remaining_cities):
                robot = i % robots
                robot_routes[robot].append(city)

            # Completing routes to return to the respective depots
            for robot in range(robots):
                robot_routes[robot].append(depots[robot])

            # Calculate the total cost of routes
            total_cost = 0
            for robot in range(robots):
                route_cost = sum(distance_matrix[robot_routes[robot][i]][robot_routes[robot][i+1]] for i in range(len(robot_routes[robot])-1))
                total_cost += route_cost

            routes.append(robot_routes)
            costs.append(total_cost)

            # Update best solution found
            if total_cost < best_cost:
                best_cost = total_cost
                best_route = robot_routes

        # Pheromone update
        for i in range(num_cities):
            for j in range(num_cities):
                pheromones[i][j] *= (1 - decay)
        
        # Add the pheromone of the best route in this iteration
        for robot, route in best_route.items():
            for k in range(len(route) - 1):
                i, j = route[k], route[k+1]
                pheromones[i][j] += Q / best_cost

    return best_route, best_cost

# Execute the Ant Colony Optimization
best_route, best_cost = ant_colony_optimization()

# Printing the results
overall_total_cost = 0
for robot_id, tour in best_route.items():
    route_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_total_cost += route_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {round(route_cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_total_cost, 2)}")