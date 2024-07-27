import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# City coordinates
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Groups: 0-indexed, grouped as 1-indexed data
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], 
    [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Calculate Euclidean distance
def distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Create variables
n = len(coordinates)
all_cities = range(n)

# Create the decision variables
x = LpVariable.dicts('x', ((i, j) for i in all_cities for j in all_cities if i != j), cat=LpBinary)

# Initialize the model
model = LpProblem("Minimize_Distance", LpMinimize)

# Objective Function
model += lpSum(distance(i, j) * x[i, j] for i in all_cities for j in all_cities if i != j)

# Each group must have exactly one outgoing/incoming connection to the rest of the network
for group in groups:
    model += lpSum(x[i, j] for i in group for j in all_cities if j not in group) == 1
    model += lpSum(x[j, i] for i in group for j in all_cities if j not in group) == 1

# Ensure each city (except depot) has one incoming and one outgoing edge
for k in all_cities:
    model += lpSum(x[j, k] for j in all_cities if j != k) == lpSum(x[k, j] for j in all_cities if j != k)

# Solve the problem
status = model.solve()

# Extract the results
tour = []
visited = [0]  # Start at depot
while len(visited) < len(groups) + 1:
    for j in all_cities:
        if x[visited[-1], j].varValue > 0.99 and j not in visited:
            visited.append(j)
            break
tour = visited + [0]  # return to depot

# Calculate the total distance of the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)