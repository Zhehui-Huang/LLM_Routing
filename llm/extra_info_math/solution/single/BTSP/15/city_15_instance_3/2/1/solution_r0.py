import pulp
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of cities including the depot
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

n = len(cities)  # Number of cities including the depot

# Calculate distances between each pair of cities
distances = {(i, j): calculate_distance(cities[i], cities[j]) for i in range(n) for j in range(n)}

# Setting up the optimization problem
problem = pulp.LpProblem("MinimaxTSP", pulp.LpMinimize)

# Decision variables: x[i,j] is 1 if the path goes from city i to city j
x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat=pulp.LpBinary)

# Auxiliary variable for the maximum distance in the tour
max_distance = pulp.LpVariable("max_distance", lowBound=0)

# Objective: minimize the maximum distance
problem += max_distance

# Constraints
for i in range(n):
    problem += (pulp.lpSum(x[i][j] for j in range(n) if j != i) == 1)  # leave each city only once
    problem += (pulp.lpSum(x[j][i] for j in range(n) if j != i) == 1)  # enter each city only once

# For sub-tour elimination
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i][j] * distances[i, j] <= max_distance

# Subtour elimination constraints
for length in range(2, n):
    for subset in itertools.combinations(range(n), length):
        problem += pulp.lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
problem.solve()

# Calculate the tour and the total travel cost
tour = []
current = 0
visited = set([0])
total_cost = 0
max_seg_distance = 0

for _ in range(n):
    next_city = next(j for j in range(n) if pulp.value(x[current][j]) == 1)
    tour.append(next_city)
    segment_cost = distances[current, next_city]
    total_cost += segment_cost
    if segment_cost > max_seg:
        max_seg_distance = segment_cost
    visited.add(next_city)
    current = next_city

tour.append(0)  # returning to the depot
total_cost += distances[current, 0]

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_seg_distance)