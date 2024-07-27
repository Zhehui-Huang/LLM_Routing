import math
import pulp

# Coordinates of cities
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# City groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
    [2, 4, 14], [10, 17], [7, 15]
]

# Calculate distances
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

num_cities = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Flat list of nodes from the groups
group_nodes = set(node for group in groups for node in group)
all_nodes = [0] + list(group_nodes)

# Create LP problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in all_nodes for j in all_nodes if i != j), cat='Binary')

# Objective
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in all_nodes for j in all_nodes if i != j), "Total_Distance"

# Constraints
# Enter and exit each group exactly once
for group in groups:
    prob += pulp.lpSum(x[0, j] for j in group) == 1, f"enter_group_{group}"
    prob += pulp.lpSum(x[j, 0] for j in group) == 1, f"exit_group_{group}"

# Flow conservation
for k in group_nodes:
    prob += pulp.lpSum(x[i, k] for i in all_nodes if i != k) == pulp.lpSum(x[k, j] for j in all_nodes if j != k), f"flow_conservation_{k}"

# Solve problem
prob.solve()

# Result extraction
tour = []
visited = {i: False for i in all_nodes}
current = 0
while True:
    tour.append(current)
    visited[current] = True
    next_cities = [j for j in all_nodes if x[current, j].varValue == 1 and not visited[j]]
    if not next_cycles:
        break
    current = next_cities[0]

# Closing the tour
tour.append(0)

# Calculate the total travel cost
total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
print("Tour:", tour)
print("Total travel cost:", total_distance)