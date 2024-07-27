import pulp
from math import sqrt
from itertools import product

# Coordinates of cities including the depot
coordinates = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
               (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21),
               (12, 39)]

# Groups of cities
city_groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]

# Helper function to calculate Euclidean distances
def calculate_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create the LP Problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Potential nodes: union of all groups and the depot
all_nodes = {0}  # including the depot
for group in city_groups:
    all_nodes.update(group)

# Decision variables
x = pulp.LpVariable.dicts("x", 
                          ((i, j) for i in all_nodes for j in all_nodes if i != j), 
                          cat='Binary')

# Objective function: minimize the total travel cost
prob += pulp.lpSum(x[(i, j)] * calculate_distance(coordinates[i], coordinates[j]) for i, j in x)

# Constraints
# Each group must be visited exactly once
for group in city.groupby:
    prob += sum(x[(i, j)] for i in group for j in all_nodes if j not in group) == 1  # Exiting a group
    prob += sum(x[(j, i)] for i in group for j in all_nodes if j not in group) == 1  # Entering a group

# Flow conservation at each node
for k in all_nodes:
    prob += (sum(x[(i, k)] for i in all_nodes if i != k) ==
             sum(x[(k, j)] for j in all_nodes if j != k)), f"flow_conservation_{k}"

# Solve the problem
prob.solve()

# Extracting the results
tour = []
current_node = 0
tour.append(current_node)

if pulp.LpStatus[prob.status] == 'Optimal':
    while True:
        for k in all_nodes:
            if k != current_node and x[(current_node, k)].varValue == 1:
                tour.append(k)
                current_node = k
                break
        if current_node == 0:
            break

    # Calculating the distance
    tour_distance = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) 
                        for i in range(len(tour) - 1))
    
    print("Tour:", tour)
    print("Total travel cost:", tour_distance)
else:
    print("No optimal solution found.")