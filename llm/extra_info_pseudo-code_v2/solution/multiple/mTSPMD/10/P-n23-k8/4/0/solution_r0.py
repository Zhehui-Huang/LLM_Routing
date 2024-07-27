import numpy as np
import random

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
n_cities = len(cities)

# Calculate distances matrix
dist_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            dist_matrix[i, j] = np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Ant Colony Optimization parameters
antnum = 30
cyclenum = 100
initPheromone = 1.0
alpha = 1.0
beta = 5.0
rho = 0.1

pheromones = initPheromone * np.ones((n_cities, n_cities))

# Heuristic information (inverse of distance)
eta = 1 / (dist_matrix + np.where(dist_matrix == 0, np.inf, 0))

def select_next_city(current_city, allowed_cities):
    probabilities = pheromones[current_city, allowed_cities] ** alpha * eta[current_city, allowed_cities] ** beta
    probabilities /= probabilities.sum()
    next_city = np.random.choice(allowed_cities, p=probabilities)
    return next_city

def update_pheromone(ant_tours, costs):
    global pheromones
    pheromones *= (1 - rho)
    for tour, cost in zip(ant_tours, costs):
        for i in range(len(tour) - 1):
            pheromones[tour[i], tour[i+1]] += 1 / cost
            pheromones[tour[i+1], tour[i]] += 1 / cost  # if assuming symmetric TSP

# Robots and their respective depot cities
depots = list(range(8))
robot_tours = dict.fromkeys(depots)

# Best tours and minimal cost found
best_tours = {depot: None for depot in depots}
best_costs = {depot: np.inf for depot in depots}

for cycle in range(cyclenum):
    for depot in depots:
        allowed_cities = list(set(range(n_cities)) - set(depots))
        current_city = depot
        tour = [depot]
        while allowed_cities:
            next_city = select_next_city(current_city, allowed_cities)
            tour.append(next_city)
            allowed_cities.remove(next_city)
            current_city = next_city
        tour.append(depot)

        # Calculate tour cost
        cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
        if cost < best_costs[depot]:
            best_costs[depot] = cost
            best_tours[depot] = tour

    update_pheromone(list(best_tours.values()), list(best_costs.values()))

# Output tours and costs for each robot
overall_cost = 0
for depot in sorted(depots):
    print(f"Robot {depot} Tour: {best_tours[depot]}")
    print(f"Robot {depot} Total Travel Cost: {best_costs[depot]:.2f}")
    overall_cost += best_costs[depot]

print(f"Overall Total Travel Cost: {overall_cost:.2f}")