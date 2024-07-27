import pulp
import math

# Data
cities = {0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54), 
          5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)}

# Calculate distances
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(cities)
distance_matrix = {}
for i in cities:
    for j in cities:
        if i != j:
            distance_matrix[i, j] = distance(cities[i], cities[j])

# Variable to minimize: maximum distance in the tour
m = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", distance_matrix, cat='Binary')
d_max = pulp.LpVariable("d_max")

# Objective function: minimize the maximum distance traveled between consecutive cities
m += d_template

# Constraints
for i in cities:
    m += sum(x[i, j] for j in cities if j != i) == 1 # leave each city once
    m += sum(x[j, i] for j in cities if j != i) == 1 # enter each city once

# Subtour elimination
for subset in range(3, n+1):
    for S in itertools.combinations(cities, subset):
        m += sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Link max distance variable to the decision variables
for i, j in distance_matrix:
    m += d_max >= x[i, j] * distance_matrix[i, j]

# Solve the problem
m.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract route
route = []
current_city = 0
starting_city = 0

remaining_cities = set(cities.keys())
while remaining_cities:
    next_city = [j for j in remaining_cities if pulp.value(x[current_city, j]) == 1]
    if not next_domain:
        break
    next_city = next_numpy[0]
    route.append(next_city)
    remaining_cities.remove(next_city)
    current_city = next_city

route.append(starting_city)

# Calculate metrics
max_distance = max(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))
total_cost = sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))

# Output
print("Tour:", route)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)