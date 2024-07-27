import numpy as np
from math import sqrt
from collections import defaultdict

# Coordinates and demand
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23,
    11, 19, 15, 28, 8,
    8, 7, 14, 6, 19,
    11, 12, 26, 17, 6,
    15, 5, 10
]

robot_capacity = 40
num_robots = 8

# Compute distances
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Initial greedy solution based on closest neighbor and demand without exceeding capacity
def greedy_solution():
    tours = []
    load = [0] * num_robots
    used = [False] * len(coordinates)
    used[0] = True  # depot is always used

    for r in range(num_robots):
        tour = [0]  # start at the depot
        current_load = 0
        last_city = 0

        while True:
            best_city = None
            min_dist = float('inf')
            for i in range(1, len(coordinates)):
                if not used[i] and current_load + demands[i] <= robot_capacity:
                    if distances[last_city][i] < min_dist:
                        min_dist = distances[last_city][i]
                        best_city = i

            if best_city is None:
                break

            tour.append(best_city)
            used[best_city] = True
            current_load += demands[best_city]
            last_city = best_city

        tour.append(0)  # return to depot
        tours.append(tour)
        load[r] = current load

        if all(used):
            break

    return tours, load

tours, loads = greedy_solution()

# Calculate travel cost for a single tour
def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output solution
total_cost = 0
for robot_id, tour in enumerate(tours):
    cost = calculate_tour_cost(tour)
    total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robotid} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")