import numpy as np
from scipy.spatial.distance import euclidean
from collections import defaultdict

# Define the city coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247), 
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231), 
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193), 
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Number of robots and depots
robot_info = {0: 0, 1: 1, 2: 2, 3: 3}
num_cities = len(cities)
num_robots = len(robot_info)

# Calculate distances between each pair of cities
distances = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean(cities[i], cities[j])
        else:
            distances[i][j] = float('inf')

# ACO parameters
num_ants = 20
pheromone = np.ones((num_cities, num_cities)) * 0.1
desirability = 1 / distances
evaporation_rate = 0.5
alpha = 1  # influence of pheromone
beta = 1   # influence of desirability
iterations = 100

def aco_tsp():
    best_route = None
    best_cost = float('inf')
    
    for iteration in range(iterations):
        routes = []
        costs = []
        
        for _ in range(num_ants):
            route = generate_route()
            cost = calculate_cost(route)
            routes.append(route)
            costs.append(cost)
        
        # Update pheromones
        for i in range(num_cities):
            for j in range(num_cities):
                pheromone[i][j] *= (1 - evaporation_rate)
        
        for route, cost in zip(routes, costs):
            for i in range(len(route) - 1):
                a, b = route[i], route[i + 1]
                pheromone[a][b] += 1 / cost
        
        # Check for best solution
        for cost, route in sorted(zip(costs, routes)):
            if cost < best_cost:
                best_cost = cost
                best_route = route
    
    return best_route, best_cost

def generate_route():
    route = []
    visitable = list(range(num_cities))
    current_city = np.random.choice(list(robot_info.values()))  # start at a depot
    
    while visitable:
        next_city_choices = [(pheromone[current_city][j] ** alpha) * (desirability[current_city][j] ** beta) for j in visitable]
        next_city_probs = next_city_choices / np.sum(next_city_choices)
        next_city = np.random.choice(visitable, p=next_city_probs)
        
        route.append(current_city)
        visitable.remove(current_city)
        current_city = next_city
    
    route.append(route[0])  # return to the starting depot
    return route

def calculate_cost(route):
    return sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))


# Applying the ACO algorithm
final_route, final_cost = aco_tsp()

# Printing route and cost details
print("Final Route:")
print(final_route)
print("Final Total Travel Cost:")
print(final_cost)