import pulp
import math

# City coordinates as given
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of salesmen
num_salesmen = 4

# Number of nodes (cities)
num_nodes = len(coordinates)

# Function to compute Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate distances between all pairs
costs = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(num_nodes) for j in range(num_nodes) if i != j}

# Initialize the problem
model = pulp.LpProblem("VRP_Multiple_Robots", pulp.LpMinimize)

# Variables: x[i, j, k] is 1 if robot k travels from i to j
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_nodes) for j in range(num_nodes) if i != j for k in range(num_salesmen)), cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_nodes)), lowBound=0, cat=pulp.LpContinuous)

# Objective function
model += pulp.lpSum(costs[i, j] * x[i, j, k] for i in range(num_nodes) for j in range(num_nodes) if i != j for k in range(num_salesmen))

# Constraints
# Each city is visited exactly once by exactly one salesman
for j in range(1, num_nodes):
    model += pulp.lpSum(x[i, j, k] for i in range(num_nodes) if i != j for k in range(num_properties)) == 1

# Flow conservation constraints and salesman leaves/returns to depot
for k in range(num_salesmen):
    model += pulp.lpSum(x[0, j, k] for j in range(1, num_nodes)) == 1  # leaves depot
    model += pulp.lpSum(x[i, 0, k] for i in range(1, num_nodes)) == 1  # returns to depot
    for p in range(1, num_nodes):
        model += pulp.lpSum(x[p, j, k] for j in range(num_nodes) if p != j) == pulp.lpSum(x[i, p, k] for i in range(num_nodes) if i != p)  # flow conservation

# Subtour elimination constraints
for i in range(1, num_nodes):
    for j in range(1, num_nodes):
        if i != j:
            for k in range(num_salesmen):
                model += u[i] - u[j] + num_nodes * x[i, j, k] <= num_nodes - 1

# Solve the problem
status = model.solve()

# Output results
if status == pulp.LpStatusOptimal:
    tours = {k: [] for k in range(num_salesmen)}
    costs = {k: 0 for k in range(num_salesmen)}
    for k in range(num_salesmen):
        node = 0
        while True:
            next_nodes = [j for j in range(num_nodes) if j != node and pulp.value(x[node, j, k]) == 1]
            if not next_nodes:
                break
            next_node = next_nodes[0]
            tours[k].append(next_node)
            costs[k] += costs[node, next_node]
            node = next_node
            if node == 0:
                break
    total_cost = sum(costs[k] for k in range(num_salesmen))
    for k in range(num_salesmen):
        print(f"Robot {k} Tour: {[0] + tours[k] + [0]}")
        print(f"Robot {k} Total Travel Cost: {costs[k]}")
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("Solution not found. Status:", pulp.LpStatus[status])