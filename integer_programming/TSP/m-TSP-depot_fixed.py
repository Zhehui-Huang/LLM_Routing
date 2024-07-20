import gurobipy as gp
from gurobipy import GRB
import numpy as np
import matplotlib.pyplot as plt

# Sample data
n = 15 # Total number of nodes
d = 3   # Number of depots
m = 4   # Total number of salesmen
K = 2   # Minimum number of nodes a salesman must visit
L = np.ceil(n/m)+1   # Maximum number of nodes a salesman can visit
m_k = [1, 1, 2]  # Number of salesmen at each depot

# Generate random node locations
#np.random.seed(42)
node_locations = np.random.rand(n, 2) * 100  # Random locations in a 100x100 area

# Calculate the cost matrix as the Euclidean distance between nodes
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

c = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        c[i, j] = euclidean_distance(node_locations[i], node_locations[j])

# Create a new model
model = gp.Model("multiple_depot_mtsp_fixed_destination")

# Variables
x = model.addVars(n, n, d, vtype=GRB.BINARY, name="x")
u = model.addVars(n, vtype=GRB.INTEGER, name="u")

# Objective function: minimize the total cost
model.setObjective(gp.quicksum(c[i][j] * x[i, j, k] for k in range(d) for i in range(n) for j in range(n)), GRB.MINIMIZE)

# Constraints
# 1. Salesmen departure from each depot
for k in range(d):
    model.addConstr(gp.quicksum(x[k, j, k] for j in range(d, n)) == m_k[k])

# 2. Each customer node is visited exactly once
for j in range(d, n):
    model.addConstr(gp.quicksum(x[k, j, k] for k in range(d)) + gp.quicksum(x[i, j, k] for i in range(d, n) if i!=j for k in range(d)) == 1)

# 3. Route continuity for customer nodes
for k in range(d):
    for j in range(d, n):
        model.addConstr(x[k, j, k] + gp.quicksum(x[i, j, k] for i in range(d, n)) - x[j, k, k] - gp.quicksum(x[j, i, k] for i in range(d, n)) == 0)

# 4. Route continuity for depot nodes
for k in range(d):
    model.addConstr(gp.quicksum(x[k, j, k] for j in range(d, n)) - gp.quicksum(x[j, k, k] for j in range(d, n)) == 0)

# 5. Bounding constraints
for i in range(d, n):
    model.addConstr(u[i] + (L - 2) * gp.quicksum(x[k, i, k] for k in range(d)) - gp.quicksum(x[i, k, k] for k in range(d)) <= L - 1)
    model.addConstr(u[i] + gp.quicksum(x[k, i, k] for k in range(d)) + (2 - K) * gp.quicksum(x[i, k, k] for k in range(d)) >= 2)

# 6. Single customer visit restriction
for i in range(d, n):
    model.addConstr(gp.quicksum(x[k, i, k] for k in range(d)) + gp.quicksum(x[i, k, k] for k in range(d)) <= 1)

# 7. Subtour elimination constraints
for i in range(d, n):
    for j in range(d, n):
        if i != j:
            model.addConstr(u[i] - u[j] + L * gp.quicksum(x[i, j, k] for k in range(d)) + (L - 2) * gp.quicksum(x[j, i, k] for k in range(d)) <= L - 1)

# Optimize model
model.optimize()

# Extract solution
if model.status == GRB.OPTIMAL:
    solution = model.getAttr('x', x)
    routes = {k: [] for k in range(d)}
    for k in range(d):
        for i in range(n):
            for j in range(n):
                if solution[i, j, k] > 0.5:
                    routes[k].append((i, j))

    # Visualization
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    plt.figure(figsize=(10, 10))
    for i in range(n):
        if i < d:
            plt.plot(node_locations[i][0], node_locations[i][1], 's', markersize=10, label=f'Depot {i}')
        else:
            plt.plot(node_locations[i][0], node_locations[i][1], 'o', markersize=5, label=f'Customer {i}')

    for k in range(d):
        for (i, j) in routes[k]:
            plt.plot([node_locations[i][0], node_locations[j][0]], [node_locations[i][1], node_locations[j][1]], colors[k % len(colors)], label=f'Route {k}' if i == k else "")

    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.title('Multiple Depot m-TSP with Fixed Destination')
    plt.legend()
    plt.show()

else:
    print("No optimal solution found.")
