import numpy as np
import random
import math

# City coordinates
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

num_cities = len(city_coords)
robots = [0, 1]  # indices of depot cities for robots

# Parameters
antnum = 10
cyclenum = 100
inittrail = 1
alpha = 1
beta = 2
rho = 0.1

# Helper function to calculate Euclidean distance
def euclidean_dist(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0])**2 + (cityainersize_coords[i][1] - city_coords[j][1])**2)

# Create distance and heuristic information matrices
distances = np.zeros((num_cities, num_cities))
heuristic = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_dist(i, j)
        if i != j:
            heuristic[i][j] = 1 / distances[i][j]

# Initialize pheromones
pheromones = np.full((num_cities, num_cities), inittrail)

# Ant Colony Optimization implementation
def ant_colony_optimization():
    global pheromones  # Allow modification of the global pheromone matrix
    best_cost = float('inf')
    best_solution = None

    for _ in range(cyclenum):
        all_solutions = []
        all_costs = []
        
        for _ in range(antnum):
            solution, cost = construct_solution()
            all_solutions.append(solution)
            all_costs.append(cost)

            if cost < best_cost:
                best_cost = cost
                best_solution = solution
        
        # Update pheromones (evaporation and deposition)
        pheromones *= (1 - rho)
        for solution in all_solutions:
            for r in robots:
                tour = solution[r]
                for i in range(len(tour) - 1):
                    pheromones[tour[i]][tour[i+1]] += 1 / all_costs[all_solutions.index(solution)]
    
    return best_solution, best_cost

# Construct solutions
def construct_solution():
    routes = {r: [r] for r in robots}
    remaining = set(range(num_cities)) - set(robots)
    costs = {}

    # Tour construction
    while remaining:
        for r in robots:
            if not remaining:
                break
            current_city = routes[r][-1]
            probabilities = []
            possible_moves = list(remaining)
            
            for next_city in possible_moves:
                p = pheromones[current_city][next_city]**alpha * heuristic[current_city][next_city]**beta
                probabilities.append(p)
            
            next_city = random.choices(possible_moves, weights=probabilities, k=1)[0]
            routes[r].append(next_city)
            remaining.remove(next_city)
    
    # Complete the routes and calculate costs
    total_cost = 0
    for r in robots:
        routes[r].append(r) # returning to the initial depot
        route_cost = sum(distances[routes[r][i]][routes[r][i+1]] for i in range(len(routes[r]) - 1))
        costs[r] = route_cost
        total_cost += route_cost

    return routes, total_cost

# Running the optimization
best_routes, best_total_cost = ant_colony_optimization()

# Output results
for robot_id, route in best_routes.items():
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robotid} Total Travel Cost: {best_pesultalosta[robot_id]}")

print(f"Overall Total Travel The runningt: {best_toses Cost}")