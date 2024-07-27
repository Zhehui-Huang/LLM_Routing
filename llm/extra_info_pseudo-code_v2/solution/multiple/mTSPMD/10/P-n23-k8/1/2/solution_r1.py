import numpy as np
import random
from scipy.spatial import distance

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

robots = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

# Hyperparameters
antnum = 50
cyclenum = 100
alpha = 1.0
beta = 5.0
rho = 0.1
init_pheromone = 1.0

# Distances and heuristic
N = len(cities)
distances = np.zeros((N, N))
heuristic = np.zeros((N, N))

for i in cities:
    for j in cities:
        if i != j:
            distances[i][j] = distance.euclidean(cities[i], cities[j])
            heuristic[i][j] = 1.0 / distances[i][j]

# Pheromones
pheromones = np.ones((N, N)) * init_pheromone

def calculate_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def aco():
    best_cost = float('inf')
    best_solution = None

    for _ in range(cyclenum):
        solutions = []
        
        for ant in range(antnum):
            tours = {}
            total_cost = 0
            all_visited = set()

            for r_id, start in robots.items():
                current = start
                tour = [current]
                visited = {current}

                while True:
                    unvisited = [c for c in cities if c not in visited and c not in robots.values()]
                    if not unvisited:
                        break
                    probabilities = []
                    for u in unvisited:
                        probability = (pheromones[current][u] ** alpha) * (heuristic[current][u] ** beta)
                        probabilities.append(probability)
                    
                    probabilities = np.array(probabilities) / sum(probabilities)
                    next_city = np.random.choice(unvisited, p=probabilities)
                    tour.append(next_city)
                    visited.add(next_city)
                    current = next_city

                tour.append(start)
                tour_cost = calculate_cost(tour)
                total_cost += tour_cost
                tours[r_id] = tour

            solutions.append((total_cost, tours))

        # Pheromone update
        pheromones *= (1 - rho)
        for cost, s_tours in solutions:
            if cost < best_cost:
                best_cost = cost
                best_solution = s_tours

            for r_id, tour in s_tours.items():
                for i in range(len(tour) - 1):
                    pheromones[tour[i]][tour[i+1]] += 1.0 / cost

    return best_cost, best_solution

best_cost, best_solution = aco()

# Output results
overall_total_cost = 0
for robot, tour in best_solution.items():
    tour_cost = calculate_cost(tour)
    overall_total_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")