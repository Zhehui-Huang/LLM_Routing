import math
from itertools import combinations

# Using Gurobi Python Interface
from gurobipy import Model, GRB, quicksum

# Coordinates of the cities, including depot city at index 0
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Total number of cities including the depot
n = len(coordinates)

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Model setup
model = Model("Minimax TSP")

# Add variables: x[i,j] = 1 if the route goes directly from i to j
x = model.addVars(n, n, vtype=GRB.BINARY, name="x")

# Add variable for the maximum distance
max_dist = model.addVar(vtype=GRB.CONTINUOUS, name="max_distance")

# Objective: minimize the maximum distance used in any part of the tour
model.setObjective(max_dist, GRB.MINIMIZE)

# Add constraints
# 1. Exactly one outgoing from each node
model.addConstrs((x.sum(i, '*') == 1 for i in range(n)), name="outgoing")

# 2. Exactly one incoming to each node
model.addConstrs((x.sum('*', i) == 1 for i in range(n)), name="incoming")

# 3. Minimize the maximum distance
model.addConstrs((x[i, j] * distance_matrix[i][j] <= max_dist for i in range(n) for j in range(n) if i != j),
                 name="max_edge")

# 4. Subtour Elimination
u = model.addVars(n, vtype=GRV.CONTINUOUS, lb=0, name='u')
model.addConstrs((u[i] - u[j] + n * x[i, j] <= n - 1 for i in range(n) for j in range(n) if i != j and i > 0 and j > 0),
                 name="subtourElimination")

# Solve the model
model.optimize()

# Output the solution
if model.status == GRB.OPTIMAL:
    solution = model.getAttr('x', x)
    tour = []
    for h in range(n):
        for i, j in solution:
            if solution[i, j] > 0.9:
                if i == h:
                    tour.append(j)
                    h = j
                    break
    tour = [0] + tour
    total_travel_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(n))
    max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(n))
    
    print("Tour:", tour)
    print("Total travel cost:", total_travel_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No optimal solution found")