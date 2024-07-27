from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# Coordinates of the depot and cities
coords = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# City groups
city_groups = {
    0: [1, 4],
    1: [2, 6],
    2: [7],
    3: [5],
    4: [9],
    5: [8],
    6: [3]
}

# Determine all vertices considering each group has exactly one representer
k = len(city_groups)
nodes = [0] + [group[i] for group, i in zip(city_groups.values(), [0]*k)]

# Calculate distances
def euclidean_distance(c1, c2):
    return math.sqrt((coords[c1][0] - coords[c2][0])**2 + (coords[c1][1] - coords[c2][1])**2)

dist = {(i, j): euclideannothing_distance(i, j) for i in nodes for j in nodes if i != j}

# Setup the problem
prob = LpProblem("TSP_Variant", LpMinimize)

# Variables x_ij: i to j is part of the route
x = LpVariable.dicts("x", [(i, j) for i in nodes for j in nodes if i != j], 0, 1, LpBinary)

# Objective Function
prob += lpSum(x[(i, j)] * dist[(i, j)] for i in nodes for j in nodes if i != j)

# Constraints
# Entry and exit for each city exactly once
for j in nodes:
    prob += lpSum(x[(i, j)] for i in nodes if i != j) == 1, f"enter_{j}"
    prob += lpSum(x[(j, i)] for i in nodes if i != j) == 1, f"exit_{j}"

# Subtour elimination
u = LpVariable.dicts("u", nodes, 0, len(nodes) - 1, cat='Continuous')
for i in nodes:
    for j in nodes:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + k * x[(i, j)] <= k - 1

# Solve the problem
prob.solve()

# Extract tour
tour = []
current = 0
while True:
    tour.append(current)
    next_nodes = [j for j in nodes if x[(current, j)].varValue == 1]
    if next_nodes:
        current = next_nodes[0]
    if current == 0:
        break

# Compute total travel cost
total_cost = sum(dist[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

# Output tour and total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)