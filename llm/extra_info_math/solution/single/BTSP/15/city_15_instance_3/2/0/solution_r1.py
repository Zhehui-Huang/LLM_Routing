import pulp
import math
from itertools import combinations

# Define coordinates of cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a model
model = pulp.LpProblem("Minimax_Regret_TSP", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(cat=pulp.LpBinary, name=f"x_{i}_{j}") for i in cities for j in cities if i != j}

# Objective: Minimize the maximum travel distance between consecutive cities
z = pulp.LpVariable("z")
model += z

for i in cities:
    for j in cities:
        if i != j:
            model += x[i, j] * euclidean_distance(cities[i], cities[j]) <= z

# Constraints
# Each city must be entered and left exactly once
for i in cities:
    model += pulp.lpSum(x[i, j] for j in cities if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in cities if i != j) == 1

# Subtour elimination: use the Miller-Tucker-Zemlin formulation
u = {i: pulp.LpVariable(cat=pulp.LpContinuous, lowBound=0) for i in cities}
n = len(cities)
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the model
model.solve()

# Retrieve the tour from the decision variables
tour = []
current_city = 0
while True:
    next_city = next(j for j in cities if j != current_city and pulp.value(x[current_city, j]))
    tour.append(next_city)
    if next_city == 0:
        break
    current_city = next_city

# Calculate the tour cost and maximum distance
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")