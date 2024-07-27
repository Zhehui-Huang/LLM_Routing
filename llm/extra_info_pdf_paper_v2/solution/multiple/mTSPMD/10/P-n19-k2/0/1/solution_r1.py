import numpy as np
from math import sqrt

# City coordinates are predefined
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35) 
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city01[1]) ** 2 + (city2[0] - city2[1]) ** 2)

# Number of cities and robots
n_cities = len(city_coordinates)
n_robots = 2
depots = [0, 1]

# Distances matrix
distances = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distances[i, j] = euclidean_distance(city_coordinates[i], city_coordinates[j])

# Ant Colony Optimization settings
n_ants = 20
n_iterations = 100
decay = 0.1
alpha = 1  # pheromone importance
beta = 5   # distance priority
initial_pheromone = 1 / (n_cities * np.mean(distances))

# Pheromone matrix
pheromone = np.full((n_cities, n_cities), initial_pheromone)

# Choose the probability of choosing a next city
def choice_prob(city, unvisited, pheromone, distances):
    pheromones = pheromone[city][unvisited]
    dists = distances[city][unvisited]
    return (pheromones ** alpha) * ((1. / dists) ** beta)

def aco_fixed_mTSP():
    best_routes = None
    best_cost = float('inf')

    for iteration in range(n_iterations):
        routes = []
        costs = []

        # Each ant generates a route
        for _ in range(n_ants):
            # Robot-specific tours starting from each depot
            robot_tours = {robot: [depots[robot]] for robot in range(n_robots)}
            all_visited = set(depots)
            
            for robot in range(n_robots):
                while len(robot_tours[robot]) - 1 < (n_cities - 2) / n_robots:
                    current_city = robot_tours[robot][-1]
                    unvisited = list(set(range(n_cities)) - all_visited)
                    if not unvisited:
                        break
                    probs = choice_prob(current_city, unvisited, pheromone, distances)
                    next_city = np.random.choice(unvisited, p=probs / probs.sum())
                    robot_tours[robot].append(next_city)
                    all_visited.add(next_city)
                # Return to starting depot
                robot_tours[robot].append(depots[robot])

            # Calculate the cost of the tours
            total_cost = 0
            for robot, tour in robot_tours.items():
                tour_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
                total_cost += tour_cost
                costs.append(tour_cost)
                routes.append(tour)

            # Update best solution if found new best
            if total_cost < best_cost:
                best_cost = total_cost
                best_routes = robot_tours
        
        # Pheromone evaporation
        pheromone *= (1 - decay)

        # Pheromone deposit
        for robot, route in enumerate(routes):
            for i in range(len(route) - 1):
                pheromone[route[i], route[i + 1]] += costs[robot] / total_cost

    # Output the results for each robot
    for robot, tour in best_routes.items():
        print(f"Robot {robot} Tour: {tour}")
        print(f"Robot {robot} Total Travel Cost: {sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))}")

    print(f"Overall Total Travel Cost: {best_cost}")

aco_fixed_mTSP()