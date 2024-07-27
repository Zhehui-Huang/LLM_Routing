import pulp as pl
import math
from itertools import product

# Define city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Parameters
n_cities = len(coordinates)
capacity = 35
robots = 8

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i, j in product(range(n_cities), repeat=2)}

# Setup the problem
problem = pl.LpProblem("CVRP", pl.LpMinimize)

# Decision variables
x = pl.LpVariable.dicts("x", [(r, i, j) for r in range(robots) for i in range(n_cities) for j in range(n_cities) if i != j], 0, 1, pl.LpBinary)

# Objective function
problem += pl.lpSum(distances[i, j] * x[r, i, j] for r in range(robots) for i in range(n_cities) for j in range(n_cities) if i != j)

# Constraints
for j in range(1, n_cities):
    problem += pl.lpSum(x[r, i, j] for r in range(robots) for i in range(n_cities) if i != j) == 1

for r in range(robots):
    problem += pl.lpSum(x[r, 0, j] for j in range(1, n_cities)) == 1
    problem += pl.lpSum(x[r, j, 0] for j in range(1, n_cities)) == 1

    # Load constraint per robot
    problem += pl.lpSum(demands[j] * x[r, i, j] for i in range(n_cities) for j in range(1, n_cities) if i != j) <= capacity

    # Flow conservation
    for j in range(1, n_cities):
        problem += pl.lpSum(x[r, i, j] for i in range(n_cities) if i != j) == pl.lpSum(x[r, j, k] for k in range(n_cities) if j != k)

# Subtour elimination is complex for large n, can use callback or other heuristics

# Solve the problem
problem.solve()

# Output results
total_cost = 0
for r in range(robots):
    tour = [0]
    current = next((j for j in range(1, n_cities) if pl.value(x[r, 0, j]) == 1), None)
    cost = 0
    while current is not None and current != 0:
        next_city = next((j for j in range(n_cities) if j != current and pl.value(x[r, current, j]) == 1), None)
        tour.append(current)
        cost += distances[current, next_city]
        current = next_city
    tour.append(0)
    cost += distances[tour[-2], 0]
    print(f"Robot {r} Tour: {tour}")
    print(f"Robot {r} Total Travel Cost: {round(cost, 2)}")
    total_cost += cost
    
print(f"Overall Total Travel Cost: {round(total_cost, 2)}")