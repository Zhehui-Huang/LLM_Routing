import numpy as np
import math
import random
import time

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
    (37, 69), (61, 33), (62, 63), (63, 67), (45, 35)
]

# Euclidean distance calculation
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Generate distance matrix
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = calc_distance(coordinates[i], coordinates[j])

# Initialize solution
def initialize_solution(num_robots):
    nodes = list(range(1, n))  # excluding the depot
    random.shuffle(nodes)
    tours = [[] for _ in range(num_robots)]
    for index, node in enumerate(nodes):
        tours[index % num_robots].append(node)
    return tours

# Calculate tour cost
def calculate_cost(tour):
    total_cost = distance_matrix[0][tour[0]] + distance_matrix[tour[-1]][0]
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i + 1]]
    return total_cost

# Shake the solution
def shake(tours, k):
    for _ in range(k):
        # Choose two different tours
        r1, r2 = np.random.choice(len(tours), 2, replace=False)
        if tours[r1] and tours[r2]:  # make sure both tours are not empty
            i1, i2 = np.random.randint(len(tours[r1])), np.random.randint(len(tours[r2]))
            # Swap cities
            tours[r1][i1], tours[r2][i2] = tours[r2][i2], tours[r1][i1]
        
    return tours

# Local search with 2-opt
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_cost(new_tour) < calculate_cost(best):
                    best = new_tour
                    improved = True
    return best

# General VNS
def gvns(num_robots, max_time):
    tours = initialize_solution(num_robots)
    start_time = time.time()
    while time.time() - start_time < max_time:
        k = 1
        while k < 4:
            new_tours = shake(tours, k)
            new_tours = [two_opt(tour) for tour in new_tours]
            if max(calculate_cost(t) for t in new_tours) < max(calculate_cost(t) for t in tours):
                tours = new_tours
                k = 1
            else:
                k += 1
    return tours

# Set parameters
num_robots = 2
execution_time = 5  # seconds

# Execute GVNS
final_tours = gvns(num_robots, execution_time)
final_costs = [calculate_cost(t) for t in final_tours]
max_final_cost = max(final_costs)

# Print tours and costs
for i, tour in enumerate(final_tours):
    print(f"Robot {i} Tour: [0, " + ", ".join(map(str, tour)) + ", 0]")
    print(f"Robot {i} Total Travel Cost: {final_costs[i]}")
print(f"Maximum Travel Cost: {max_final_cost}")