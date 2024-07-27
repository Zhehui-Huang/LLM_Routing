from pulp import *
import math

# Define the coordinates of the cities including the depot
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

n = len(coordinates)

# Calculate Euclidean distance between pairs of cities
def distance(c1, c2):
    return math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)

# Creating a list of distances
distances = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
prob = LpProblem("Minimax_TSP", LpMinimize)

# Variables: x_ij is 1 if travel is from city i to city j.
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# t for order in the cities to prevent subtours
t = LpVariable.dicts("t", range(n), lowBound=1, upBound=n, cat=LpInteger)

# Maximizing objective variable
MaxDistance = LpVariable("MaxDistance", lowBound=0)

# Objective Function
prob += MaxDistance

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city only once

for j in range(n):
    prob += lpSum(x[i, j] for i in range(n) if i != j) == 1  # enter each city only once

# Updating the objective function to minimize maximum distance
for i in range(n):
    for j in range(n):
        if i != j:
            prob += MaxDistance >= distances[i][j] * x[i, j]

# Sub-tour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += t[i] - t[j] + (n-1) * x[i,j] <= n-2

# Solve the problem
status = prob.solve(PULP_CBC_CMD(msg=0))

# Extract the solution
tour = []
current = 0
for _ in range(n):
    tour.append(current)
    next_city = [j for j in range(n) if value(x[current, j]) == 1][0]
    current = next_city

tour.append(0)  # Go back to the starting city

# Calculate total cost and max distance between consecutive cities
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")