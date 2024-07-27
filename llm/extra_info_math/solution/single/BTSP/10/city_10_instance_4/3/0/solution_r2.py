import numpy as a
import cvxpy as cp
import itertools
from math import sqrt

def calculate_distances(coords):
    n = len(coords)
    dists = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dists[i][j] = sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
    return dists

coordinates = [
    [79, 15],  # Depot city 0
    [79, 55],
    [4, 80],
    [65, 26],
    [92, 9],
    [83, 61],
    [22, 21],
    [97, 70],
    [20, 99],
    [66, 62]
]

n = len(coordinates)
distances = calculate_distances(coordinates)

x = cp.Variable((n, n), boolean=True)
z = cp.Variable()

constraints = []

for i in range(n):
    constraints.append(cp.sum(x[i, :]) == 1)
    constraints.append(cp.sum(x[:, i]) == 1)

for size in range(2, n):
    for subset in itertools.combinations(range(1, n), size):
        rows = [row for row in subset]
        cols = [col for col in subset]
        constraints.append(cp.sum(x[rows, :][:, cols]) <= len(subset) - 1)

constraints += [x[i, j] * distances[i][j] <= z for i in range(n) for j in range(n) if i != j]

objective = cp.Minimize(z)
problem = cp.Problem(objective, constraints)
problem.solve(solver=cp.GLPK_MI)

tour = []
current_city = 0
for _ in range(n):
    tour.append(current_city)
    next_city = [j for j in range(n) if round(x[current_city, j].value) == 1][0]
    current_city = next_city

tour.append(0)  # Return to the depot

total_travel_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance_between_cities = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", z.value)