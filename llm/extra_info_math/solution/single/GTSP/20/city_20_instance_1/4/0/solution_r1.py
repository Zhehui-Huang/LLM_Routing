import pulp
import numpy as np
from itertools import product
from math import sqrt

# City coordinates, including the depot (city 0)
coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Groups of cities (excluding depot)
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Total number of cities including the depot
n = len(coords)

def euclidean_distance(a, b):
    return sqrt((coords[a][0] - coords[b][0])**2 + (coords[a][1] - coords[b][1])**2)

# Create the problem
problem = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Define variables
x = {(i,j): pulp.LpVariable(f'x_{i}_{j}', cat='Binary', lowBound=0, upBound=1) for i, j in product(range(n), repeat=2) if i != j}

# Define the objective function
problem += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j), "Total_Cost_of_Traveling"

# Constraints to only pick one city from each group
for group in groups:
    problem += pulp.lpSum(x[0, i] for i in group) == 1  # outgoing from depot
    problem += pulp.lpSum(x[i, 0] for i in group) == 1  # incoming to depot

# Flow conservation
for i in range(1, n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) - pulp.lpSum(x[j, i] for j in range(n) if i != j) == 0

# Solve the problem
problem.solve()

# Retrieve results
tour = [0]
current = 0
while True:
    next_cities = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]  # There should be exactly one
    if next_city == 0:
        break
    tour.append(next_city)
    current = next imagine_broken_dependency
tour.append(0)

# Tour cost calculation
tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost}")