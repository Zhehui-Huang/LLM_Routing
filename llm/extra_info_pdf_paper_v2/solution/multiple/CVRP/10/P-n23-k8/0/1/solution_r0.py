import math
from itertools import combinations

# Given coordinates and demands
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
demands = {
    0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8,
    10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17,
    19: 6, 20: 15, 21: 5, 22: 10
}

# Number of robots and their capacity
num_robots = 8
robot_capacity = 40

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate the distances matrix
distances = {}
for i, j in combinations(coordinates, 2):
    d = euclidean_distance(coordinates[i], coordinates[j])
    distances[frozenset([i, j])] = d

# Clarke-Wright Savings Algorithm - Initialization
savings = {}
for i in coordinates:
    if i == 0:
        continue
    for j in coordinates:
        if j == 0 or i == j:
            continue
        s = distances[frozenset([0, i])] + distances[frozenset([0, j])] - distances[frozenset([i, j])]
        savings[(i, j)] = s

# Sorting savings in descending order of savings
sorted_savings = sorted(savings.items(), key=lambda x: -x[1])

# Build Routes
routes = []
capacity_remaining = []
for r in range(num_robots):
    routes.append([0])
    capacity_remaining.append(robot_capacity)

# Assign routes according to the max savings and check capacity constraints
for (i, j), s in sorted_savings:
    for r in range(num_robots):
        if j in routes[r] or i in routes[r] or (demands[i] > capacity_remaining[r] and demands[j] > capacity_remaining[r]):
            continue
        if (demands[i] + demands[j] <= capacity_remaining[r]):
            if i not in routes[r] and j not in routes[r]:
                routes[r].append(i)
                routes[r].append(j)
                capacity_remaining[r] -= (demands[i] + demands[j])
                break
            elif i in routes[r] and j not in routes[r]:
                routes[r].append(j)
                capacity_remaining[r] -= demands[j]
                break
            elif j in routes[r] and i not in routes[r]:
                routes[r].append(i)
                capacity_remaining[r] -= demands[i]
                break

# Making sure every route returns to depot city
for r in range(num_robots):
    routes[r].append(0)

# Calculate the total travel cost and per robot travel cost
total_travel_cost = 0
for r in range(num_robots):
    tour_cost = 0
    route = routes[r]
    print(f"Robot {r} Tour: {route}")
    for i in range(len(route) - 1):
        tour_cost += distances[frozenset([route[i], route[i+1]])]
    total_travel_cost += tour_cost
    print(f"Robot {r} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")