import numpy as np
from scipy.spatial.distance import euclidean
from pulp import *

# City coordinates as provided
cities = {0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
          5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
          10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)}

n = len(cities)

# Distance matrix
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')

# Define the model
model = LpProblem("Min_Max_TSP", LpMinimize)
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
U = LpVariable("U", lowBound=0)

# Objective function
model += U

# Constraints
for i in cities:
    model += lpSum(x[(i, j)] for j in cities if i != j) == 1
    model += lpSum(x[(j, i)] for j in cities if i != j) == 1

# Subtour constraints
for i in cities:
    for j in cities:
        if i != j:
            model += U >= distance_matrix[i][j] * x[(i, j)]
            for k in cities:
                if i != k and j != k:
                    model += x[(i, j)] + x[(j, k)] + x[(k, i)] <= 2

# Solve model
model.solve()

# Get the tour
tour = []
current_city = 0
tour.append(current_city)
while True:
    next_city = next(j for j in cities if j != current_city and x[current_city, j].value() == 1)
    tour.append(next_city)
    if next_city == 0:
        break
    current_city = next Cities

max_distance = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
total_distance = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)