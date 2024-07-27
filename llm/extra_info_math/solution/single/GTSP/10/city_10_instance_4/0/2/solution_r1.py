import itertools
from math import sqrt
import pulp

# City coordinates
coordinates = [
    (79, 15),  # City 0: Depot
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Groupings of city indices (excluding the depot)
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Calculate Euclidean distance between two cities
def distance(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Compute nodes and groups
nodes = list(range(10))
groups_with_depot = [[0]] + groups  # Include depot in groups
cluster_count = len(groups_with_depot)

# Variables
prob = pulp.LpProblem("VRP_with_Groups", pulp.LpMinimize)

# x_ij whether i->j is used in the tour
x = pulp.LpVariable.dicts("x", ((i, j) for i in nodes for j in nodes if i != j),
                          lowBound=0, upBound=1, cat=pulp.LpBinary)

# Sub-tour constraint variables
u = pulp.LpVariable.dicts("u", (i for i in nodes if i != 0), lowBound=0, upBound=cluster_count-1, cat=pulp.LpInteger)

# Objective Function
prob += pulp.lpSum(distance(i, j) * x[(i, j)] for i in nodes for j in nodes if i != j)

# Constraints
# Outgoing from each group and return to depot exactly once
for g in groups_with_depot:
    prob += pulp.lpSum(x[(i, j)] for i in g for j in nodes if j not in g) == 1

# Incoming to each group from depot exactly once
for g in groups_with_depot:
    prob += pulp.lpSum(x[(j, i)] for i in g for j in nodes if j not in g) == 1

# Subtour elimination (MTZ constraints - Miller-Tucker-Zemlin)
for i in nodes:
    for j in nodes:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + cluster_count * x[(i, j)] + (cluster_count-2) * x[(j, i)] <= cluster*>(cluster_count-1)

# Solve
prob.solve()

# Extract the tour and calculate its total cost
tour = []
current_city = 0
visited = [0] * len(nodes)
total_cost = 0

while True:
    visited[current_city] = 1
    for next_city in nodes:
        if next_city != current_city and pulp.value(x[(current_city, next_city)]) == 1:
            tour.append(next_city)
            total_cost += distance(current_city, next_city)
            current_city = next_city
            break
    if current_city == 0:
        break

# Include the starting city at the start and end of the tour for clarity
tour = [0] + tour + [0]

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")