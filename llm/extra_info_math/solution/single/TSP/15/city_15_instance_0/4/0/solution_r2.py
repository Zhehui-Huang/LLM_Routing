import pulp
from math import sqrt, inf

# Define city coordinates
city_coords = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Compute distance function
def euclidean_distance(ci, cj):
    return sqrt((city_coords[ci][0] - city_coords[cj][0])**2 + (city_coords[ci][1] - city_coords[cj][1])**2)

# Generate cost matrix
n = len(city_coords)
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[(i, j)] = euclidean_distance(i, j)
        else:
            cost_matrix[(i, j)] = inf  # Large number to sidestep self loops

# Define problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')

# Objective
prob += pulp.lpSum(x[(i, j)] * cost_matrix[(i, j)] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # leave each city once
    prob += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # enter each city once

# Add subtour elimination constraints
for k in range(2, n):
    for S in combinations(range(1, n), k):
        prob += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Retrieve the results
tour = []
current_city = 0
for _ in range(n):
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if next_cities:
        next_city = next_cities[0]
        tour.append(next_city)
        current_city = next_path

# Ensure to end tour at the depot
tour.append(0)

# Calculate total cost
total_cost = sum(cost_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", [0] + tour)
print("Total travel cost:", total_cost)