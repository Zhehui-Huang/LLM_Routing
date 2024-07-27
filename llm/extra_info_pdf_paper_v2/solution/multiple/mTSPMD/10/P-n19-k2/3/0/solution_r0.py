import numpy as np
import random

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Distance matrix using Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Ant Colony Optimization parameters:
num_ants = 30
num_iterations = 100
decay = 0.5
alpha = 1  # influence of pheromone
beta = 2   # influence of heuristic information
initial_pheromone = 1 / len(cities)

# Initialization: Pheromone levels
pheromones = np.full((len(cities), len(cities)), initial_pheromone)

# ACO Algorithm implementation
def aco_algorithm(pheromones, distance_matrix):
    best_cost = float('inf')
    best_solution = []
    
    for _ in range(num_iterations):
        all_tours = []
        all_costs = []
        
        for __ in range(num_ants):
            # Each ant generates a tour starting from a random depot
            start = random.choice([0, 1])  # Randomly pick a depot for each ant
            tour = [start]
            unvisited = set(range(2, len(cities)))  # Exclude depots
            
            while unvisited:
                current = tour[-1]
                probs = []
                
                for city in unvisited:
                    pheromone = pheromones[current][city]**alpha
                    heuristic = (1 / distance_matrix[current][city])**beta
                    probs.append(pheromone * heuristic)
                
                probs = np.array(probs) / sum(probs)
                next_city = np.random.choice(list(unvisited), p=probs)
                tour.append(next_city)
                unvisited.remove(next_city)
            
            tour.append(tour[0])  # Return to the depot
            cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            
            all_tours.append(tour)
            all_costs.append(cost)
        
        # Update the best solution found
        for cost, tour in zip(all_costs, all_tours):
            if cost < best_cost:
                best_cost = cost
                best_solution = tour
        
        # Pheromone evaporation
        pheromones *= decay
        
        # Pheromone update by the best tour
        for i in range(len(best_solution) - 1):
            pheromones[best_solution[i]][best_solution[i+1]] += 1 / best_cost
    
    return best_solution, best_cost

best_tour, best_cost = aco_algorithm(pheromones, distance_matrix)

# Output formatting
print(f"Best Tour: {best_tour}")
print(f"Best Tour Total Travel Cost: {best_cost}")