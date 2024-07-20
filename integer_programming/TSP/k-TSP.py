#Two multi‑start heuristics for the k‑traveling salesman problem

import gurobipy as gp
from gurobipy import GRB
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools

# Define the data
n = 10  # Number of nodes (including the home city)
k = 5  # Number of cities to visit (including the home city)
np.random.seed(1)
dist = np.random.rand(n, n)  # Random distance matrix for illustration
np.fill_diagonal(dist, 0)  # No self-loops

# Coordinates for visualization
coords = np.random.rand(n, 2)

# Create a new model
model = gp.Model("k-TSP")

# Create variables
x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
y = model.addVars(n, vtype=GRB.BINARY, name="y")

# Set objective function
model.setObjective(gp.quicksum(dist[i, j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)

# Add constraints
model.addConstr(gp.quicksum(y[i] for i in range(n)) == k, name="visit_k_cities")

# Ensure the tour starts and ends at the home city
model.addConstr(gp.quicksum(x[0, j] for j in range(1, n)) == 1, name="start_at_home")
model.addConstr(gp.quicksum(x[i, 0] for i in range(1, n)) == 1, name="end_at_home")

# Degree constraints
for i in range(1, n):
    model.addConstr(gp.quicksum(x[i, j] for j in range(n) if j != i) == y[i], name=f"out_degree_{i}")
    model.addConstr(gp.quicksum(x[j, i] for j in range(n) if j != i) == y[i], name=f"in_degree_{i}")

# Sub-tour elimination constraints
for subset_size in range(2, k+1):
    for subset in itertools.combinations(range(1, n), subset_size):
        model.addConstr(gp.quicksum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1, name=f"subtour_elim_{subset}")

# Optimize the model
model.optimize()

# Print the solution
if model.status == GRB.OPTIMAL:
    selected_edges = [(i, j) for i in range(n) for j in range(n) if x[i, j].x > 0.5]
    selected_nodes = [i for i in range(n) if y[i].x > 0.5]
    print("Optimal tour:", selected_edges)
    print("Visited nodes:", selected_nodes)

    # Visualization
    G = nx.DiGraph()

    for i in range(n):
        G.add_node(i, pos=coords[i])

    for i, j in selected_edges:
        G.add_edge(i, j)

    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_weight='bold')
    edge_labels = {(i, j): f'{dist[i][j]:.2f}' for i, j in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title('Optimal k-TSP Tour')
    plt.show()
else:
    print("No optimal solution found")
