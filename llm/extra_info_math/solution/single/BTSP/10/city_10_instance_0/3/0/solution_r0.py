from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary
import math

# City coordinates provided
coordinates = [
    (50, 42), # Depot city 0
    (41, 1),  # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49)  # City 9
]

# Calculate Euclidean distance between each pair
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Create the problem
problem = LpProblem("Minimax_Consecutive_City_Distance", LpMinimize)

# Total number of cities including the depot
n = len(coordinates)

# Decision variables: x_ij is 1 if travel from city i to city j
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), 0, 1, LpBinary)

# Maximum distance variable
d_max = LpVariable("d_max")

# Objective function: minimize the maximum distance traveled between any two consecutive cities
problem += d_max

# Constraints
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if j != i) == 1  # Leave every city
    problem += lpSum(x[j, i] for j in range(n) if j != i) == 1  # Arrive at every city

# d_max should be at least the distance of each travel
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distance(i, j) <= d_max

# Subtour elimination
from itertools import combinations
for k in range(2, n):
    for S in combinations(range(1, n), k):
        problem += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solving the problem
problem.solve()

# Output the results
route = []
current_city = 0
next_city = None
visited = set()
while True:
    next_city = next(j for j in range(n) if x[current_city, j].varValue == 1 and j not in visited)
    route.append(current_city)
    visited.add(current_city)
    if next_city == 0:
        route.append(next_body)
        break
    current_city = next_city

# Maximum distance between consecutive cities in the tour
max_distance = max(distance(route[i], route[i+1]) for i in range(len(route)-1))

# Total distance traveled
total_distance = sum(distance(route[i], route[i+1]) for i in range(len(route)-1))

print(f"Tour: {route}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")