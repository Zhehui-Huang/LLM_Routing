from gurobipy import Model, GRB, quicksum
import math
from itertools import combinations
import sys

# Coordinates of the cities, including the depot
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

n = len(coordinates)

# Calculate Euclidean distance
def dist(i, j):
    dx = coordinates[i][0] - coordinates[j][0]
    dy = coordinates[i][1] - coordinates[j][1]
    return math.sqrt(dx * dx + dy * dy)

# Create model
m = Model("TSP")

# Add variables
x = m.addVars(n, n, vtype=GRB.BINARY, name="x")
longest = m.addVar(vtype=GRB.CONTINUOUS, name="longest")

# Objective
m.setObjective(longest, GRB.MINIMIZE)

# Constraints
for i in range(n):
    m.addConstr(quicksum(x[i, j] for j in range(n) if j != i) == 1, name=f"out_{i}")
    m.addConstr(quicksum(x[j, i] for j in range(n) if j != i) == 1, name=f"in_{i}")

# Subtour elimination constraints
for size in range(2, n):
    for S in combinations(range(1, n), size):
        m.addConstr(quicksum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1)

# Longest distance constraints
m.addConstrs((x[i, j] * dist(i, j) <= longest for i in range(n) for j in range(n) if i != j), name="max_dist")

# Solve
try:
    m.optimize()
    if m.status == GRB.OPTIMAL:
        # Tour extraction
        tour = []
        next_city = 0
        while len(tour) < n:
            for j in range(n):
                if x[next_city, j].x > 0.99 and j not in tour:
                    tour.append(next_city)
                    next_city = j
                    break
        tour.append(0)  # return to depot

        # Calculate distances for the tour
        total_distance = sum(dist(tour[i], tour[i+1]) for i in range(len(tour)-1))
        max_distance = max(dist(tour[i], tour[i+1]) for i in range(len(tour)-1))

        print(f"Tour: {tour}")
        print(f"Total travel cost: {total_distance}")
        print(f"Maximum distance between consecutive cities: {max_distance}")
    else:
        print("No optimal solution found")
except Exception as e:
    print(f"An error occurred: {str(e)}")