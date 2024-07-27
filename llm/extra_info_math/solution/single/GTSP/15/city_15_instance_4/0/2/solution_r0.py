import numpy as np
from scipy.spatial.distance import euclidean
from itertools import product
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# City coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Grouping of cities
groups = {
    0: [3, 8],
    1: [4, 13],
    2: [1, 2],
    3: [6, 14],
    4: [5, 9],
    5: [7, 12],
    6: [10, 11]
}

# Calculate distances between each pair of cities
def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = {}
    for i in cities:
        for j in cities:
            if i != j:
                dist_matrix[(i, j)] = euclidean(cities[i], cities[j])
    return dist_matrix

dist_matrix = calculate_distance_matrix(cities)

# Function to solve the TSP
def solve_tsp(groups, dist_matrix):
    # Initialize the model
    model = LpProblem("GroupBasedTSP", LpMinimize)
    
    # All distinct cities including depot
    V = set(cities.keys())
    
    # Create decision variables x_ij
    x = LpVariable.dicts("x",
                         [(i, j) for i in V for j in V if i != j],
                         cat=LpBinary)

    # Objective function
    model += lpSum([dist_matrix[(i, j)] * x[(i, j)] for i, j in x]), "Total_Travel_Cost"

    # Constraint Set 2 and 3: Exactly one outgoing and incoming connection from each group
    for group in groups.values():
        model += lpSum([x[(i, j)] for i in group for j in V - set(group)]) == 1
        model += lpSum([x[(j, i)] for i in group for j in V - set(group)]) == 1

    # Constraint Set 4: Flow conservation
    for k in V:
        model += lpSum([x[(i, k)] for i in V if i != k]) == lpSum([x[(k, j)] for j in V if j != k])

    # Solve the model
    model.solve()
    
    # Extract the tour and total cost
    tour = []
    for i in V:
        for j in V:
            if i != j and x[(i, j)].varValue == 1:
                tour.append((i, j))

    ordered_tour = []
    current_city = 0
    # Construct the actual tour
    while len(ordered_tour) < len(tour):
        for t in tour:
            if t[0] == current_city:
                ordered_tour.append(current_city)
                current_city = t[1]
                break
    ordered_tour.append(0)  # Complete the tour by returning to the depot

    total_cost = sum(dist_matrix[(ordered_tour[i], ordered_tour[i + 1])] for i in range(len(ordered_tour) - 1))

    return ordered_tour, total_cost

# Solve the TSP with groups and display the results
tour, total_cost = solve_tsp(groups, dist_matrix)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")