from itertools import product
import numpy as np
from scipy.spatial.distance import euclidean
from pulp import LpMinimize, LpProblem, LpVariable, lpSum

# Coordinates of the cities, indexed from 0 to 19 with depot at index 0
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Groups of cities (excluding the depot which is assumed to be at index 0 in each group implicitly)
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Adding depot to groups for ease of constraints formulation
complete_groups = [[0] + group for group in groups]

# Calculate distances between each pair of cities
distances = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            distances[(i, j)] = euclidean(cities[i], cities[j])

# Create the problem
prob = LpProblem("Minimize_Tour_Cost", LpMinimize)

# Variables x_ij where i, j are city indices and x_ij = 1 if the tour goes from city i to city j
x = LpVariable.dicts("x", distances, 0, 1, cat='Binary')

# Objective function: minimize the total travel cost
prob += lpSum([distances[(i, j)] * x[(i, j)] for (i, j) in distances]), "Total_Cost_of_Traveling"

# Constraint: Each group must be connected to the rest exactly once
for group in complete_groups:
    prob += lpSum(x[(i, j)] for i in group for j in cities if i != j and j not in group) == 1, f"One_outgoing_edge_from_group_{group}"
    prob += lpSum(x[(j, i)] for i in group for j in cities if i != j and j not in group) == 1, f"One_incoming_edge_to_group_{group}"

# Constraint: Flow conservation at each city
for k in cities:
    prob += lpSum(x[(i, k)] for i in cities if i != k) - lpSum(x[(k, j)] for j in cities if j != k) == 0, f"Flow_conservation_at_city_{k}"

# Solve the problem
prob.solve()

# Extract the tour and calculate the cost
tour = []
visited = {0}
current_city = 0
total_cost = 0

while True:
    next_city = [j for j in cities if j != current_city and x[(current_city, j)].varValue == 1][0]
    tour.append(next_city)
    total_cost += distances[(current_city, next_city)]
    current_city = next_city
    if current_city == 0:
        break
    visited.add(current_city)

# Output the results
print(f"Tour: [{', '.join(map(str, [0] + tour))}]")
print(f"Total travel cost: {total_cost}")