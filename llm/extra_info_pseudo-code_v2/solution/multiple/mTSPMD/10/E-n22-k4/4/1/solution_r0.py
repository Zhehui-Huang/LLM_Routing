import numpy as np
import math

# Coordinates of the cities (indexed from 0 to 21)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Parameters for ACO
antnum = 20
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 2.0
rho = 0.1

# Initialize pheromones trails
distances = np.zeros((len(coordinates), len(coordinates)))
pheromones = np.full((len(coordinates), len(coordinates)), inittrail)

for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            x_dist = coordinates[i][0] - coordinates[j][0]
            y_dist = coordinates[i][1] - coordinates[j][1]
            distances[i][j] = math.sqrt(x_dist**2 + y_dist**2)
eta = 1 / distances  # heuristic information

def choose_next_city(current_city, allowed):
    choices_weight = []
    for city in allowed:
        choices_weight.append(pheromones[current_city][city] ** alpha * eta[current_city][city] ** beta)
    choice_probs = np.array(choices_weight)
    choice_probs /= choice_probs.sum()
    return np.random.choice(allowed, 1, p=choice_probs)[0]

def simulate_ants():
    solutions = []
    costs = []
    for _ in range(antnum):
        tour = [0]
        allowed = list(range(1, len(coordinates)))
        while allowed:
            current_city = tour[-1]
            next_city = choose_next_city(current_city, allowed)
            tour.append(next_city)
            allowed.remove(next_data)
        tour.append(0) # return to the starting depot
        tours.append(tour)
        total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        costs.append(total_cost)
    
    best_tour_index = np.argmin(costs)
    best_tour = tours[best_tour_index]
    best_cost = costs[best_tour_index]
    return best_tour, best_cost

def update_pheromones(tour, cost):
    Lk = 1 / cost
    for i in range(len(tour) - 1):
        pheromones[tour[i]][tour[i+1]] += Lk

# Main ACO process
best_tour_global = None
best_cost_global = float('inf')
for _ in range(cyclenum):
    best_tour_cycle, best_cost_cycle = simulate_ants()
    if best_cost_cycle < best_cost_global:
        best_tour_global = best_tour_cycle
        best_cost_global = best_cost_cycle
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            pheromones[i][j] *= (1 - rho)  # Evaporation

    update_pheromones(best_tour_cycle, best_cost_cycle)

# Output the solution in the specified format
print(f"Robot 0 Tour: {best_tour_global}")
print(f"Robot 0 Total Travel Cost: {best_cost_global}")
print(f"Overall Total Travel Cost: {best_cost_global}")