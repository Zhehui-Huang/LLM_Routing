import numpy as np
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpInteger
from itertools import combinations

# City coordinates
cities = [
    (16, 90),  # Depot city 0
    (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), 
    (35, 73), (42, 64), (64, 30), (70, 95), 
    (29, 64), (32, 79)
]

# Number of cities
n = len(cities)

# Calculate Euclidean distances
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Setting up the problem
model = LpProblem("Minimax_TSP", LpMinimize)

# Variable indicating whether city i is connected to city j
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Variable for the maximum distance in the tour
max_dist = LpVariable("max_dist", lowBound=0, cat='Continuous')

# Objective function: minimize the maximum distance in the tour
model += max_dist

# Constraints:
# Each city has exactly one outgoing connection
for i in range(n):
    model += lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Each city has exactly one incoming connection
for j in range(n):
    model += lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Subtour elimination
for s in range(2, n):
    for subset in combinations(range(1, n), s):  # No need to include depot in subsets
        model += lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Constrain distances according to max_dist
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i][j] * x[(i, j)] <= max_dist

# Solve the problem
model.solve()

# Retrieve the solution
tour = []
current_city = 0
while True:
    tour.append(current_city)
    next_cities = [j for j in range(n) if j != current_city and x[(current_city, j)].varValue == 1]
    if not next_cities:
        break
    current_city = next_cities[0]

# Close the tour
tour.append(0)

# Calculate total cost and maximum distance
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the tour
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")