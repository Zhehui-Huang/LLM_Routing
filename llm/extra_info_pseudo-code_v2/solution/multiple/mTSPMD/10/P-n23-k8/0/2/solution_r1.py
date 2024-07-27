import numpy as np
import math
from random import choice

# City coordinates provided
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Depot indices
depots = list(range(8))

# Algorithm parameters
antnum = 20
cyclenum = 100
init_pheromone = 1.0
alpha = 1.0
beta = 5.0
rho = 0.1

# Distance matrix using Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distances = [
    [calculate_distance(cities[i], cities[j]) for j in range(len(cities))]
    for i in range(len(cities))
]

# Initialize pheromones
pheromones = [
    [init_pheromone for _ in range(len(cities))]
    for _ in range(len(cities))
]

# Calculate heuristic: inverse of distance avoiding division by zero
heuristic = [
    [1 / (distances[i][j] + 1e-10) if i != j else 0 for j in range(len(cities))]
    for i in range(len(cities))
]

def create_solution():
    tours = {robot: [depots[robot]] for robot in range(len(depots))}
    costs = {robot: 0 for robot in range(len(depots))}
    unvisited = set(range(len(cities))) - set(depots)

    for robot in tours:
        while unvisited:
            current = tours[robot][-1]
            if not unvisited:
                break
            probabilities = [
                pheromones[current][j] ** alpha * heuristic[current][j] ** beta if j in unvisited else 0
                for j in range(len(cities))
            ]
            total = sum(probabilities)
            if total == 0:  # Avoid division by zero
                break
            probabilities = [p / total for p in probabilities]
            next_city = np.random.choice(len(cities), p=probabilities)
            tours[robot].append(next_city)
            costs[robot] += distances[current][next_city]
            unvisited.remove(next_city)

        # Return to the depot
        last = tours[robot][-1]
        home = depots[robot]
        tours[robot].append(home)
        costs[robot] += distances[last][home]

        # Allow other robots to work if cities are still unvisited
        if not untransfer:
            break

    return tours, costs

def update_pheromones(all_tours, all_costs):
    for i in range(len(cities)):
        for j in range(len(cities)):
            pheromones[i][j] *= (1 - rho)  # Evaporation

    for robot, tour in all_tours.items():
        tour_length = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        deposit = 1 / tour_length  # Deposit amount
        for i in range(len(tour) - 1):
            pheromones[tour[i]][tour[i + 1]] += deposit

best_solution = None
best_cost_sum = float('inf')

for _ in range(cyclenum):
    all_tours, all_costs = create_solution()
    current_cost_sum = sum(all_costs.values())
    if current_cost_sum < best_cost_sum:
        best_solution = all_tours
        best_cost_sum = current_cost_sum
        update_pheromones(all_tours, all_costs)

# Output results
for robot, tour in best_solution.items():
    robot_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {best_cost_sum}")