import math
import numpy as np
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates including the depot
cities = [
    (29, 51), # Depot City 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

n = len(cities)

# Calculate distance matrix
distances = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1, n):
        distances[i][j] = distances[j][i] = euclidean_distance(cities[i], cities[j])

# Define the problem
prob = LpProblem("TSP", LpMinimize)

# Create variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=LpBinary)
z = LpVariable("z", lowBound=0)

# Objective function
prob += z

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination
from itertools import combinations
for S in combinations(range(1, n), 2):
    prob += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Max distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j]*distances[i][j] <= z

# Solve the problem
prob.solve()

# Retrieve the solution
tour = []
current_city = 0
while True:
    tour.append(current_city)
    next_cities = [j for j in range(n) if j != current_city and x[current_city, j].varValue == 1]
    if not next_cities:
        break
    current_city = next_cities[0]

tour.append(0)  # Ending at the depot

# Calculate distances
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")