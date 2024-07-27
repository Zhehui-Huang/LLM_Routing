import pulp as pl
import math

# Given city coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of cities
n = len(cities)

# Computing the cost matrix
costs = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Setting up the Min-Max problem
model = pl.LpProblem("Minimize_Maximum_Distance_in_Tour", pl.LpMinimize)

# Binary variables indicating travel between cities
x = pl.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Continuous variable for the maximum distance
max_dist = pl.LpVariable("Max_Distance", lowBound=0)

# Objective function
model += max_dist

# Constraints
for i in range(n):
    model += pl.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave each city only once
    model += pl.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter each city only once

for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * costs[i][j] <= max_dist

# Subtour Elimination Constraints
subsets = range(2, n)
from itertools import combinations
for r in subsets:
    for subset in combinations(range(1, n), r):
        model += pl.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the model
status = model.solve()

# Parse and print the results
if pl.LpStatus[status] == 'Optimal':
    print("Optimal solution found!")
    tour = []
    current_city = 0
    visited = set()
    total_cost = 0
    max_dist_result = pl.value(max_dist)

    while True:
        tour.append(current_city)
        visited.add(current_city)
        next_cities = [j for j in range(n) if pl.value(x[current_city, j]) > 0.5 and j not in visited]
        if not next_cities:
            break
        next_city = next_cities[0]
        total_cost += costs[current_city][next_city]
        current_city = next_city

    # complete the tour back to the depot
    tour.append(0)
    total_cost += costs[current_city][0]

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist_result}")
else:
    print("No optimal solution.")