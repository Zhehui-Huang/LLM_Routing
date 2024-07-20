import gurobipy as gp
from gurobipy import GRB
import matplotlib.pyplot as plt
import networkx as nx
import random


# *************************************
# random cases are not always feasible 
# *************************************

# Parameters for random data generation
num_nodes = 18  # including the depot
num_edges = 20
num_products = 5
max_demand = 10
max_quantity = 15
max_price = 20
max_travel_cost = 50

# Generate random nodes and edges
V = list(range(num_nodes))  # List of nodes including the depot (node 0)
E = random.sample([(i, j) for i in V for j in V if i < j], num_edges)  # List of edges

# Generate random products, suppliers, demand, quantity, price, and travel cost
K = list(range(num_products))  # List of products
M_k = {k: random.sample(V[1:], random.randint(1, num_nodes - 1)) for k in K}  # Suppliers for each product
d_k = {k: random.randint(1, max_demand) for k in K}  # Demand for each product
q_ik = {(i, k): random.randint(1, max_quantity) for k in K for i in M_k[k]}  # Quantity of product k at supplier i
p_ik = {(i, k): random.randint(1, max_price) for k in K for i in M_k[k]}  # Price of product k at supplier i
c_e = {(i, j): random.randint(1, max_travel_cost) for i, j in E}  # Cost of traveling on edge e

# Create a new model
model = gp.Model("STPP")

# Create variables
x = model.addVars(E, vtype=GRB.BINARY, name="x")
y = model.addVars(V, vtype=GRB.BINARY, name="y")
z = model.addVars(q_ik.keys(), vtype=GRB.CONTINUOUS, name="z")

# Set objective function
model.setObjective(gp.quicksum(c_e[e] * x[e] for e in E) +
                   gp.quicksum(p_ik[i, k] * z[i, k] for i, k in q_ik.keys()), GRB.MINIMIZE)

# Add constraints
for k in K:
    model.addConstr(gp.quicksum(z[i, k] for i in M_k[k]) == d_k[k], name=f"demand_{k}")

for i, k in q_ik.keys():
    model.addConstr(z[i, k] <= q_ik[i, k] * y[i], name=f"quantity_{i}_{k}")

for h in V:
    model.addConstr(gp.quicksum(x[e] for e in E if h in e) == 2 * y[h], name=f"degree_{h}")

# Generate all non-empty proper subsets of V excluding the depot
for S in range(1, 1 << (len(V) - 1)):
    subset = [V[i] for i in range(len(V)) if (S & (1 << i)) > 0]
    if len(subset) > 1:
        for h in subset:
            model.addConstr(gp.quicksum(x[e] for e in E if (e[0] in subset and e[1] not in subset) or (e[1] in subset and e[0] not in subset)) >= 2 * y[h],
                            name=f"connectivity_{subset}_{h}")

# Optimize the model
model.optimize()

# Print the solution
if model.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    for e in E:
        if x[e].x > 0.5:
            print(f"Edge {e} is used.")
    for i in V:
        if y[i].x > 0.5:
            print(f"Supplier {i} is visited.")
    for i, k in z.keys():
        if z[i, k].x > 0.1:
            print(f"Purchase {z[i, k].x} units of product {k} from supplier {i}.")
else:
    print("No optimal solution found.")

# Visualization
G = nx.Graph()

# Add nodes
for node in V:
    G.add_node(node)

# Add edges
for e in E:
    if x[e].x > 0.5:
        G.add_edge(e[0], e[1])

# Position nodes using a layout
pos = nx.spring_layout(G)

# Draw the network
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')

# Draw edge labels
edge_labels = {(i, j): f'' for i, j in E if x[(i, j)].x > 0.5}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title('Optimal Tour for the STPP')
plt.show()
