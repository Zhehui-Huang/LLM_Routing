import gurobipy as gp
from gurobipy import GRB
import matplotlib.pyplot as plt
import networkx as nx

# Sample data
nodes = [0, 1, 2, 3]  # 0 is the depot
products = [0, 1]
edges = [(i, j) for i in nodes for j in nodes if i < j]
travel_costs = {(0, 1): 10, (0, 2): 20, (0, 3): 30, (1, 2): 25, (1, 3): 35, (2, 3): 15}
purchase_costs = {(1, 0): 5, (1, 1): 7, (2, 0): 8, (2, 1): 6, (3, 0): 4, (3, 1): 9}
demands = {0: 10, 1: 15}
availabilities = {(1, 0): 10, (1, 1): 15, (2, 0): 10, (2, 1): 10, (3, 0): 10, (3, 1): 15}
positions = {0: (0, 0), 1: (1, 1), 2: (2, 0), 3: (1, -1)}  # Example positions for visualization

# Create the model
model = gp.Model("STPP")

# Variables
x = model.addVars(edges, vtype=GRB.BINARY, name="x")
y = model.addVars(nodes, vtype=GRB.BINARY, name="y")
z = model.addVars(availabilities.keys(), vtype=GRB.CONTINUOUS, name="z")

# Objective function
model.setObjective(gp.quicksum(travel_costs[e] * x[e] for e in edges) +
                   gp.quicksum(purchase_costs[i, k] * z[i, k] for (i, k) in availabilities.keys()), GRB.MINIMIZE)

# Constraints
# Product demand satisfaction
model.addConstrs((gp.quicksum(z[i, k] for i in nodes if (i, k) in availabilities) == demands[k] for k in products), "demand")

# Product availability
model.addConstrs((z[i, k] <= availabilities[i, k] * y[i] for (i, k) in availabilities.keys()), "availability")

# Supplier selection
model.addConstrs((gp.quicksum(x[e] for e in edges if i in e) == 2 * y[i] for i in nodes if i != 0), "supplier_selection")

# Tour connectivity
model.addConstrs((gp.quicksum(x[e] for e in edges if i in e) >= 2 * y[i] for i in nodes if i != 0), "connectivity")

# Optimize the model
model.optimize()

# Print the solution
if model.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    selected_edges = []
    selected_nodes = []
    for e in edges:
        if x[e].x > 0.5:
            print(f"Edge {e} is used")
            selected_edges.append(e)
    for i in nodes:
        if y[i].x > 0.5:
            print(f"Supplier {i} is selected")
            selected_nodes.append(i)
    for (i, k) in availabilities.keys():
        if z[i, k].x > 0:
            print(f"Product {k} is purchased from supplier {i} in quantity {z[i, k].x}")
else:
    print("No optimal solution found.")

# Visualization
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = positions  # Node positions for visualization

plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
nx.draw_networkx_edges(G, pos, edgelist=selected_edges, edge_color='r', width=2)
nx.draw_networkx_nodes(G, pos, nodelist=selected_nodes, node_color='orange', node_size=700)

plt.title('Optimal Tour for STPP')
plt.show()
