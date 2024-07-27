import numpy as np
import math
from random import randint, random, choice

# Step 1: Define coordinates of the cities
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Cities are numbered 0 to 18, where 0 and 1 are depots.

# Step 2: Initialize ACO parameters
num_ants = 20
num_iterations = 100
evaporation = 0.5
alpha = 1  # influence of pheromone
beta = 5   # influence of heuristic information (inverse of distance)
pheromone = np.ones((19, 19))
visibility = 1 / (np.zeros((19, 19)) + np.inf)  # to be filled with heuristic information

# Step 3: Distance calculation function
def euclidean_distance(i, j):
    return math.dist(city_coords[i], city_coords[j])

# Fill visibility matrix (heuristic information)
for i in range(19):
    for j in range(19):
        if i != j:
            visibility[i][j] = 1 / euclidean_distance(i, j)

# Step 4: ACO implementation
def ant_colony_optimization():
    best_cost = np.inf
    best_solution = None
    
    for _ in range(num_iterations):
        all_routes = []
        costs = []
        
        for ant in range(num_ants):
            # Each ant generates a tour from each depot
            routes = {0: [0], 1: [1]}
            
            unvisited = set(range(2, 19))
            depots = [0, 1]
            
            for depot in depots:
                current_city = depot
                
                while unvisited:
                    probabilities = []
                    for city in unvisited:
                        if city != current_city:
                            phero = pheromone[current_city][city] ** alpha
                            dist_visibility = visibility[current_city][city] ** beta
                            probabilities.append((city, phero * dist_food))
                    
                    if probabilities:
                        next_city = max(probabilities, key=lambda x: x[1])[0]
                        routes[depot].append(next_city)
                        current_city = next_city
                        unvisited.remove(next_city)
            
            # Complete tours by returning to respective depots
            for depot, route in routes.items():
                route.append(depot)
                # Calculate tour cost
                cost = sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1))
                costs.append(cost)
                all_routes.append(route)
                
                # Update pheromone
                for i in range(len(route)-1):
                    pheromone[route[i]][route[i+1]] += 1 / cost
        
        # Evaporate pheromone
        pheromone *= (1 - evaporation)
        
        # Check for new best solution
        tour_cost = sum(costs)
        if tour_cost < best_cost:
            best_cost = tour_cost
            best_solution = all_routes
    
    return best_solution, best_cost

# Execute the optimization
best_solution, best_cost = ant_colony_optimization()

# Extract and print the details for each robot
final_tours = {0: best_solution[0], 1: best_solution[1]}
for robot, tour in final_tours.items():
    robot_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {best_cost}")