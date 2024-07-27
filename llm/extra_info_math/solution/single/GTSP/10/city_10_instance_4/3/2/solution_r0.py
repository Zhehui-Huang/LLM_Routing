from pulp import *
import math

# Cities and their coordinates
coordinates = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Groups of cities (1-based to 0-based indexing)
groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]

# Number of clusters including the depot
k = len(groups) + 1  # Add depot cluster

# Generating all possible combinations between cities
V = sum(groups, [0])  # flatten list and add depot (0)
A = [(i, j) for i in V for j in V if i != j]

# Calculating the Euclidean distance between cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

c = {(i, j): distance(coordinates[i], coordinates[j]) for i, j in A}

# Create the problem variable to minimize cost
prob = LpProblem("RobotTour", LpMinimize)

# Decision variables: x_ij is 1 if the path between i and j is chosen
x = LpVariable.dicts('x', A, cat='Binary')

# Objective Function
prob += lpSum(c[i, j] * x[i, j] for i, j in A), "Total Travel Cost"

# A list to store cluster variables
cluster_vars = []
for p in range(k):
    cluster_vars.append([c for c in V if c in groups[p-1]] if p != 0 else [0])

# Cluster entrance and exit constraints
for p in range(1, k):
    prob += lpSum(x[i, j] for i in cluster_vars[p] for j in V if j not in cluster_vars[p]) == 1, f"Cluster_{p}_exit"
    prob += lpSum(x[j, i] for i in cluster_vars[p] for j in V if j not in cluster_vars[p]) == 1, f"Cluster_{p}_entry"

# Flow conservation constraints
for i in V:
    prob += lpSum(x[j, i] for j in V if (j, i) in A) == lpSum(x[i, j] for j in V if (i, j) in A), f"Flow_{i}"

# Subtour elimination constraints
u = LpVariable.dicts('u', V[1:], lowBound=0, cat='Continuous')  # Subtour vars, ignoring depot
for i in V[1:]:
    for j in V[1:]:
        if i != j and (i, j) in A:
            prob += u[i] - u[j] + (k-1) * x[i, j] <= k-2, f"SubtourElimination_{i}_{j}"

# Solving the problem
prob.solve()
tour = []
cost = value(prob.objective)

if LpStatus[prob.status] == 'Optimal':
    current = 0
    tour.append(current)
    while True:
        next_cities = [j for j in V if j != current and value(x[current, j]) == 1]
        if not next_cities:
            break
        current = next_cities[0]
        tour.append(current)
        if current == 0:
            break

print("Tour:", tour)
print("Total travel cost:", cost)