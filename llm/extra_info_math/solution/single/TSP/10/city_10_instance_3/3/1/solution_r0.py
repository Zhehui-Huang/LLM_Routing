import math
from pulp import *

# Coordinates of each city including depot (city 0)
coordinates = [
    (84, 67), (74, 40), (71, 13), (74, 82), 
    (97, 28), (0, 31), (8, 62), (74, 56), 
    (85, 71), (6, 76)
]

n = len(coordinates)  # Number of cities

# Helper function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Cost matrix (distance between each pair of cities)
cost = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Define LP problem
prob = LpProblem("TSP", LpMinimize)

# Variables: x_ij is 1 if the tour goes from city i to city j, otherwise 0
x = LpVariable.dicts("x", (range(n), range(n)), cat='Binary')

# Objective function: Minimize the total travel cost
prob += lpSum([cost[i, j] * x[i][j] for i in range(n) for j in range(n)])

# Constraints: 
# Each city is left and entered exactly once
for i in range(n):
    prob += lpSum([x[i][j] for j in range(n) if i != j]) == 1  # Leave city i once
    prob += lpSum([x[j][i] for j in range(n) if i != j]) == 1  # Enter city i once

# Subtour elimination using Miller-Tucker-Zemlin (MTZ) approach
u = LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1) * x[i][j] <= n-2

# Solve the problem
prob.solve()

# Extract tour from problem solution
tour = [0]
while len(tour) < n:
    for j in range(n):
        if x[tour[-1]][j].value() == 1:
            tour.append(j)
            break

tour.append(0)  # Returning to the depot

# Calculate the total travel cost
total_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)