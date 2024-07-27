import numpy as np
import random

# Coordinates of cities
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Number of cities and robots
num_cities = len(coordinates)
num_robots = 2
depots = [0, 1]

# Calculate Euclidean distance matrix
def calc_distance_matrix(coords):
    n = len(coords)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
    return distance_matrix

distance_matrix = calc_distance_matrix(coordinates)

# Simplified Ant Colony Optimization (ACO) algorithm
def ant_colony_optimization(num_robots, num_cities, distance_matrix, depots, num_ants=10, num_iterations=100, alpha=1, beta=2, evaporation_rate=0.5, Q=100):
    # Initialize pheromones
    pheromones = np.ones((num_cities, num_cities))
    
    # Record the best solution found
    best_cost = float('inf')
    best_solution = None
    
    for iteration in range(num_iterations):
        solutions = []
        for ant in range(num_ants):
            # Each ant generates a solution
            tours = [[] for _ in range(num_robots)]
            remaining_cities = set(range(num_cities)) - set(depots)
            
            # Start from each depot
            for i in range(num_robots):
                tours[i].append(depots[i])
            
            # Construct the tours
            for i in range(num_robots):
                current_city = depots[i]
                while remaining_cities:
                    probabilities = []
                    for city in remaining_cities:
                        try:
                            tau = pheromones[current_city][city] ** alpha
                            eta = (1 / distance_matrix[current_city][city]) ** beta
                            probabilities.append((city, tau * eta))
                        except ZeroDivisionError:
                            probabilities.append((city, 0))
                    
                    probabilities = sorted(probabilities, key=lambda x: x[1], reverse=True)
                    next_city = random.choices([p[0] for p in probabilities], weights=[p[1] for p in probabilities], k=1)[0]
                    
                    tours[i].append(next_city)
                    remaining_cities.remove(next_city)
                    current_city = next_city
                tours[i].append(depots[i])
            
            solutions.append(tours)
        
        # Evaluate solutions and update pheromones
        for tours in solutions:
            total_cost = sum(distance_matrix[tours[i][j]][tours[i][j + 1]] for i in range(num_robots) for j in range(len(tours[i]) - 1))
            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = tours
            
            for tour in tours:
                for i in range(len(tour) - 1):
                    pheromones[tour[i]][tour[i + 1]] += Q / total_cost
        
        # Evaporate pheromones
        pheromones *= (1 - evaporation_rate)
    
    return best_solution, best_cost

best_tours, best_cost = ant_colony_optimization(num_robots, num_cities, distance_matrix, depots)

# Output the tours and costs
total_cost = 0
for i, tour in enumerate(best_tours):
    tour_cost = sum(distance_matrix[tour[j]][tour[j + 1]] for j in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")