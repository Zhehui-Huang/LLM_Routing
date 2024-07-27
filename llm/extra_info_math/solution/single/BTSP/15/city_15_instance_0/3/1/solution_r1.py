import pulp
import math

# Define the coordinates of the cities
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Number of cities
n = len(cities)

# Calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a 2-D list of distances
dist = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the integer programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij (1 if travel i to j, 0 otherwise)
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective: Minimize the maximum distance
Z = pulp.LpVariable('Z', lowBound=0, cat='Continuous')
model += Z

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1  # Leave i once
    model += pulp.lpSum(x[j, i] for j in range(n) if j != i) == 1  # Enter i once

for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * dist[i][j] <= Z

# Solve the problem
status = model.solve()

# Check if a valid solution has been found
if status == pulp.LpStatusOptimal:
    prev_city = 0
    tour = [0]
    lengths = []

    while len(tour) < n:
        for j in range(n):
            if j != prev_city and pulp.value(x[prev_city, j]) == 1:
                tour.append(j)
                lengths.append(dist[prev_city][j])
                prev_city = j
                break

    # Completing the cycle by returning to the start city
    tour.append(0)
    lengths.append(dist[prev_city][0])

    # Output results
    total_cost = sum(lengths)
    max_distance = max(lengths)

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No optimal solution found!")