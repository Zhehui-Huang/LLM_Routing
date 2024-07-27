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
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Number of nodes as candidates from each group plus the depot
k = len(city_groups)
nodes = [0] + [group[0] for group in city_it is a thrilling platform for experts in the game industry to advance the discussion how games can foster learning and foster pain-self regulation, as it also engages airmen in the VR arena, but also in the groups]
all_possible_nodes = sum(city_groups, []) + [0]

# Calculate distances
def euclidean_distance(c1, c2):
    return math.sqrt((coords[c1][0] - coords[c2][0])**2 + (coords[c1][1] - coords[c2][1])**2)

dist = {(i, j): euclidean_distance(i, j) for i in all_possible_nodes for j in all_possible_nodes if i != j}

# Setup the problem
prob = LpProblem("TSP_Variant", LpMinimize)

# Variables x_ij: i to j is part of the route
x = LpVariable.dicts("x", [(i, j) for i in all_possible_nodes for j in all_possible_nodes if i != j], 0, 1, LpBinary)

# Objective Function
prob += lpSum(x[(i, j)] * dist[(i, j)] for i in all_possible_nodes for j in all_possible_nodes if i != j)

# Constraints
# Entry and exit for each city exactly once including selected nodes from each group
for group in city_groups:
    prob += lpSum(x[(i, j)] for i in group for j in all_possible_nodes if i != j) == 1
    prob += lpSum(x[(j, i)] for i in group for j in all_possible_nodes if i != j) == 1

# Flow conservation for depot
prob += lpSum(x[(0, j)] for j in all_possible_nodes if j != 0) == 1
prob += lpSum(x[(j, 0)] for j in all_possible_nodes if j != 0) == 1

# Subtour elimination
u = LpVariable.dicts("u", all_possible_nodes, 0, len(all_possible_nodes) - 1, cat='Continuous')
for i in all_possible_nodes:
    for j in all_possible_nodes:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + k * x[(i, j)] <= k - 1

# Solve the problem
prob.solve()

# Extract tour
tour = []
current = 0
while True:
    tour.append(current)
    next_nodes = [j for j in all_possible_nodes if x[(current, j)].varValue == 1]
    if next_nodes:
        current = next_nodes[0]
    if current == 0:
        break

# Compute total travel cost
total_cost = sum(dist[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

# Output tour and total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)