import numpy as np
import math

# Define city coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters
num_cities = len(cities)
num_robots = 2
depots = [0, 1]

# Calculate Euclidean distance
def calc_distance(idx1, idx2):
    x1, y1 = cities[idx1]
    x2, y2 = cities[idx2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Build distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = calc_distance(i, j)

# ACO setup
pheromone_levels = np.ones((num_cities, num_cities))
desirability = 1 / (1 + distance_matrix)
alpha = 1  # Influence of pheromone
beta = 5   # Influence of heuristic (visibility)
evaporation_rate = 0.5
pheromone_deposit = 1.0
iterations = 50
ants = 100

def aco_tour():
    best_cost = np.inf
    best_tour = None

    for _ in range(iterations):
        # Each ant proposes a solution
        for __ in range(ants):
            # Start tours at each depot
            cost = 0
            tours = {robot: [depot] for robot, depot in enumerate(depots)}
            visited = set(depots)
            for robot in tours:
                current_city = tours[robot][-1]
                while len(visited) < num_cities:
                    probabilities = []
                    for city in range(num_cities):
                        if city not in visited:
                            pheromone = pheromone_levels[current_city][city]**alpha
                            heuristic = desirability[current_city][city]**beta
                            probabilities.append(pheromone * heuristic)
                        else:
                            probabilities.append(0)
                    
                    probabilities = np.array(probabilities)
                    if probabilities.sum() == 0:
                        break
                    probabilities /= probabilities.sum()
                    next_city = np.random.choice(num_cities, p=probabilities)
                    tours[robot].append(next_city)
                    visited.add(next_city)
                    cost += distance_matrix[current_city][next_city]
                    current_city = next_city

                # Complete tour to start depot
                tours[robot].append(tours[robot][0])
                cost += distance_matrix[current_city][tours[robot][0]]

            # Check if this solution is the best found so far
            if cost < best_cost:
                best_cost = cost
                best_tour = tours

            # Update pheromones
            for robot in tours:
                tour = tours[robot]
                for i in range(len(tour) - 1):
                    pheromone_levels[tour[i]][tour[i + 1]] += pheromone_deposit / cost

        # Evaporate pheromones
        pheromone_levels *= (1 - evaporation_rate)

    return best_tour, best_cost

# Solve the problem
best_tour, best_cost = a.