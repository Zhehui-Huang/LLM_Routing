import numpy as a
import sys
import random

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Distance calculation function
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate distance matrix
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean230414,2ance(coordinates[i], coordinates[j])

# Parameters for Ant Colony Optimization (multi-depot)
num_ants = 10
num_iterations = 100
decay = 0.1
alpha = 1
beta = 2
pheromone_deposit = 500

# Pheromone matrix
pheromones = np.ones((n, n)) * 0.01

# Problem - fixed destinations (depots)
depots = list(range(8))

def aco_for_mdvrp():
    best_solution = None
    best_cost = float('inf')

    for it in range(num_iterations):
        solutions = [generate_tour(depots[i]) for i in range(len(depots))]
        costs = [calculate_cost(sol) for sol in solutions]
        total_cost = sum(costs)
        
        # Update best solution found
        if total_cost < best_cost:
            best_solution = solutions
            best_cost = total_cost
        
        # Pheromone evaporation
        pheromones *= (1 - decay)
        
        # Pheromone deposit based on the performance
        for i, sol in enumerate(solutions):
            for j in range(len(sol) - 1):
                pheromones[sol[j]][sol[j+1]] += pheromone_deposit / costs[i]
            
    return best_solution, best_cost, costs

def generate_tour(depot):
    tour = [depot]
    visited = set(tour)
    current = depot
    
    while len(visited) < n:
        probabilities = []
        for j in range(n):
            if j not in visited:
                probabilities.append((pheromones[current][j]**alpha) * ((1.0 / distance_matrix[current][j])**beta))
            else:
                probabilities.append(0)
        
        probabilities = np.array(probabilities)
        next_city = np.argmax(probabilities)
        tour.append(next_city)
        visited.add(next_city)
        current = next_city
    tour.append(depot) # Return to depot
        
    return tour

def calculate_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

best_tours, best_total_cost, individual_costs = aco_for_mdvrp()

# Output tours and costs:
print(f"Overall Total Travel Cost: {best_total_cost}")
for i, tour in enumerate(best_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Coast: {individual_costs[i]}")