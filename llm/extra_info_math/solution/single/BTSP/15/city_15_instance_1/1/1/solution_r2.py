import math
import numpy as np
from pulp import LpProblem, LpVariable, lpSum, LpMinimize

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
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Define the problem
prob = LpProblem("TSP", LpMinimize)

# Create variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Continuous')

# Objective function
prob += lpSum(distances[i][j] * x[i,j] for i in range(n) for j in range(n) if i != j)

# Constraints
for j in range(1, n):
    prob += lpSum(x[i,j] for i in range(n) if i != j) == 1

for i in range(1, n):
    prob += lpSum(x[i,j] for j in range(n) if i != j) == 1

# Subtour elimination
for i in range(1,n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n - 1) * x[i,j] <= n - 2

# Solve the problem
prob.solve()

# Extract the solution
tour = []
for i in range(n):
    for j in range(n):
        if i != j and x[i,j].varValue > 0.99:
            tour.append((i, j))


# Follow the tour
sorted_tour = []
current_location = 0
while len(sorted_tour) < len(tour):
    for link in tour:
        if link[0] == current_location:
            sorted_tour.append(link[0])
            current_location = link[1]
            break
sorted_tour.append(0)  # return to the depot

# Calculate total cost and max distance
total_cost = sum(distances[sorted_tour[i]][sorted_tour[i+1]] for i in range(len(sorted_tour)-1))
max_distance = max(distances[sorted_tour[i]][sorted_tour[i+1]] for i in range(len(sorted_tour)-1))

output_tour = [city for city in sorted_tour]

print(f"Tour: {output_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")