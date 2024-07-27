import numpy as np
import random

# Coordinates for each city including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Parameters for ACO
antnum = 50
cyclenum = 100
init_pheromone = 1.0
alpha = 1.0
beta = 2.0
rho = 0.5

# Initialize pheromone levels
num_cities = len(coordinates)
pheromones = np.full((num_cities, num_cities), init_pheromone)
robots = len(range(8))
robot_start_depots = range(robots)

def distance(city1_idx, city2_idx):
    x1, y1 = coordinates[city1_idx]
    x2, y2 = coordinates[city2_idx]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Transition probability calculation
def transition_probability(i, j, pheromones, desirability):
    return (pheromones[i][j] ** alpha) * (desirability[i][j] ** beta)

def construct_solution(start_city):
    tour = [start_city]
    visited = set(tour)
    current_city = start_city
    
    while len(visited) < num_cities:
        probabilities = []
        cities = []
        for next_city in range(num_cities):
            if next_city not in visited:
                prob = transition_probability(current_city, next_city, pheromones, desirability)
                probabilities.append(prob)
                cities.append(next_city)
        probabilities = np.array(probabilities)
        probabilities /= probabilities.sum()
        next_city = np.random.choice(cities, p=probabilities)
        tour.append(next_city)
        visited.add(next_city)
        current_city = next_city
    tour.append(start_city)  # return to the depot
    return tour

# The main optimization loop
best_solution = None
best_cost = float('inf')
desirability = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            desirability[i][j] = 1 / distance(i, j)

for cycle in range(cyclenum):
    solutions = []
    costs = []
    for ant in range(antnum):
        start_city = random.choice(robot_start_depots)
        solution = construct_solution(start_city)
        cost = sum(distance(solution[i], solution[i+1]) for i in range(len(solution) - 1))
        solutions.append((cost, solution))
        costs.append(cost)
    cycle_best_cost, cycle_best_solution = min(solutions, key=lambda x: x[0])
    
    if cycle_best_cost < best_cost:
        best_cost = cycle_best_cost
        best_solution = cycle_best_solution

    # Updating pheromones
    pheromones *= (1 - rho)
    for cost, solution in solutions:
        for i in range(len(solution) - 1):
            pheromones[solution[i]][solution[i+1]] += 1 / cost

# Printing the solution found
total_cost = 0
for i, start_city in enumerate(robot_start_depots):
    tour = [start_city]
    next_city = start_city
    for _ in range((num_cities // robots) - 1):
        next_city = best_solution[next_city]
        tour.append(next_city)
    tour.append(start_current)
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f'Robot {i} Tour: {tour}')
    print(f'Robot {i} Total Travel Cost: {tour_cost}')

print(f'Overall Total Travel Cost: {total_cost}')