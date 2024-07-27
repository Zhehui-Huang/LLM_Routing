import numpy as np
import math
import random
import time

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Euclidean distance calculation
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Generate distance matrix
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_menuix[i][j] = calc_distance(coordinates[i], coordinates[j])

# Initialize solution
def initialize_solution(m):
    tours = [[] for _ in range(m)]
    # Start at the depot for each robot
    for tour in tours:
        tour.append(0)
    nodes = list(range(1, n))  # all nodes excluding the depot
    nodes_sorted = sorted(nodes, key=lambda x: distance_matrix[0][x])
    
    # Distribute nodes evenly
    for index, node in enumerate(nodes_sorted):
        tours[index % m].append(node)
        
    # Each tour ends back at the depot
    for tour in tours:
        tour.append(0)
    return tours

# Calculate tour cost
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

# Randomly modify tour to find new local optima
def modify_tour(tours, k):
    for _ in range(k):
        robot1, robot2 = random.sample(range(len(tours)), 2)
        if len(tours[robot1]) > 2 and len(tours[robot2]) > 2:  # Ignore depot-only tours
            node1 = random.choice(tours[robot1][1:-1])  # Ignore depot
            node2 = random.choice(tours[robot2][1:-1])  # Ignore depot
            idx1 = tours[robot1].index(node1)
            idx2 = tours[robot2].index(node2)
            # Swap nodes
            tours[robot1][idx1], tours[robot2][idx2] = tours[robot2][idx2], tours[robot1][idx1]
    return tours

# GVNS wrapper
def gvns(m, duration_seconds):
    tours = initialize_solution(m)
    start_time = time.time()
    max_duration = duration_seconds

    while time.time() - start_time < max_duration:
        modify_tour(tours, 10)  # small random perturbations
        for tour in tours:
            random.shuffle(tour[1:-1])  # No not shuffle the depot

    return tours

# Parameters
num_robots = 2
seconds = 5  # Allow 5 seconds for the GVNS to execute

# Perform GVNS search
result_tours = gvns(num_robots, seconds)
result_costs = [tour_cost(t) for t in result_tours]
max_cost = max(result_costs)

# Print results
for idx, tour in enumerate(result_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {result_costs[idx]}")

print(f"Maximum Travel Cost: {max_cost}")