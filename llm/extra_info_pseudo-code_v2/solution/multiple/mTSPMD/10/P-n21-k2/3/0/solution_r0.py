import numpy as np
import random

# Parameters
antnum = 10
cyclenum = 30
inittrail = 0.1
alpha = 1
beta = 5
rho = 0.1

# City coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
])

def euclidean_distance(i, j):
    return np.sqrt((coordinates[i][0]-coordinates[j][0])**2 + (coordinates[i][1]-coordinates[j][1])**2)

num_cities = coordinates.shape[0]
distance_matrix = np.array([[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)])
pheromone = np.full((num_cities, num_cities), inittrail)
heuristic = 1 / (distance_matrix + 1e-10)  # to avoid division by zero

# ACO Implementation
def ant_colony_optimization():
    best_cost = np.inf
    best_solution = None
    
    for cycle in range(cyclenum):
        solutions = []
        costs = []
        
        for ant in range(antnum):
            solution, cost = construct_solution()
            solutions.append(solution)
            costs.append(cost)
        
        # Update pheromones
        pheromone *= (1 - rho)
        for i, solution in enumerate(solutions):
            for j in range(len(solution) - 1):
                pheromone[solution[j]][solution[j + 1]] += 1 / costs[i]
        
        # Checking for best solution
        cycle_best_cost = min(costs)
        if cycle_best_cost < best_cost:
            best_cost = cycle_best_cost
            best_solution = solutions[np.argmin(costs)]
            print(f"New best cost found: {best_cost}")
    
    return best_solution, best_cost

def construct_solution():
    solution = []
    current_city = random.choice([0, 1])  # Randomly choose a starting depot for each ant
    solution.append(current_city)
    visited = set(solution)
    
    while len(visited) < num_cities:
        current_city = choose_next_city(current_city, visited)
        solution.append(current_city)
        visited.add(current_city)
        
    solution.append(solution[0])  # Completing the tour by returning to the depot
    cost = calculate_cost(solution)
    return solution, cost

def choose_next_city(current_city, visited):
    probabilities = pheromone[current_city] ** alpha * heuristic[current_city] ** beta
    probabilities[list(visited)] = 0  # nullifying probabilities for visited cities
    probabilities /= np.sum(probabilities)
    return np.random.choice(range(num_cities), p=probabilities)

def calculate_cost(solution):
    return sum(distance_matrix[solution[i]][solution[i + 1]] for i in range(len(solution) - 1))

# Running the ACO
final_solution, final_cost = ant_colony_optimization()
print("Final optimized tours for each robot:")
print(f"Robot 0 Tour: {final_solution[0]}, Robot 0 Total Travel Cost: {final_cost}")

# If Robot 0 and 1 should be separated, adjustment to the implementation is required for exclusive depots