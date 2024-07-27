import numpy as np
import math
from random import choice, seed

# Initialization of city data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

depot_starts = {i: i for i in range(8)}  # Robots correspond to depots 0 to 7

num_robots = 8
alpha = 1.0
beta = 2.0
rho = 0.1
init_pheromone = 1.0
num_ants = 32
num_cycles = 100

# Function to calculate Euclidean distance
def calc_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create distance and initial pheromone matrices
n = len(cities)
distances = np.zeros((n, n))
eta = np.zeros_like(distances)
pheromones = np.full_like(distances, init_pheromone)

for i in range(n):
    for j in range(n):
        if i != j:
            distances[i, j] = calc_distance(cities[i], cities[j])
            eta[i, j] = 1.0 / distances[i, j]

# Decision function for next city
def select_next_city(current, allowed, pheromones, dist_inv):
    probs = pheromones[current, allowed] ** alpha * dist_inv[current, allowed] ** beta
    probs /= np.sum(probs)
    return np.random.choice(allowed, p=probs)

# Simulation of one ant's tour starting from a specific depot
def ant_tour(depot, pheromones):
    tour = [depot]
    visited = set(tour)
    while len(visited) < n:
        current = tour[-1]
        allowed = [i for i in range(n) if i not in visited]
        if not allowed:  # Shouldn't happen, but a safety check
            break
        next_city = select_next_city(current, allowed, pheromones, eta)
        tour.append(next_city)
        visited.add(next_city)
    tour.append(depot)  # Return to starting depot
    return tour

# Calculate total length of a tour
def tour_length(tour):
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Main simulation
best_tours = None
best_cost = float('inf')

for cycle in range(num_cycles):
    tours = []
    total_cost = 0
    new_pheromones = np.zeros_like(pheromones)

    for _ in range(num_ants):
        for depot in depot_starts.values():
            tour = ant_tour(depot, pheromones)
            cost = tour_length(tour)
            total_cost += cost
            for i in range(len(tour) - 1):
                new_pheromones[tour[i], tour[i+1]] += 1000.0 / cost  # Better tours add more pheromone

    pheromones = (1 - rho) * pheromones + new_pheromones  # Update pheromones

    if total_cost < best_cost:
        best_cost = total_cost
        best_tours = tours

# Print results
print(f"Overall Total Travel Cost: {best_cost}")
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_length(tour)}")