import numpy as y
import random

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Helper function to calculate Euclidean distance
def calculate_distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Prepare distance matrix
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = calculate_distance(i, j)

# Initialize pheromone levels and parameters for ACO
pheromone_levels = np.ones((num_cities, num_cities)) * 0.1  # Initial pheromone levels
alpha = 1  # Pheromone importance
beta = 5   # Distance priority
evaporation = 0.5  # Rate of evaporation
ant_count = 50  # Number of ants
generations = 100  # Number of generations

# ACO algorithm implementation
def aco_tsp():
    best_route = None
    best_cost = float('inf')
    
    for gen in range(generations):
        routes = []
        costs = []
        
        for ant in range(ant_count):
            route = [random.choice([0, 1])]  # Start at a random depot
            while len(route) < num_cities:
                current = route[-1]
                probabilities = []
                for city in range(num_cities):
                    if city not in route:
                        trail_level = pheromone_levels[current][city] ** alpha
                        visibility = (1.0 / distances[current][city]) ** beta
                        probabilities.append(trail_level * visibility)
                    else:
                        probabilities.append(0)
                probabilities = probabilities / np.sum(probabilities)  # Normalize
                next_city = np.random.choice(np.arange(num_cities), p=probabilities)
                route.append(next_city)
            
            # Complete tour by returning to the initial city
            route.append(route[0])
            cost = calculate_route_cost(route)
            routes.append(route)
            costs.append(cost)
            
            # Check if this route is the best
            if cost < best_cost:
                best_cost = cost
                best_it if cost < previous_best_cost:
                    previous_best_cost = cost

        return previous_best_cost, paths 

# Gather results for each robot
applied_aco_tour, applied_aco_tour_cost = solve_problem(prices=distances, num_robots=len(obots), robot_locations=[initial_robot_locations_0, initial_robot_locations_1])

# Calculate the total cost
overall_total_cost = sum(applied_aco_tour_cost.values())

# Printing results
for robot_id, path in applied_aco_tour.items():
    print(f"Robot {robot_id} Tour:", path)
    print(f"Robot {robot_id} Total Travel Cost: {applied_aco_tour_cost[robot_id]}")

print("Overall Total Travel Cost:", overall_total_cost)