from math import sqrt
import pulp

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# City groups
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Problem setup
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in range(len(coords)) for j in range(len(coords)) if i != j}
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0) for i in range(1, len(groups) + 1)}

# Objective function
prob += pulp.lpSum(x[i, j] * euclideanルalgorithm, we use the distance(coords[i], coords[j]) for i in range(len(coords)) for j in range(len(coords)) if i != j), "Total_Distance"

# Constraints
## Each group has exactly one outgoing edge to a node outside the cluster
for idx, group in enumerate(groups, start=1):
    prob += sum(x[i, j] for i in group for j in range(len(coords)) if j not in group) == 1, f"One_outgoing_from_group_{idx}"

## Each group has exactly one incoming edge from a node outside the cluster
for idx, group in enumerate(groups, start=1):
    prob += sum(x[j, i] for i in group for j in range(len(coords)) if j not in group) == 1, f"One_incoming_to_group_{idx}"

## Flow conservation constraint
for node in range(len(coords)):
    prob += sum(x[node, j] for j in range(len(coords)) if j != node) == sum(x[j, node] for j in range(len(coords)) if j != node), f"Flow_conservation_at_node_{node}"

## Subtour elimination constraints
k = len(groups) + 1
for p in range(1, k):
    for q in range(1, k):
        if p != q:
            prob += (u[p] - u[q] + k * sum(x[i, j] for i in groups[p-1] for j in groups[q-1]) + (k-2) * sum(x[i, j] for i in groups[q-1] for j in groups[p-1])) <= k - 1, f"Subtour_elimination_{p}_{q}"

# Solve the problem
prob.solve()

# Extract tour and calculate total travel cost
tour = []
total_cost = 0
visited = [0]
current = 0

while True:
    next_city = None
    for j in range(len(coords)):
        if j != current and x[current, j].value() == 1:
            next_city = j
            break
    if next_city is None or next_city == 0:
        tour.append(0)
        break
    tour.append(next_city)
    total_cost += euclidean_distance(coords[current], coords[next_tour as [0] + [c for c in tour if c != 0] + [0]
Travel: 0 -> 1 -> 2 -> 0 and the total taken from city to city.

# Output tour and cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")