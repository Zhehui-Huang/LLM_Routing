import math
from itertools import permutations

# Description of cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distance
def euclidean_dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Distance matrix
dist_matrix = [[euclidean_dist(i, j) for j in range(len(cities))] for i in range(len(cities))]

# Simple example split for 8 robots
robots = {i: [i] for i in range(8)}

for c in range(8, 23):
    closer_robot = min(robots.keys(), key=lambda r: euclidean_dist(r, c))
    robots[closer_robot].append(c)

# Calculate cost of a tour
def calculate_cost(tour):
    return sum(dist_matrix[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)))

# Add depots and calculate costs
total_cost = 0
for renk, tour in robots.items():
    tour.append(renk)  # Completing the round trip to the starting depot
    tour.insert(0, renk)  # Starting from the respective depot
    tour_cost = calculate_cost(tour)
    total_cost += tour_cost
    print(f"Robot {renk} Tour: {tour}")
    print(f"Robot {renk} Total Travel Cost: {tour_cost}")

print("Overall Total Travel Cost:", total_cost)