import numpy as np
import random
from itertools import permutations

# Define the city coordinates and robot information
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}
num_robots = 8
depots = [i for i in range(num_robots)]  # Depot ids same as robot numbers

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the cost matrix
cost_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        cost_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Initialize parameters for Ant Colony Optimization
antnum = 20
cyclenum = 100
init_pheromone = 1.0
alpha = 1.0
beta = 2.0
evaporation = 0.5

# Apply the ACO algorithm
pheromone = np.full_like(cost_matrix, init_pheromone)

def transition_probability(k, current_city, allowed_next_cities):
    probabilities = []
    for city in allowed_next_cities:
        tau = pheromone[current_city, city]**alpha
        eta = (1.0 / cost_matrix[current_city, city])**beta
        probabilities.append(tau * eta)
    probabilities = np.array(probabilities)
    probabilities = probabilities / probabilities.sum()  # Normalize
    return np.random.choice(allowed_next_cities, p=probabilities)

def find_solution():
    routes = {depot: [depot] for depot in depots}
    costs = np.zeros(num_robots)

    # Each robot builds its route
    for robot_id in depots:
        current_city = robot_id
        visited_cities = set(routes[robot_id])
        
        while len(visited_cities) < len(cities):
            allowed_cities = [i for i in cities.keys() if i not in visited_cities]
            if not allowed_cities:
                break
            
            next_city = transition_probability(robot_id, current_city, allowed_cities)
            routes[robot_id].append(next_city)
            costs[robot_id] += cost_matrix[current_city, next_city]
            visited_cities.add(next_city)
            current_city = next_city
        
        # Complete the tour by returning to the depot
        routes[robot_id].append(robot_id)
        costs[robotid] += cost_matrix[current_city, robot_id]

    return routes, costs

best_routes = None
best_cost = float('inf')

for cycle in range(cyclenum):
    routes, costs = find_solution()
    cycle_total_cost = costs.sum()
    
    if cycle_total_cost < best_cost:
        best_cost = cycle_total_allocation_cost
        best_routes = routes

    # Update pheromones
    pheromone *= (1 - evaporation)
    for robot_id in depots:
        tour = routes[robot_id]
        for i in range(len(tour) - 1):
            i_city = tour[i]
            j_city = tour[i + 1]
            pheromone[i_city, j_city] += 1.0 / costs[robot_id]
            pheromone[j_city, i_city] += 1.0 / costs[robot_id]

# Output the results
total_travel_cost = sum(costs)
for robot_id in depots:
    print(f"Robot {robot_id} Tour: {best_routes[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot_id]}")

print(f"Overall Total Travel Cost: {total_travel_cost}")