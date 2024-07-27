import math
from scipy.spatial import distance_matrix
import numpy as np

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def solve_tsp_dynamic_programming(distance_matrix):
    n = len(distance_matrix)
    all_sets = range(1 << n)
    dp = [[float('inf')] * n for _ in all_sets]
    parent = [[-1] * n for _ in all_sets]

    for i in range(1, n):
        dp[1 << i][i] = distance_matrix[0][i]

    for subset in all_sets:
        for current in range(1, n):
            if not ((1 << current) & subset):
                continue
            prev = subset & ~(1 << current)
            for last in range(1, n):
                if not ((1 << last) & prev) or last == current:
                    continue
                new_dist = dp[prev][last] + distance_matrix[last][current]
                if new_dist < dp[subset][current]:
                    dp[subset][current] = new_dist
                    parent[subset][current] = last

    min_tour_cost = float('inf')
    last_leg = 0
    for i in range(1, n):
        tour_cost = dp[(1 << n) - 1][i] + distance_matrix[i][0]
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            last_leg = i

    tour = [0]
    subset = (1 << n) - 1
    while last_leg != -1:
        tour.append(last_leg)
        next_leg = parent[subset][last_leg]
        subset ^= (1 << last_leg)
        last_leg = next_leg

    tour.append(0)
    tour.reverse()
    return tour, calculate_total_distance(tour, distance_matrix)

# Coordinates of cities including the depot
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Compute distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Placeholder solution: Partition the cities in a simple way
city_indices = [i for i in range(1, len(coordinates))]

# Split city indices into two roughly equal parts
partition1 = city_indices[:len(city_indices)//2]
partition2 = city_indices[len(city_indices)//2:]

tours = []
total_costs = []
for cities in [partition1, partition2]:
    selected_coords = [coordinates[0]] + [coordinates[c] for c in cities]
    selected_distances = distance_matrix(selected_coords, selected_coords)
    tour, cost = solve_tsp_dynamic_programming(selected_distances)
    adjusted_tour = [0 if x == 0 else cities[x-1] for x in tour]
    tours.append(adjusted_tour)
    total_costs.append(cost)

max_cost = max(total_costs)

# Output results
for i, (tour, cost) in enumerate(zip(tours, total_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print("Maximum Travel Cost:", max_cost)