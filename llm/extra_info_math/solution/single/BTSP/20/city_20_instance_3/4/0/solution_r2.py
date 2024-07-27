import math
import pulp

# Coordinates of the cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Problem setup
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
max_dist = pulp.LpVariable("max_dist", lowBound=0, cat='Continuous')

# Objective function: minimize the maximum distance between consecutive cities
problem += max_dist

# Constraints
for i in cities:
    problem += sum(x[(i, j)] for j in cities if j != i) == 1  # Leave each city only once
    problem += sum(x[(j, i)] for j in cities if j != i) == 1  # Enter each city only once

# Constraint linking max_dist to the distances
for i in cities:
    for j in cities:
        if i != j:
            problem += distances[(i, j)] * x[(i, j)] <= max_dist

# Subtour elimination constraints (Miller-Tucker-Zemlin formulation)
u = pulp.LpVariable.dicts("u", [i for i in cities], lowBound=0, upBound=len(cities)-1, cat='Integer')
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            problem += u[i] - u[j] + len(cities) * x[(i, j)] <= len(cities) - 1

# Solve the problem
problem.solve()

# Extract the tour and calculate metrics
tour = [0]
total_cost = 0
max_distance = 0

for _ in range(len(cities) - 1):
    last = tour[-1]
    next_city = next(j for j in cities if j != last and x[(last, j)].value() == 1)
    tour.append(next_city)
    total_cost += distances[(last, next_city)]
    max_distance = max(max_distance, distances[(last, next_city)])

tour.append(0)  # Complete the tour back to the depot city 0
total_cost += distances[(tour[-2], 0)]
max_distance = max(max_distance, distances[(tour[-2], 0)])

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")