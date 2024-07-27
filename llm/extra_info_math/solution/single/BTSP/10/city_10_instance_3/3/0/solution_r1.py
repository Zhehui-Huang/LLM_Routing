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

# Distance matrix and initialization of cities count
n = len(cities)
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i, j] = euclidean_distance(cities[i], cities[j])

# Define the problem
problem = pl.LpProblem("Minimax_TSP", pl.LpMinimize)

# Decision variables
x = pl.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pl.LpVariable("z", lowBound=0, cat='Continuous')

# Objective function
problem += z, "Maximum_distance"

# Degree constraints
for i in range(n):
    problem += pl.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Outflow_{i}"
    problem += pl.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Inflow_{i}"

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(n), s):
        problem += pl.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1, f"no_subtour_{S}"

# Link the maximum distance to z
for i, j in distances:
    problem += x[i, j] * distances[i, j] <= z

# Solve
problem.solve()

# Extract solution
tour = []
used_edges = [(i, j) for i in range(n) for j in range(n) if i != j and pl.value(x[i, j]) == 1]
current_city = 0
remaining_cities = set(range(n))

while remaining_cities:
    next_cities = [j for i, j in used_edges if i == current_city]
    if next_cities:
        next_city = next_cities[0]
    tour.append(current_city)
    remaining_cities.remove(current_city)
    current_city = next_city

tour.append(tour[0])  # returning to the depot

# Calculate tour details
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")