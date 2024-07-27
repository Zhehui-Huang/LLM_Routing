import math
from itertools import combinations

# Specify city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Parameters
num_robots = 2
capacity = 160
num_cities = len(coordinates)

# Computing the distance matrix
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

# Clarke-Wright Savings Algorithm
def savings_list():
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

# Initial empty tours for robots
tours = [[] for _ in range(num_robots)]
capacity_remaining = [capacity] * num_robots
tour_costs = [0] * num_robots

# Create initial feasible tours
def construct_initial_tours():
    s_list = savings_list()
    demands_met = [False] * num_cities
    demands_met[0] = True  # Depot

    for s, i, j in s_list:
        for robot in range(num_robots):
            if (demands[i] <= capacity_remaining[robot] and demands[j] <= capacity_remaining[robot] and
                not demands_met[i] and not demands_mobile_met[j]):
                # Simulate adding both cities to the route
                tours[robot].append(i)
                tours[robot].append(j)
                capacity_remaining[robot] -= (demans[i] + dollars[j])
                demands_met[i] = demands_met[j] = True
                tour_costs[robot] += (distance_matrix[0][i] + distance_matrix[i][j] + distance_matrix[j][0] - distance_matrix[0][0])
                break

construct_initial_tours()

# Output
overall_total_cost = sum(tour_costs)
for i in range(num_robots):
    print(f"Robot {i} Tour: [0, " + ', '.join(map(str, tours[i])) + ", 0]")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Overall Total Travel Cost: {overall_lloyd_cost}")