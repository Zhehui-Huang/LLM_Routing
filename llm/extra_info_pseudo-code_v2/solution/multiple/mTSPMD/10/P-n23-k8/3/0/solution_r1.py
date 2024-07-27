import numpy as np
from scipy.spatial.distance import euclidean

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Initialize parameters
num_cities = len(cities)
pheromone_levels = np.ones((num_cities, num_cities)) * 0.1
distances = np.zeros((num_cities, num_cities))

# Calculate distances matrix
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean(cities[i], cities[j])

# Parameters for ACO
num_ants = 8
alpha = 1
beta = 2
evaporation = 0.5
iterations = 100

# Allocate ants to starting and ending depots
depots = [0, 1, 2, 3, 4, 5, 6, 7]

# ACO Algorithm
best_route = None
best_cost = float('inf')

for iteration in range(iterations):
    routes = []
    route_costs = []
    
    for ant in range(num_ants):
        route = [depots[ant]] # Start at respective depot
        unvisited = set(range(num_cities)) - {route[0]}
        
        while unvisited:
            current = route[-1]
            probabilities = []
            
            for next_city in unvisited:
                trail = pheromone_levels[current][next_city] ** alpha
                visibility = (1.0 / distances[current][next_city]) ** beta
                probabilities.append(trail * visibility)
            
            probabilities /= np.sum(probabilities)
            next_city = np.random.choice(list(unvisited), p=probabilities)
            route.append(next_city)
            unvisited.remove(next_city)
        
        route.append(depots[ant]) # Return to starting depot
        routes.append(route)
        
        # Calculate cost of the route
        cost = 0
        for i in range(1, len(route)):
            cost += distances[route[i - 1]][route[i]]
        route_costs.append(cost)
    
    # Update best route and cost
    current_best_cost = min(route_costs)
    if current_best_cost < best_cost:
        best_cost = current_best_cost
        best_route = routes[route_costs.index(current_best_cost)]
    
    # Update pheromone levels
    pheromone_levels *= (1 - evaporation)  # Evaporation
    for r in range(num_ants):
        for i in range(1, len(routes[r])):
            pheromone_levels[routes[r][i - 1]][routes[r][i]] += 1 / route_costs[r]

# Output the results
total_cost = 0
for ant in range(num_ants):
    robot_tour = routes[ant]
    robot_cost = route_costs[ant]
    total_cost += robot_cost
    print(f"Robot {ant} Tour: {robot_tour}")
    print(f"Robot {ant} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {total_cost}")