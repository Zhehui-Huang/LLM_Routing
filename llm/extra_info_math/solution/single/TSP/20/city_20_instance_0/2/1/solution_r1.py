import pulp
import math
from itertools import combinations

# Coordinates of the cities
coordinates = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]
num_cities = len(coordinates)

# Distance calculator
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
cost_matrix = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            cost_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Setting up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(cost_matrix[i, j] * x[i, j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
for i in range(num_cities):
    prob += pulp.lpSum(x[i, j] for j in range(num_cities) if i != j and (i, j) in x) == 1  # Leave each city once
    prob += pulp.lpSum(x[j, i] for j in range(num_cities) if i != j and (j, i) in x) == 1  # Enter each city once

# Subtour elimination
for s in range(2, num_cities + 1):
    for S in combinations(range(num_cities), s):
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j and (i, j) in x) <= len(S) - 1

# Solving the problem
prob.solve()

# Extracting the solution
tour = [0]
current_city = 0
while True:
    next_city = [j for j in range(num_cities) if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current_city = next_city
    if next_city == 0:  # If back to the depot
        break

total_cost = sum(cost_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")