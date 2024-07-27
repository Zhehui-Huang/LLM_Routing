import numpy as np
from scipy.spatial.distance import euclidean
from pulp import *

# City coordinates as provided
cities = {0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
          5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
          10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)}

n = len(cities)

# Calculate distances between each pair of cities
def dist(i, j):
    return euclidean(cities[i], cities[j])

# Create the LP problem
model = LpProblem("Min-Max Distance TSP", LpMinimize)

# Create decision variables x_ij and a variable for the longest distance U
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')
U = LpVariable("Max_Distance", lowBound=0)

# Objective function is to minimize the longest distance U
model += U

# Exactly one outgoing edge from each city
for i in range(n):
    model += lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Exactly one incoming edge to each city
for j in range(n):
    model += lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Subtour elimination constraint using Miller-Tucker-Zemlin formulation:
u = LpVariable.dicts("u", range(n), lowBound=0, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n - 1) * x[(i, j)] <= n - 2

# Each pair of cities either to or from must not exceed U
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[(i, j)] * dist(i, j) <= U

# Solve the problem
model.solve()

# Determine the tour from the solution
tour = []
if model.status == LpStatusOptimal:
    active_edges = [(i, j) for i in range(n) for j in range(n) if i != j and x[(i, j)].varValue == 1]
    current_city = 0
    while len(active_edges) > 0:
        for edge in active_edges:
            if edge[0] == current_city:
                tour.append(current_city)
                current_city = edge[1]
                active_edges.remove(edge)
                break
    tour.append(0)  # return to the depot

    # Calculate the total distance and maximum distance between consecutive cities
    total_cost = sum(dist(tour[i], tour[(i + 1) % n]) for i in range(len(tour) - 1))
    max_distance = max(dist(tour[i], tour[(i + 1) % n]) for i in range(len(tour) - 1))
    
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("The problem did not solve optimally.")