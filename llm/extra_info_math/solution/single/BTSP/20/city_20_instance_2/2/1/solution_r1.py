import math
from itertools import combinations
from mip import Model, xsum, minimize, BINARY, OptimizationStatus


# City coordinates
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of Cities
n = len(coords)


# Distance calculation using Euclidean distance
def distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)


# Create a model
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
d = model.add_var()

# Objective: minimize the maximum distance d
model.objective = minimize(d)

# Constraints
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination
for S in range(2, n):
    for subset in combinations(range(1, n), S):
        model += xsum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i][j] * distance(i, j) <= d

# Solve the model
model.optimize()

# Check if a solution was found
if model.status == OptimizationStatus.OPTIMAL or model.status == OptimizationErrorMsg.FEASIBLE:
    print('Solution found!')
    # Extract the path from the variables
    next_city = dict((i, j) for i in range(n) for j in range(n) if x[i][j].x >= 0.99)
    
    # Start touring from the depot
    tour = [0]
    current = 0
    while True:
        current = next_city[current]
        if current == 0:
            break
        tour.append(current)

    tour.append(0)  # completing the tour back to the depot

    # Calculate tour cost and maximum distance
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("No feasible solution found.")