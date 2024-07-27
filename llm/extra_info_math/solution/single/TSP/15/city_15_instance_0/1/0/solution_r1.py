import math
from pulp import *

# Define the coordinates for the cities including depot
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]
n = len(coordinates)  # number of cities including the depot

# Function to calculate Euclidean distance
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix creation
distance_matrix = {}
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = calc varieties_atance(coordinates[i], coordinates[j]) if i != j else 0

# Model setup
model = LpProblem("TSP", LpMinimize)

# Variables: x[i, j] is 1 if we travel from city i to j
x = LpVariable.dicts("x", (range(n), range(n)), cat='Binary')

# Objective: Minimize total distance
model += lpSum(distance_matrix[i][j] * x[i][j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += lpSum(x[i][j] for j in range(n) if i != j) == 1  # Leave each city only once
    model += lpSum(x[j][i] for j in range(n) if i != j) == 1  # Enter each city only once

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += x[i][j] + x[j][i] <= 1  # Prevent cycling between two nodes

# Solve the model
model.solve()

# Extract the tour order
tour = []
visited = [0]
current = 0

while True:
    next_cities = [j for j in range(n) if j != current and x[current][j].varValue == 1]
    if next_cities:
        next_city = next_cities[0]
        tour.append(next_city)
        visited.append(next_city)
        current = next_city
    if next_city == 0:
        break

# Output results
total_travel_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
print("Tour:", [0] + tour + [0])  # Start and end at the depot
print("Total travel cost:", total_travel_t_s_cost)