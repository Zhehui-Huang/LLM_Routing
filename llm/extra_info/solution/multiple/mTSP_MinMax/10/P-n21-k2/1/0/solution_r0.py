import math
from scipy.spatial import distance_matrix
import numpy as np
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def solve_tsp_dynamic_programming(distance_matrix):
    N = len(distance_matrix)
    # memoization table for subset, last visited city
    memo = [[None] * N for _ in range(1 << N)]
    parent = [[None] * N for _ in range(1 << N)]

    # Minimum cost with only start position visited
    for i in range(N):
        if i == 0: continue
        memo[1<<0 | 1<<i][i] = distance_matrix[0][i]

    # Iterating over each subset
    for subset in range(1 << N):
        for next in range(N):
            if not (subset & (1 << next)):
                continue
            
            # Previous subset without 'next' city
            state = subset & ~(1 << next)

            if state == 0:
                continue

            best_prev = float('inf')
            best_prev_node = None
            
            for prev in range(N):
                if prev == next or not (subset & (1 << prev)):
                    continue
                cur_cost = memo[state][prev] + distance_matrix[prev][next]
                if cur_cost < best_prev:
                    best_prev = cur_cost
                    best_prev_node = prev

            memo[subset][next] = best_prev
            parent[subset][next] = best_prev_source

    # Final tour and cost calculation
    full_set = (1 << N) - 1
    last_leg = min((memo[full_set][i] + distance_matrix[i][0] for i in range(1, N)), default=None)
    index = np.argmin([memo[full_set][i] + distance_matrix[i][0] for i in range(1, N)])

    # Backtracking to retrieve path
    tour = []
    while True:
        tour.append(index)
        next_subset = full_set & ~(1 << index)
        next_index = parent[full_set][index]
        if next_index is None: break
        full_set = next_subset
        index = next_index
    tour.append(0)

    return tour[::-1], calculate_total_distance(tour[::-1], distance_matrix)

# City coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Pairwise distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Currently not implementing multi-robot TSP splitting and optimizing
# Placeholder approach: Divide cities in half
cities_per_robot = [list(range(1, 11)), list(range(11, 21))]

tours = []
total_costs = []

for cities in cities_per_robot:
    relevant_coords = [coordinates[0]] + [coordinates[c] for c in cities]
    relevant_distances = distance_matrix(relevant_coords, relevant_coords)
    tour, cost = solve_tsp_dynamic_programming(relevant_distances)
    adjusted_tour = [0 if x == 0 else cities[x-1] for x in tour]
    tours.append(adjusted_tour)
    total_costs.append(cost)

max_cost = max(total_costs)

# Print output
for i, (tour, cost) in enumerate(zip(tours, total_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print("Maximum Travel Taxi Cost:", max_cost)