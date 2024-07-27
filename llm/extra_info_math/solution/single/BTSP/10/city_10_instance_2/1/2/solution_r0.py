from pulp import *
import math


# Coordinates of the cities (depot included)
coordinates = [
    (90, 3),  # depot city 0
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Compute Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Create distance matrix
n = len(coordinates)
dist_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
prob = LpProblem("Minimax_TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = LpVariable("z", lowBound=0, cat='Continuous')  # Maximum distance variable

# Objective
prob += z, "Maximize_Minimum_Distance"

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Sum_out_{i}"
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Sum_in_{i}"

# Constrain z to be at least the distance of any route taken
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * dist_matrix[i][j] <= z, f"Max_dist_{i}_{j}"

# Subtour elimination constraints
for s in range(3, n+1):
    for S in itertools.combinations(range(1, n), s):
        prob += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve(PULP_CBC_CMD(msg=0))

# Extract tour
tour = [0]
for _ in range(n-1):
    i = tour[-1]
    for j in range(n):
        if i != j and x[i, j].varValue > 0.5:
            tour.append(j)
            break
tour.append(0)  # Return to depot

# Calculate total cost and max distance
total_distance = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.4f}")
print(f"Maximum distance between consecutive cities: {max_distance:.4f}")