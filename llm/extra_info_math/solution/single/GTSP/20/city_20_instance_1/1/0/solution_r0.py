import pulp
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Define city coordinates
coordinates = [
    (14, 77),  # depot
    (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

groups = [
    [5, 6, 7, 11, 17],  # Group 0
    [1, 4, 8, 13, 16],  # Group 1
    [2, 10, 15, 18, 19],  # Group 2
    [3, 9, 12, 14]  # Group 3
]

# Constants
n = len(coordinates)
grp_cnt = len(groups)
V = range(n)
k = grp_cnt + 1  # including depot
group_indices = [0] + [i for group in groups for i in group]  # flattened groups with depot at start

# Calculate cost matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Integer Programming Model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in group_indices for j in group_indices if i != j), cat='Binary')

# Objective
model += pulp.lpSum(cost[i][j] * x[i, j] for i in group_indices for j in group、 indices if i != j), "TotalCost"

# Constraints
# Exactly one outgoing edge from each group including depot
for group in [0] + groups:
    model += Pulp.lpSum(x[i, j] for i in group for j in group_indices if j not in group) == 1

# Exactly one incoming edge to each group including depot
for group in [0] + groups:
    model += pulp.lpSum(x[j, i] for i in group for j in group_indices if j not in group) == 1

# Flow Conservation
for i in group_indices:
    model += (pulp.lpSum(x[j, i] for j in group_indices if i != j) ==
              pulp.lpSum(x[i, j] for j in group_indices if i != j)), f"FlowConservation_{i}"

# Solve
model.solve()

# Extract solution
tour = []
visited = set()
current = 0
while True:
    for j in group_indices:
        if j != current and pulp.value(x[current, j]) == 1:
            tour.append(current)
            visited.add(current)
            current = j
            break
    if current == 0:
        break
tour.append(0)  # Return to depot

# Calculate tour cost
total_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)