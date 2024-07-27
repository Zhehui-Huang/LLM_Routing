import numpy as np
import math
import random

# Provided city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_cities = len(coordinates)

distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = math.sqrt((coordinates[i][0] - coordinates[j][0])**2 +
                                          (coordinates[i][1] - coordinates[j][1])**2)

# Simple ACO setup
num_ants = 20
alpha = 1.0  # Influence of pheromone
beta = 5.0   # Influence of heuristic (inverse of distance)
evaporation = 0.5
pheromone_deposit = 1.0
iterations = 10
pheromone = np.ones((num_cities, num_cities)) * 0.1

# Get the initial tours using ACO
def aco_tsp():
    best_route = None
    best_cost = float('inf')
    
    for _ in range(iterations):
        for _ in range(num_ants):
            routes = {depot: [depot] for depot in depots}
            local_pheromone = np.zeros((num_cities, num_cities))
            
            for robot_id, start_depot in enumerate(depots):
                current_city = start_depot
                visited = set([start_depot])
                route = [start_depot]
                
                while len(visited) < num_cities:
                    probabilities = []
                    total_probs = 0
                    
                    for next_city in range(num_cities):
                        if next_city not in visited:
                            tau = pheromone[current_city][next_city] ** alpha
                            eta = (1.0 / distance_matrix[current_city][next_city]) ** beta
                            prob = tau * eta
                            probabilities.append((prob, next_city))
                            total_probs += prob
                    
                    if probabilities:
                        chosen_city = random.choices([x[1] for x in probabilities], 
                                                     weights=[x[0] for x in probabilities], k=1)[0]
                        route.append(chosen_city)
                        local_pheromone[current_city][chosen_city] += pheromone_deposit
                        current_city = chosen_city
                        visited.add(chosen_city)
                
                route.append(start_depot)  # complete the cycle
                routes[robot_id] = route
            
            # Pheromone evaporation
            pheromone *= (1 - evaporation)
            # Pheromone update
            pheromone += local_pheromone
            
            # Calculate tour cost
            tour_costs = {}
            total_tour_cost = 0
            for robot_id, tour in routes.items():
                cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
                tour_costs[robot_id] = cost
                total_tour_cost += cost
            
            if total_tour_cost < best_cost:
                best_cost = total_tour_cost
                best_route = routes

    return best_route, tour_costs, best_cost

# Obtain the best routes and costs
best_route, tour_costs, overall_best_cost = aco_tsp()

# Output results
for robot_id in range(num_robots):
    print(f"Robot {robot_id} Tour: {best_route[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_best_cost}")