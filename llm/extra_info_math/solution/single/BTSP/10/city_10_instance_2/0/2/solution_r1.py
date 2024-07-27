import itertools
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

# Create the optimization model
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j),
                          cat='Binary')
d_max = pulp.LpVariable("d_max", lowBound=0, cat='Continuous')

# Objective Function
model += d_max

# Subject to the constraints
# Every city must be left and entered exactly once
for k in cities:
    model += pulp.lpSum(x[(i, j)] for i, j in distance_matrix if i == k) == 1  # leave each city
    model += pulp.lpSum(x[(i, j)] for i, j in distance_matrix if j == k) == 1  # enter each city

# Subtour elimination: Add subtour constraints using Miller-Tucker-Zemlin formulation (MTZ)
u = pulp.LpVariable.dicts("u", cities, lowBound=0, upBound=len(cities)-1, cat='Integer')
for i, j in distance_matrix:
    if i != 0 and j != 0:
        model += u[i] - u[j] + (n - 1) * x[(i, j)] <= n - 2

# Link the variable d_max to the decision variables of the network distances
for i, j in distance_matrix:
    model += d_max >= x[i, j] * distance_matrix[i, j]

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Formulate the tour
tour = []
active_arcs = [(i, j) for (i, j) in x if pulp.value(x[i, j]) == 1]
current_city = 0
visited = set([0])

while len(visited) < n:
    next_city = [j for (i, j) in active_arcs if i == current_city and j not in visited]
    if next_city:
        next_city = next_city[0]
        tour.append((current_city, next_city))
        visited.add(next_city)
        current_city = next_city

tour.append((current_city, 0))  # Returning to the initial city

# Calculate travel cost and maximum distance
total_travel_cost = sum(distance_matrix[i, j] for i, j in tour)
max_travel_distance = max(distance_matrix[i, j] for i, j in tour)

# Output
print("Tour:", [t[0] for t in tour] + [tour[-1][1]])
print("Total travel cost:", total_travel_peak)
print("Maximum distance between consecutive cities:", max_travel_peak)