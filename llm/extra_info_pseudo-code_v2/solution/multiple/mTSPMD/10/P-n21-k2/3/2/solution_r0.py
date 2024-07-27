import math
import random

# Data Setup
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
depots = [0, 1]
robots = {0: 0, 1: 1}  # Robot ID mapped to starting depot index

# Parameters
antnum = 50
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 5.0
rho = 0.1

# Calculate Euclidean distance
def calculate_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Initialize distance matrix and pheromone levels
distances = [[calculate_distance(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))]
pheromones = [[inittrail for _ in range(len(coordinates))] for _ in range(len(coordinates))]

def choose_next_city(current, allowed):
    probabilities = []
    denominator = sum((pheromones[current][l] ** alpha) * ((1 / distances[current][l]) ** beta) for l in allowed)
    for next_city in allowed:
        probabilities.append((pheromones[current][next_city] ** alpha) * ((1 / distances[current][next_city]) ** beta) / denominator)
    return random.choices(allowed, weights=probabilities)[0]

def construct_solution():
    robots_tours = {0: [depots[0]], 1: [depots[1]]}
    all_cities = set(range(len(coordinates)))
    remaining_cities = all_cities - set(depots)

    while remaining_cities:
        for robot in robots:
            if remaining_cities:
                current = robots_tours[robot][-1]
                allowed = [city for city in remaining_cities if city not in robots_tours[robot]]
                if allowed:
                    next_city = choose_next_city(current, allowed)
                    robots_tours[robot].append(next_city)
                    remaining_cities.remove(next_city)
    
    # Return to depots
    for robot in robots:
        robots_tours[robot].append(depots[robot])
    
    return robots_tours

best_tours = None
best_cost = float('inf')

for cycle in range(cyclenum):
    solutions = []
    for _ in range(antnum):
        solution = construct_solution()
        solutions.append(solution)

    # Evaluate and update pheromone trails
    for solution in solutions:
        cost = sum(distances[solution[robot][i]][solution[robot][i+1]] for robot in solution for i in range(len(solution[robot]) - 1))
        if cost < best_cost:
            best_cost = cost
            best_tours = solution
    
    # Pheromone evaporation
    for i in range(len(pheromones)):
        for j in range(len(pheromones[i])):
            pheromones[i][j] *= (1 - rho)

    # Pheromone deposition
    for tour in solutions:
        for robot in tour:
            for i in range(len(tour[robot]) - 1):
                i1, i2 = tour[robot][i], tour[robot][i+1]
                pheromones[i1][i2] += 1 / best_cost
                pheromones[i2][i1] = pheromones[i1][i2]

# Output solutions
for robot in best_tours:
    tour = best_tours[robot]
    tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    print(f'Robot {robot} Tour: {tour}')
    print(f'Robot {robot} Total Travel Cost: {tour_cost}')

print(f'Overall Total Travel Cost: {best_cost}')