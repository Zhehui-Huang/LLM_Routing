import numpy as np
import random

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

# Define parameters for the ACO algorithm
antnum = 30
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 2.0
rho = 0.5

# Calculate Euclidean distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i, j] = np.hypot(cities[i][0] - cities[j][0], cities[i][1] - cities[j][1])
    return distance_matrix

distance_matrix = calculateameliorate_distance_matrix(cities)

# Initialize pheromone levels
pheromone_levels = np.full((16, 16), inittrail)

# Heuristic information (inverse of distance matrix)
heuristic_info = 1 / (distance_matrix + 1e-10)

# Function to select the next city
def select_next_city(current_city, allowed_cities):
    probabilities = pheromone_levels[current_city, allowed_cities] ** alpha * heuristic_info[current_city, allowed_cities] ** beta
    probabilities /= probabilities.sum()
    return np.random.choice(allowed_cities, p=probabilities)

# Run ACO algorithm
def ant_colony_optimization():
    best_solution = None
    best_cost = float('inf')
    
    for cycle in range(cyclenum):
        solutions = []
        costs = []
        
        for ant in range(antnum):
            start_depot = random.randint(0, 7)  # randomly choose a depot for each ant
            tour = [start_depot]
            visited = set(tour)
            current_city = start_depot
            
            while len(visited) < 16:
                allowed_cities = [i for i in range(16) if i not in visited]
                if not allowed_cities:
                    break
                next_city = select_next_city(current_city, allowed_cities)
                tour.append(next_city)
                visited.add(next_city)
                current_city = next_city
            
            tour.append(start_depot)  # complete the tour by returning to the depot
            solutions.append(tour)
            cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
            costs.append(cost)
        
        # Find the best solution in the current cycle
        cycle_best_cost = min(costs)
        if cycle_best_cost < best_cost:
            best_cost = cycle_best_cost
            best_solution = solutions[costs.index(cycle_best_cost)]
        
        # Update pheromones
        pheromone_levels *= (1 - rho)
        for solution, cost in zip(solutions, costs):
            for i in range(len(solution) - 1):
                pheromone_levels[solution[i], solution[i+1]] += 1 / cost
    
    return best_solution, best_cost

best_solution, best_cost = ant_colony_optimization()

print("Best Solution:", best_solution)
print("Best Total Cost:", best_cost)