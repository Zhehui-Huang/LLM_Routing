import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary
from pulp import PULP_CBC_CMD

# Define the city coordinates
city_coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

n = len(city_coords)

# Calculate Euclidean distances
def euclidean_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)

distance_matrix = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(n)] for i in range(n)]

# Define the optimization problem
prob = LpProblem("Minimax_TSP", LpMinimize)

# Decision variables: x[(i,j)] is 1 if the route goes from i to j
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=LpDataFrame(data_type[Binary)

# Subtour elimination variables
u = LpVariable.dicts("u", range(n), lowBound=0, cat="Continuous")

# Max distance variable
dmax = LpVariable("dmax", lowBound=0)

# Objective: minimize maximum distance
prob += dmax

# Constraints that ensure every city is entered and left exactly once
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1, f"leave_{i}"
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1, f"enter_{i}"

# Constraint for maximum distance
for i in range(n):
    for j in range(n):
        if i != j:
            prob += dmax >= x[(i, j)] * distance_matrix[i][j]

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
otp += u[i] - u[j] + (n-1) * x[(i, j)] <= n-2

# Solve the problem
prob.solve(PULP_CBC_CMD(msg=0))

# Extract the solution
tour = [0]
for _ in range(n):
    next_cities = [j for j in range(n) if j not in tour and value(x[(tour[-1], j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)

# Include the return to the starting point
tour.append(0)

# Calculate the total and maximum distance
total_distance = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")