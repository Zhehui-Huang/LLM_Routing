import numpy as np
import random

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Parameters
antnum = 10
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 5.0
rho = 0.1

# Initialize distances and heuristic information (inverse of distance)
n_cities = len(cities)
distances = np.zeros((n_cities, n_cities))
eta = np.zeros((n_cities, n_cities))  # Heuristic information
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            dist = np.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)
            distances[i][j] = dist
            eta[i][j] = 1.0 / dist

# Pheromone matrix
pheromone = np.ones((n_cities, n_cities)) * inittrail

def choose_next_city(current_city, allowed_cities, pheromone, eta):
    probabilities = np.zeros(len(allowed_cities))
    pheromone_vector = pheromone[current_city, allowed_cities]
    eta_vector = eta[current_city, allowed_cities]
    
    probabilities = (pheromone_vector ** alpha) * (eta_vector ** beta)
    probabilities /= probabilities.sum()
    
    return np.random.choice(allowed_cities, p=probabilities)

def simulate_ants(start_city, antnum, pheromone, eta):
    tours = []
    for _ in range(antnum):
        tour = [start_city]
        allowed_cities = list(range(n_cities))
        allowed_cities.remove(start_city)
        
        while allowed_cities:
            current_city = tour[-1]
            next_city = choose_next_city(current_city, allowed_cities, pheromone, eta)
            tour.append(next_city)
            allowed_cities.remove(next_city)
        
        tour.append(start_city)  # Return to depot
        tours.append(tour)
    return tours

def update_pheromone(pheromone, tours, rho):
    pheromone *= (1 - rho)
    for tour in tours:
        for i in range(len(tour) - 1):
            pheromone[tour[i]][tour[i+1]] += 1.0 / calculate_tour_cost(tour, distances)
    return pheromone

def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Main optimization cycle
for cycle in range(cyclenum):
    tours_0 = simulate_ants(0, antnum // 2, pheromone, eta)
    tours_1 = simulate_ants(1, antnum // 2, pheromone, eta)
    pheromone = update_pheromone(pheromone, tours_0 + tours_1, rho)

# Select the best tours
best_tour_0 = min(tours_0, key=lambda tour: calculate_tour_cost(tour, distances))
best_tour_1 = min(tours_1, key=lambda tour: calculate_tour_cost(tour, distances))
cost_0 = calculate_tour_cost(best_tour_0, distances)
cost_1 = calculate_tour_cost(best_tour_1, distances)

print("Robot 0 Tour:", best_tour_0)
print("Robot 0 Total Travel Cost:", cost_0)
print("\nRobot 1 Tour:", best_tour_1)
print("Robot 1 Total Travel_cost:", cost_1)
print("\nOverall Total Travel_cost:", cost_0 + cost_1)