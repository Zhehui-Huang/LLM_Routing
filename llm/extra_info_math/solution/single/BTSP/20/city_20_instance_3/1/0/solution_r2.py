import pulp
import math

# Coordinates of cities
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Total number of cities (including the depot)
n = len(coordinates)

# Calculating distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Solving the problem utilizing MILP (Mixed Integer Linear Programming)
# Declare the model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Continuous variable representing the max distance in the solution
max_distance = pulp.LpVariable("max_distance")

# Objective function
model += max_distance

# Constraints
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # leave each city only once
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # enter each city only once

# Distance constraints related to the objective of minimizing the longest leg distance
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i][j] * x[(i, j)] <= max_distance

# Subtour elimination constraints
subtours = []
for size in range(2, n):
    for subset in itertools.combinations(range(n), size):
        subtours.append(subset)
        model += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Retrieve the results
route = []
for i in range(n):
    for j in range(n):
        if pulp.value(x[(i, j)]) == 1:
            route.append((i, j))

# To make the route human-readable and confirm we return to the depot
sorted_route = []
current_location = 0
while len(sorted_route) < n:
    for (i, j) in route:
        if i == current_location:
            sorted_route.append(i)
            current_location = j
            break
sorted_route.append(0)  # return to the depot

# Calculate max edge length and total cost
total_cost = sum(distances[sorted_route[i]][sorted_route[i + 1]] for i in range(len(sorted_route) - 1))
max_edge_length = max(distances[sorted_item[i]][sorted_item[i + 1]] for i in range(len(sorted_route) - 1))

print("Tour:", sorted_route)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", pulp.value(max_distance))