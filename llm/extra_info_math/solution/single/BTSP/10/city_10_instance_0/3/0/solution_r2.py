import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary

# coordinates of the cities including the depot city as city 0
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

n = len(coordinates)  # number of cities

# Function to calculate the Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Creating the problem
problem = LpProblem("Minimax_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = LpVariable.dicts("u", (i for i in range(n)), lowBound=0, cat='Continuous')
d_max = LpVariable("d_max", lowBound=0, cat='Continuous')

# Objective: minimize the maximum distance between any two consecutive cities
problem += d_max

# Constraints
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if i != j) == 1  # Each city is left exactly once
    problem += lpSum(x[j, i] for j in range(n) if i != j) == 1  # Each city is entered exactly once

for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distance(i, j) <= d_max  # Max distance constraint

# Subtour elimination (Miller-Tucker-Zemlin constraints, slightly modified to include 0th city)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i, j] <= n - 1

# Solving the problem
problem.solve()

# Extracting the tour and calculating distances
tour = []
keys = [var for var in x if x[var].varValue == 1]

current_city = 0
tour.append(current_city)
next_city = [key for key in keys if key[0] == 0][0][1]
while next_city != 0:
    tour.append(next_city)
    current_city = next_city
    next_city = [key for key in keys if key[0] == current_city][0][1]

tour.append(0)  # complete the tour by returning to the depot

total_distance = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
max_distance = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)