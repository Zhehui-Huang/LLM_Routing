import numpy as np
import random

# Cities and their coordinates
CITIES = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = CITIES[city1]
    x2, y2 = CITIES[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Total number of cities
num_cities = len(CITIES)

# Establishing the distance matrix
distance_matrix = np.array([[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)])

# Number of ants, same as the number of cities
num_ants = num_cities

# Initial pheromone concentration
pheromones = np.ones((num_cities, num_cities))

# Parameter setup for ACO
alpha = 1.0   # Influence of pheromone
beta = 2.0    # Influence of heuristic information (1/distance)
evaporation_rate = 0.5
pheromone_deposit_weight = 1.0

# Run ACO algorithm to find Tours for each Robot
def ant_colony_optimization(num_iterations):
    best_cost_global = float('inf')
    best_solutions_global = []
    
    for iteration in range(num_iterations):
        routes = []
        route_costs = []
        
        # Each ant creates a solution
        for ant in range(num_ants):
            # Start from random cities for diversification
            start_city = ant % num_cities
            current_city = start_city
            tour = [current_city]
            allowed_cities = list(range(num_cities))
            allowed_cities.remove(current_city)
            
            # Build the tour
            while allowed_cities:
                transition_probabilities = []
                for city in allowed_cities:
                    pheromone = pheromones[current_city][city]**alpha
                    heuristic = (1.0 / distance_matrix[current_city][city])**beta
                    transition_probabilities.append(pheromone * heuristic)
                
                transition_probabilities /= np.sum(transition_probabilities)
                next_city = np.random.choice(allowed_cities, p=transition_probabilities)
                tour.append(next_city)
                allowed_cities.remove(next_city)
                current_city = next_city
            
            tour.append(start_city)
            tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            routes.append(tour)
            route_costs.append(tour_cost)
        
        # Update pheromones
        pheromones *= evaporation_rate
        for i, route in enumerate(routes):
            for j in range(len(route) - 1):
                pheromones[route[j]][route[j+1]] += pheromone_deposit_weight / route_costs[i]
        
        # Check for new best solution in this iteration
        min_cost = min(route_costs)
        if min_cost < best_cost_global:
            best_cost_global = min_cost
            best_solutions_global = [routes[i] for i, cost in enumerate(route_costs) if cost == min_cost]
    
    return best_solutions_global, best_cost_global

# Running the ACO
best_solutions, best_cost = ant_colony_optimization(num_iterations=100)
print("Best Solutions:", best_solutions)
print("Best Cost:", best_cost)