import numpy as np
import random
import math

# City Coordinates and number of robots
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
depots = [0, 1]  # Depot indices
num_robots = 2

# Parameters setting
antnum = 30
cyclenum = 100
init_pheromone = 1.0
alpha = 1
beta = 2
rho = 0.1

# Calculate distance matrix
def euclidean_dist(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

n = len(coordinates)
dist_matrix = np.array([[euclidean_dist(i, j) for j in range(n)] for i in range(n)])

# Initializing pheromone matrix
pheromone = np.full((n, n), init_pheromone)

# Main ACO algorithm
def run_aco():
    best_tours = None
    best_cost = float('inf')
    stagnant_cycles = 0
    current_best_cost = float('inf')

    for cycle in range(cyclenum):
        all_tours = []
        all_costs = []
        for ant in range(antnum):
            tours = [[depot] for depot in depots]
            unvisited = set(range(n)) - set(depots)
            for robot in range(num_robots):
                current_city = tours[robot][-1]
                while unvisited:
                    probabilities = []
                    for city in unvisited:
                        if city in depots:
                            continue
                        heuristic = 1 / dist_matrix[current_city][city]
                        probability = (pheromone[current_city][city] ** alpha) * (heuristic ** beta)
                        probabilities.append(probability)
                    probabilities = np.array(probabilities)
                    probabilities /= probabilities.sum()
                    
                    chosen_city = np.random.choice(list(unvisited), p=probabilities)
                    tours[robot].append(chosen_city)
                    unvisited.remove(chosen_city)
                    current_city = chosen_city

                tours[robot].append(tours[robot][0])  # Return to the starting depot

            tour_costs = [sum(dist_matrix[tours[i][j]][tours[i][j + 1]] for j in range(len(tours[i]) - 1)) for i in range(num_robots)]
            all_tours.append(tours)
            all_costs.append(sum(tour_costs))

        # Update the best tours and costs
        idx_best = np.argmin(all_costs)
        if all_costs[idx_best] < best_cost:
            best_cost = all_costs[idx_best]
            best_tours = all_tours[idx_best]
            stagnant_cycles = 0
        else:
            stagnant_cycles += 1

        # Update pheromone trails
        pheromone *= (1 - rho)
        for tours, cost in zip(all_tours, all_costs):
            contribution = 1 / cost
            for tour in tours:
                for j in range(len(tour) - 1):
                    pheromone[tour[j]][tour[j + 1]] += contribution

        # Check for stopping criterion
        if stagnant_cycles >= cyclenum:
            break
    
    return best_tours, best_cost

best_tours, best_cost = run_aco()

# Output results
for i, tour in enumerate(best_tours):
    tour_cost = sum(dist_matrix[tour[j]][tour[j + 1]] for j in range(len(tour) - 1))
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Case: {tour_cost}")
print(f"Overall Total Travel Cost: {best_cost}")