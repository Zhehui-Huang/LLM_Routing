import numpy as np
import math

# Constants and Inputs
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_robots = 8
robot_capacity = 35

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculating cost matrix
num_cities = len(coordinates)
cost_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        cost_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Initialization - Compute savings
savings = {}
for i in range(1, num_cities):
    for j in range(i+1, num_cities):
        if i != j:
            save = cost_matrix[0, i] + cost_matrix[0, j] - cost_matrix[i, j]
            savings[(i, j)] = save

sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)

# Begin with the Clarke-Wright Savings Algorithm
tours = [[] for _ in range(num_robots)]
load = [0] * num_robots
in_tour = {i: None for i in range(1, num_cities)}

def can_merge(tour1, tour2):
    if tour1 is not None and tour2 is not None and tour1 != tour2:
        # Check ends of the tours and capacity constraints
        end1 = tours[tour1][-1]
        start2 = tours[tour2][0]
        end2 = tours[tour2][-1]
        start1 = tours[tour1][0] if len(tours[tour1]) > 1 else None
        if (end1 == start2 or end2 == start1) and (load[tour1] + load[tour2] <= robot_capacity):
            return True
    return False

def merge_tours(tour1, tour2):
    if tours[tour1][-1] == tours[tour2][0]:
        load[tour1] += load[tour2]
        tours[tour1].extend(tours[tour2][1:])
        tours[tour2] = []
    elif tours[tour2][-1] == tours[tour1][0]:
        load[tour2] += load[tour1]
        tours[tour2].extend(tours[tour1][1:])
        tours[tour1] = []

robot = 0
for pair, saving in sorted_savings:
    if in_tour[pair[0]] is None and in_tour[pair[1]] is None:
        if load[robot] + demands[pair[0]] + demands[pair[1]] <= robot_capacity:
            tours[robot] = [0, pair[0], pair[1], 0]
            load[robot] = demands[pair[0]] + demands[pair[1]]
            in_tour[pair[0]] = robot
            in_tour[pair[1]] = robot
            robot = (robot + 1) % num_robots
    elif in_tour[pair[0]] is None and in_tour[pair[1]] is not None:
        if load[in_tour[pair[1]]] + demands[pair[0]] <= robot_capacity:
            if tours[in_tour[pair[1]]][1] == pair[1]:  # front of tour
                tours[in_tour[pair[1]]].insert(1, pair[0])
            else:  # end of tour
                tours[in_tour[pair[1]]].insert(-1, pair[0])
            load[in_tour[pair[1]]] += demands[pair[0]]
            in_tour[pair[0]] = in_tour[pair[1]]
    elif in_tour[pair[1]] is None and in_tour[pair[0]] is not None:
        if load[in_tour[pair[0]]] + demands[pair[1]] <= robot_capacity:
            if tours[in_tour[pair[0]]][1] == pair[0]:  # front of tour
                tours[in_tour[pair[0]]].insert(1, pair[1])
            else:  # end of tour
                tours[in_tour[pair[0]]].insert(-1, pair[1])
            load[in_tour[pair[0]]] += demands[pair[1]]
            in_tour[pair[1]] = in_tour[pair[0]]
    elif can_merge(in_tour[pair[0]], in_tour[pair[1]]):
        merge_tours(in_tour[pair[0]], in_tour[pair[1]])

# Clean up and print output
total_cost = 0
for i, tour in enumerate(tours):
    if tour:
        robot_tour_cost = sum(cost_matrix[tour[j]][tour[j+1]] for j in range(len(tour)-1))
        total_cost += robot_tour_cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {robot_tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")