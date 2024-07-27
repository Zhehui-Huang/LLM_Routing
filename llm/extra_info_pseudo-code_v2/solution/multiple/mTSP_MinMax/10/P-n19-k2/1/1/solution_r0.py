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
        distance_matrix[i][j] = calc_distance(coordinates[i], coordinates[j])

# GVNS components
def initialize_solution(m):
    tours = [[] for _ in range(m)]
    nodes = list(range(1, n))  # ignore the depot for now
    sorted_nodes = sorted(nodes, key=lambda x: distance_matrix[0][x])
    for i in range(m):
        tours[i].append(sorted_nodes[i])
    for j in range(m, len(sorted_nodes)):
        min_cost = float('inf')
        best_tour = -1
        for v in range(m):
            estimated_cost = distance_matrix[tours[v][-1]][sorted_nodes[j]]
            if estimated_cost < min_cost:
                min_cost = estimated_cost
                best_tour = v
        tours[best_tour].append(sorted_nodes[j])
    return tours

def calc_tour_cost(tour):
    tour_cost = distance_matrix[0][tour[0]]  # from depot to first city
    for i in range(1, len(tour)):
        tour_cost += distance_matrix[tour[i-1]][tour[i]]
    tour_cost += distance_matrix[tour[-1]][0]  # return to depot
    return tour_cost

def shake(tours, k):
    all_tours = tours[:]
    while k > 0:
        v = random.randint(0, len(all_tours) - 1)
        if len(all_tours[v]) > 0:
            i = random.randint(0, len(all_tours[v]) - 1)
            item = all_tours[v].pop(i)
            t = random.randint(0, len(all_tours) - 1)
            while t == v:
                t = random.randint(0, len(all_tours) - 1)
            all_tours[t].append(item)
            k -= 1
    return all_tours

def seq_vnd(tours, lmax):
    def two_opt(tour):
        best = tour
        improved = True
        while improved:
            improved = False
            for i in range(1, len(tour) - 2):
                for j in range(i + 2, len(tour)):
                    if j - i == 1: continue  # Do not swap with consecutive nodes
                    new_tour = tour[:]
                    new_tour[i:j] = tour[j-1:i-1:-1]
                    if calc_tour_cost(new_tour) < calc_tour_cost(best):
                        best = new_tour
                        improved = True
        return best
    
    for i in range(len(tours)):
        tours[i] = two_opt(tours[i])
    return tours

def gvns(m, lmax, kmax, tmax):
    x = initialize_solution(m)
    start_time = time.time()
    while time.time() - start_time < tmax:
        k = 1
        while k < kmax:
            x_prime = shake(x, k)
            x_double_prime = seq_vnd(x_prime, lmax)
            if max(calc_tour_cost(t) for t in x_double_prime) < max(calc_tour_cost(t) for t in x):
                x = x_double_prime
                k = 1
            else:
                k += 1
    return x

# Parameters
num_robots = 2
duration_seconds = 5  # Time limit approximately for the GVNS to execute

tours = gvns(num_robots, 5, 10, duration_seconds)
tour_costs = [calc_tour_cost(t) for t in tours]
max_cost = max(tour_costs)

# Output results
for idx, tour in enumerate(tours):
    full_tour = [0] + tour + [0]
    print(f"Robot {idx} Tour: {full_tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_costs[idx]}")

print(f"Maximum Travel Cost: {max_cost}")