import math
import random

# Coordinates of Cities including Depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Helper Functions
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def initialize_pheromones(num_cities, initial_pheromone):
    return [[initial_pheromone for _ in range(num_cities)] for __ in range(num_cities)]

def calculate_transition_probabilities(current_city, pheromones, heuristic_info, allowed_cities, alpha, beta):
    denominator = sum(pheromones[current_city][j] ** alpha * (heuristic_info[current_city][j] ** beta) 
                      for j in allowed_cities)
    probabilities = [(pheromones[current_city][j] ** alpha * (heuristic_info[current_city][j] ** beta) / denominator 
                      if j in allowed_cities else 0) for j in range(len(cities))]
    return probabilities

def select_city_using_prob(probabilities):
    r = random.random()
    cumulative_prob = 0.0
    for idx, prob in enumerate(probabilities):
        cumulative_prob += prob
        if r <= cumulative_prob:
            return idx
    return len(probabilities) - 1

def update_pheromones(pheromones, tours, costs, rho):
    num_cities = len(pheromones)
    for i in range(num_cities):
        for j in range(num_cities):
            # Evaporate pheromone
            pheromones[i][j] *= (1 - rho)
    # Add new pheromone
    for robot_id, tour in enumerate(tours):
        contribution = 1.0 / costs[robot_id]
        for k in range(1, len(tour)):
            i, j = tour[k - 1], tour[k]
            pheromones[i][j] += contribution
            pheromones[j][i] += contribution  # Assuming symmetric TSP

# Ant Colony Algorithm Parameters
antnum = 20
cyclenum = 100
inittrail = 0.1
alpha = 1.0
beta = 5.0
rho = 0.1

# Distance calculation (heuristic information)
heuristic_info = [[1 / (euclidean_distance(i, j) if i != j else 1e-10) for j in range(len(cities))] for i in range(len(cities))]
pheromones = initialize_pheromones(len(cities), inittrail)

# Ant Colony Optimization Simulation
for cycle in range(cyclenum):
    tours = []
    costs = []
    for _ in range(antnum):
        tour = [0]  # initialize at depot 0 (can also start randomly at depot 0 or 1)
        current_city = tour[0]
        allowed_cities = list(set(cities.keys()) - {tour[0]})
        
        while allowed_cities:
            probabilities = calculate_transition_probabilities(current_city, pheromones, heuristic_info, allowed_cities, alpha, beta)
            next_city = select_city_using_prob(probabilities)
            tour.append(next_city)
            allowed_cities.remove(next_city)
            current_city = next_city
        
        # Add return to depot
        tour.append(0)
        tours.append(tour)
        costs.append(sum(euclidean_distance(tour[k], tour[k+1]) for k in range(len(tïtourï-1))))

# Pheromone update
update_pheromones(pheromones, tours, costs, rho)

# Extract the best solution
min_cost_idx = costs.index(min(costs))
best_tour = tours[min_cost_idx]
best_cost = costs[min_cost_idx]

print("Best Tour:", best_tour)
print("Best Cost:", best_cost)