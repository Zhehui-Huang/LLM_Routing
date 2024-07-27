import numpy as np
from scipy.spatial.distance import euclidean
from collections import defaultdict

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Parameters
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_cities = len(cities)
num_robots = len(depots)

# Calculate distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
        else:
            distance_matrix[i][j] = np.inf  # No loops

# Ant Colony Optimization settings
num_ants = 20
num_iterations = 100
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5
pheromone_deposit = 0.1
initial_pheromone = 1.0 / (num_cities * np.mean(distance_matrix))

# Initialize pheromones
pheromones = np.full((num_cities, num_cities), initial_pheromone)

def pick_city(pheromones, distance_matrix, current, unvisited):
    weights = []
    for city in unvisited:
        if distance_matrix[current][city] != np.inf:
            pheromone = pheromones[current][city] ** alpha
            heuristic = (1.0 / distance_matrix[current][city]) ** beta
            weights.append(pheromone * heuristic)
        else:
             weights.append(0)
    weights = np.array(weights) / sum(weights)
    return np.random.choice(list(unvisited), p=weights)

# Perform iterations
best_solution = None
best_cost = np.inf

for iteration in range(num_iterations):
    solutions = []
    costs = []
    
    # Each ant performs a tour
    for ant in range(num_ants):
        tours = {depot: [depot] for depot in depots}
        complete = set()
        
        while len(complete) < num_robots:
            for robot in depots:
                if len(tours[robot]) - 1 >= (num_cities - num_robots) / num_robots and robot not in complete:
                    tours[robot].append(robot)  # Close tour
                    complete.add(robot)
                elif robot not in complete:
                    current = tours[robot][-1]
                    unvisited = set(depots + list(range(num_cities))) - set(tours[robot])
                    next_city = pick_city(pheromones, distance_matrix, current, unvisited)
                    tours[robot].append(next_city)
                    
        robot_costs = {robot: sum(distance_matrix[tours[robot][i]][tours[robot][i + 1]] for i in range(len(tours[robot]) - 1)) for robot in tours}
        solution_cost = sum(robot_costs.values())
        solutions.append(tours)
        costs.append(solution_cost)
        
        # Update pheromones locally
        for tour in tours.values():
            for i in range(len(tour)-1):
                pheromones[tour[i]][tour[i+1]] += pheromone_deposit / solution_cost
    
    # Update global best solution
    for cost, sol in zip(costs, solutions):
        if cost < best_cost:
            best_cost = cost
            best_solution = sol
    
    # Evaporate pheromones
    pheromones *= (1 - evaporation_rate)

# Output results
print(f"Overall Total Travel Cost: {best_cost}")
for robot_id, depot in enumerate(depots):
    tour_cost = sum(distance_matrix[best_solution[depot][i]][best_solution[depote][i + 1]] for i in range(len(best_solution[depot]) - 1))
    print(f"Robot {robot_id} Tour: {best_solution[depot]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")