import pulp
import math
import itertools

# Define city coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Number of cities including the depot
n = len(cities)

# Calculate Euclidean distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = pulp.LpProblem("MinimaxTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
maximum_distance = pulp.LpVariable("maximum_distance")

# Objective function
problem += maximum_distance

# Constraints
# 1. Each city must be left exactly once and arrived exactly once
for i in range(n):
    problem += (pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1)
    problem += (pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1)

# 2. Subtour elimination
for S in range(2, n):
    subgroups = itertools.combinations(range(1, n), S)
    for subgroup in subgroups:
        problem += (pulp.lpSum(x[i, j] for i in subgroup for j in subgroup if i != j) <= len(subgroup) - 1)
        
# 3. Distance constraints imply maximum_distance
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distances[i][j] <= maximum_distance

# Solve the problem
solver = pulp.PULP_CBC_CMD(msg=False, timeLimit=120)  # Use CBC solver
problem.solve(solver)

# Extract the solution
tour = []
current_city = 0
visited = set([current_city])
while True:
    next_cities = [(j, distances[current_city][j]) for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = min(next_cities, key=lambda item: item[1])[0]
    if next_city in visited:
        break
    tour.append(current_city)
    visited.add(next_city)
    current_city = next_city

# Return to the start city
tour.append(current_city)
tour.append(tour[0])

# Calculate maximum and total travel distances in the tour
max_distance_in_tour = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
total_distance_in_tour = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

output = {
    "Tour": tour,
    "Total travel cost": total_distance_in_tour,
    "Maximum distance between consecutive cities": max_distance_in_tour
}

# Print the output
print(output)