import pulp
import math
from itertools import combinations

# Coordinates of the cities
coordinates = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]
num_cities = len(coordinates)

# Calculating distance between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

cost_matrix = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            cost_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Setting up the PuLP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities)), cat='Binary', lowBound=0, upBound=1)

# Objective function
prob += pulp.lpSum(cost_matrix[i, j] * x[i][j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
for i in range(num_cities):
    prob += pulp.lpSum(x[i][j] for j in range(num_cities) if i != j) == 1  # Leaving each city 
    prob += pulp.lpSum(x[j][i] for j in range(num_cities) if i != j) == 1  # Entering each city

# Subtour elimination
for s in range(2, num_cities):
    for S in combinations(range(num_cities), s):
        prob += pulp.lpSum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# Solving the problem
solution_status = prob.solve()

# Collect results
tour = []
total_cost = 0
if pulp.LpStatus[solution_status] == 'Optimal':
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[i][j]) == 1:
                total_cost += cost_matrix[i, j]
                tour.append(i)

# Ensuring the tour is not broken and forced to cycle back to starting point
tour.append(tour[0])  # Add the start city to the end to complete the tour

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")