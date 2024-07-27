import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Data initialization
depots = list(range(8))  # 8 depots from 0 to 7
cities = list(range(8, 16))  # 8 other cities from 8 to 15
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Initialize distances and heuristic info
distances = {}
heuristics = {}
nodes = depots + cities
for i in nodes:
    for j in nodes:
        if i != j:
            dist = euclidean(coordinates[i], coordinates[j])
            distances[(i, j)] = dist
            heuristics[(i, j)] = 1 / dist

# Parameters
antnum = 10
cyclenum = 100
inittrail = 0.1
alpha = 1
beta = 2
rho = 0.5

# Pheromone initialization
pheromones = {k: inittrail for k in distances.keys()}

# Tour construction
def construct_tour(start_depot):
    tour = [start_depot]
    current = start_depot
    visited = set(tour)
    
    while len(visited) < len(nodes):
        if current in depots and current != start_depot:
            # Break if a robot ends up in a different depot
            break
        moves = [(pheromones[(current, k)] ** alpha) * (heuristics[(current, k)] ** beta)
                 for k in nodes if k not in visited and (current, k) in pheromones]
        if not moves:  # If no move is possible
            break
        probabilities = np.array(moves) / sum(moves)
        next_node = np.random.choice([k for k in nodes if k not in visited and (current, k) in pheromones], p=probabilities)
        tour.append(next_node)
        visited.add(next_node)
        current = next_node
    tour.append(start_depot)  # Return to start depot
    return tour

# Main cycle
best_solution = None
best_cost = float('inf')

for _ in range(cyclenum):
    all_tours = []
    all_costs = []
    # Construct solutions
    for depot in depots:
        tour = construct_tour(depot)
        all_tours.append(tour)
        cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
        all_costs.append(cost)

    # Find best solution
    cost_sum = sum(all_costs)
    if cost_sum < best_cost:
        best_solution = all_tours
        best_cost = cost_sum
    
    # Update pheromones (evaporation and reinforcement)
    for key in pheromones:
        pheromones[key] *= (1 - rho)
        
    for index, tour in enumerate(all_tours):
        for i in range(len(tour) - 1):
            pheromones[(tour[i], tour[i + 1])] += 1 / all_costs[index]

# Output the results
print("Best Solution:")
for idx, tour in enumerate(best_solution):
    print(f"Robot {idx} Tour: {tour}")
    tour_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    print(f"Robot {idx} Total Travel Cost: {tour verdict}")

print(f"Overall Total Travel Cost: {best_cost}")