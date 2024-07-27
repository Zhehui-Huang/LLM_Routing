import pulp
import math

# Define cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define groups of cities
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Calculate Euclidean distances between each pair of cities
def euclidean(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

distances = {(i, j): euclidean(i, j) for i in cities for j in cities if i != j}

# Optimization Problem Setup
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables: x_ij is 1 if travel is from city i to city j
x = pulp.LpVariable.dicts("x", distances, 0, 1, pulp.LpBinary)

# Objective Function: Minimize the total distance traveled
prob += pulp.lpSum([distances[i, j] * x[i, j] for i, j in distances]), "Minimize_Total_Distance"

# Constraints:
# 1. Exactly one edge leaving from each group
for i, group in enumerate(groups):
    prob += pulp.lpSum(x[g, j] for g in group for j in set(cities) - set(group)) == 1, f'Outgoing_from_group_{i}'
    
# 2. Exactly one edge entering each group
for i, group in enumerate(groups):
    prob += pulp.lpSum(x[j, g] for g in group for j in set(cities) - set(group)) == 1, f'Incoming_to_group_{i}'

# Flow conservation at each city
for city in cities:
    prob += pulp.lpSum(x[i, city] for i in cities if i != city) \
           == pulp.lpSum(x[city, j] for j in cities if j != city), f"Flow_conservation_at_city_{city}"

# Solve the problem
prob.solve(pulp.PUL
P_CBC_CMD(msg=False))

# Extract the tour
path = []
for k in range(len(cities)):
    for i, j in x:
        if pulp.value(x[i, j]) == 1:
            if (not path) or (path and path[-1] == i):
                path.append(j)

# Ensure we start and end at the depot
if path and path[0] != 0:
    # create the list of nodes to visit starting at the depot
    depot_idx = path.index(0)
    path = path[depot_idx:] + path[:depot_idx]

# Add depot as the end point
path.append(0)

# Calculate the total cost of the tour
total_travel_cost = sum(distances[path[i], path[i+1]] for i in range(len(path)-1))

print(f"Tour: {path}")
print(f"Total travel cost: {total_travel_ cost}")