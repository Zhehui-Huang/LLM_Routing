import gurobipy as gp
from gurobipy import GRB
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the data
#np.random.seed(42)  # For reproducibility

V = [i for i in range(1, 15)]  # List of all nodes (including depots and customer nodes)
d = 3   # Number of depots
D = list(range(1, d+1))#[1, 2, 3]  # List of depots
V_prime = list(range(d+1, len(V)+1))#[4, 5, 6, 7, 8, 9]  # List of customer nodes
m_i = {1: 2, 2: 2, 3: 2}  # Dictionary with number of salesmen starting at each depot
positions = {i: (np.random.rand() * 10, np.random.rand() * 10) for i in V}  # Random positions for nodes

# Calculate the Euclidean distance as the cost between nodes
c = {(i, j): np.linalg.norm(np.array(positions[i]) - np.array(positions[j])) for i in V for j in V if i != j}


n = len(V_prime) + len(D)  # Total number of nodes
m = sum(m_i.values())  # Total number of salesmen
K = 2  # Minimum number of nodes a salesman must visit
L = np.ceil(n/m)+1  # Maximum number of nodes a salesman may visit


# Create a new model
model = gp.Model("Nonfixed_Destination_MmTSP")

# Create variables
x = model.addVars(V, V, vtype=GRB.BINARY, name="x")
u = model.addVars(V_prime, vtype=GRB.INTEGER, name="u")

# Set objective
model.setObjective(gp.quicksum(c[i, j] * x[i, j] for i in V for j in V if (i, j) in c), GRB.MINIMIZE)

# Add constraints

# Ensure exactly m_i salesmen leave each depot i in D
for i in D:
    model.addConstr(gp.quicksum(x[i, j] for j in V_prime) == m_i[i])

# Ensure exactly m_i salesmen return to each depot i in D
for i in D:
    model.addConstr(gp.quicksum(x[j, i] for j in V_prime) == m_i[i])

# Ensure each customer node is visited exactly once
for j in V_prime:
    model.addConstr(gp.quicksum(x[i, j] for i in V if i!=j) == 1)
    model.addConstr(gp.quicksum(x[j, i] for i in V if i!=j) == 1)

# Bound constraints to ensure proper tour lengths and initialize u_i
for i in V_prime:
    model.addConstr(u[i] + (L - 2) * gp.quicksum(x[k, i] for k in D) - gp.quicksum(x[i, k] for k in D) <= L - 1)
    model.addConstr(u[i] + gp.quicksum(x[k, i] for k in D) + (2 - K) * gp.quicksum(x[i, k] for k in D) >= 2)

# Prohibit a salesman from serving only a single customer
for i in V_prime:
    for k in D:
        model.addConstr(x[k, i] + x[i, k] <= 1)

# Subtour elimination constraints
for i in V_prime:
    for j in V_prime:
        if i != j:
            model.addConstr(u[i] - u[j] + L * x[i, j] + (L - 2) * x[j, i] <= L - 1)

# Optimize the model
model.optimize()

# Print the solution and visualize routes
if model.status == GRB.OPTIMAL:
    solution = model.getAttr('x', x)
    
    # Create graph for visualization
    G = nx.DiGraph()
    G.add_nodes_from(V)
    for i in V:
        for j in V:
            if solution[i, j] > 0.5:
                G.add_edge(i, j)

    pos = positions
    labels = {i: i for i in V}
    
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): f"{c[i, j]:.2f}" for i, j in G.edges()}, font_size=8)
    plt.title('Optimal Routes for Nonfixed Destination MmTSP')
    plt.show()
else:
    print("No optimal solution found")
