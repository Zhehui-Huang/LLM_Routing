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

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a 2-D list of distances
dist = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the integer programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij (1 if travel from i to j, 0 otherwise)
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)),
                          cat='Binary', lowBound=0, upBound=1)

# Objective: Minimize the maximum distance
Z = pulp.LpVariable('Z', lowBound=0, cat='Continuous')
model += Z

# Subject to
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave i once
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter i once

# Maximum constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * dist[i][j] <= Z

# Subtour elimination
for S in range(3, n+1):
    for subset in itertools.combinations(range(1, n), S):
        model += sum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the model
model.solve()

# Extract the solution
tour = [0]
current = 0
visited = set([0])
while True:
    for j in range(n):
        if pulp.value(x[current, j]) == 1 and j not in visited:
            tour.append(j)
            visited.add(j)
            current = j
            break
    if current == 0:
        break

# Calculate total travel cost and max distance
total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(dist[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)