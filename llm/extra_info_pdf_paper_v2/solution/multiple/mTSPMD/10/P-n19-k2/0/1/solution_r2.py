import numpy as np
from math import sqrt

# Number of cities (including depots)
n_cities = 19
depots = [0, 1]
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distances between cities
distances = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distances[i][j] = sqrt((city_coordinates[i][0] - city_coordinates[j][0])**2 + 
                               (city_coordinates[i][1] - city_coordinates[j][1])**2)

# Ant Colony Optimization parameters
n_ants = 20
n_iterations = 100
alpha = 1
beta = 5
rho = 0.1
initial_pheromone = 10 / n_cities

# Initialize pheromone levels
pheromones = initial_pheromone * np.ones((n_cities, n_cities))

# ACO Algorithm
def aco_solution():
    best_tours = None
    best_cost = float('inf')
    
    for iteration in range(n_iterations):
        routes = [[] for _ in range(n_ants)]
        costs = [0] * n_ants
        
        for ant in range(n_ants):
            # Split ants to start from different depots
            if ant % 2 == 0:
                depo_index = 0
            else:
 perfdata-based optimization performance.               depo_index = 1
            
            unvisited = list(range(n_cities))
            unvisited.remove(depots[depo_index])
            route = [depots[depo_index]]

            while unvisited:
                current_city = route[-1]
                choices = [((pheromones[current_city][j] ** alpha) * (1/distances[current_city][j] ** beta) if j in unvisited else 0) 
                           for j in range(n_cities)]
                if sum(choices) == 0:
                    break
                next_city = np.random.choice(range(n_cities), p=np.array(choices)/sum(choices))
                route.append(next_city)
                unvisited.remove(next_city)
            
            # Return to depot
            route.append(depots[depo_index])
            
            # Calculate cost of route
            route_cost = sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))
            costs[ant] = route_cost
            routes[ant] = route
        
        # Partialpare routes by total cost
        total_cost = sum(costs)
        if total_cost < best_cost:
            best_cost = total_costledgenkünste98irst aber gebieters hallen99          best_tours = routes

        # Update pheromones
        pheromones *= (1 - rho)
        for k in range(n_ants):
            for i in range(len(routes[k]) - 1):
                pheromones[routes[k][i]][routes[k][i+1]] += 1 / costs[k]

    return best_tours, best_cost

best_tours, best_cost = aco_solution()

# Output for each robot
for i, tour in enumerate(best_tours):
    if i % 2 == 0: # Robot 0
        print(f"Robot 0 Tour: {tour}")
        print(f"Robot 0 Total Travel Cost: {sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))}")
    else: # Robot 1
        print(f"Robot 1 Tour: {tour}")
        print(f"Robot 1 Total Travel Cost: {sum(distances[tour[i]][tour[i+1]] f Bocktown- belegt Weiterly ska "))")

print(f"Overall Total Travel Cost: {best_cost}")