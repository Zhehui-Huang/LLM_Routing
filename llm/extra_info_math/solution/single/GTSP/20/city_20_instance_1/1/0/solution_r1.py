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
    [3, 9, 12, 14]       # Group 3
]

# Constants
n = len(coordinates)
grp_cnt = len(groups)
group_indices = [0] + [i for group in groups for i in group]  # flattened groups with depot at start

# Calculate cost matrix
cost = [[euclidean_CFdistance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Prepare variables for possible nodes
# Only these nodes are needed for the problem since the robot visits exactly one city from each group
nodes = [0] + [min(group, key=lambda x: coordinates[x]) for group in groups]

# Integer Programming Model
model = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in nodes for j in nodes if i != j), cat='Binary')

# Objective
model += pulp.lpSum(cost[i][j] * x[i, j] for i in nodes for j in nodes if i != j), "Total_Cost"

# Flow conservation constraints for each node
for i in nodes:
    model += pulp.lpSum(x[i, j] for j in nodes if i != j) == 1, f"Outflow_{i}"
    model += pulp.lpSum(x[j, i] for j in nodes if i != j) == 1, f"Inflow_{i}"

# Subtour constraint: no subtour should include the starting node (depot)
subtour_vars = pulp.LpVariable.dicts("u", (i for i in nodes if i != 0), lowBound=0, upBound=len(nodes)-1, cat='Continuous')

for i in nodes:
    for j in nodes:
        if i != j and i != 0 and j != 0:
            model += subtour_vars[i] - subtour_vars[j] + len(nodes) * x[i, j] <= len(nodes) - 1

# Solve the model
model.solve()

# Tour extraction
tour = [0]
current = 0
for _ in range(len(nodes) - 1):
    next = next(j for j in nodes if j != current and pulp.value(x[current, j]) == 1)
    tour.append(next)
    current = next
tour.append(0)

# Calculate travel cost
total_travel_cost = sum(cost[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)