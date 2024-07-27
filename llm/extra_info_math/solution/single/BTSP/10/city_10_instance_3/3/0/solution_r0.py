import math
from itertools import combinations
import pulp as pl

# Define the coordinates of the cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
n = len(cities)
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i, j] = euclidean_distance(cities[i], cities[j])

# Define the problem
problem = pl.LpProblem("Minimax_TSP", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pl.LpVariable("z", lowBound=0, cat='Continuous')

# Objective function
problem += z, "Maximum_distance"

# Constraints
for i in range(n):
    problem += pl.lpSum(x[i, j] for j in range(n) if j != i) == 1, f"Outflow_{i}"
    problem += pl.lpSum(x[j, i] for j in range(n) if j != i) == 1, f"Inflow_{i}"

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(1, n), s):  # Exclude the depot from subsets
        problem += pl.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distances[i, j] <= z

# Solve the problem
status = problem.solve()

# Extract solution
tour = []
visited = set()
current = 0
total_cost = 0
max_distance = 0
while len(visited) != n:
    visited.add(current)
    for j in range(n):
        if pl.value(x[current, j]) == 1:
            tour.append(current)
            max_distance = max(max_distance, distances[current, j])
            total_cost += distances[current, j]
            current = j
            break
tour.append(0)  # Return to the depot
total_cost += distances[current, 0]
max_distance = max(max_distance, distances[current, 0])

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")