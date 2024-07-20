import random
import matplotlib.pyplot as plt
import networkx as nx
from gurobipy import Model, GRB, quicksum
import math

# Example data
random.seed(42)
V = list(range(1, 16))  # set of nodes
k = 5  # number of sets (partitions)

# Generate random coordinates for each node
coords = {i: (random.uniform(0, 100), random.uniform(0, 100)) for i in V}

# Cluster nodes into k groups (3 nodes each)
V_p = [[] for _ in range(k)]
for i, node in enumerate(V):
    V_p[i % k].append(node)

# Ensure we have exactly k clusters of 3 nodes each
assert len(V_p) == k and all(len(cluster) == 3 for cluster in V_p)

# Cost matrix with Euclidean distances
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

c = {(i, j): euclidean_distance(coords[i], coords[j]) for i in V for j in V if i != j}

# Create a new model
m = Model("generalized_tsp")

# Create variables
x = m.addVars(V, V, vtype=GRB.BINARY, name="x")
u = m.addVars(range(2, k+1), vtype=GRB.CONTINUOUS, name="u")

# Set objective
m.setObjective(quicksum(c[i, j] * x[i, j] for i in V for j in V if i != j), GRB.MINIMIZE)

# Add constraints
for p in range(k):
    m.addConstr(quicksum(x[i, j] for i in V_p[p] for j in V if j not in V_p[p]) == 1, name=f"c2_{p+1}")
    m.addConstr(quicksum(x[i, j] for j in V_p[p] for i in V if i not in V_p[p]) == 1, name=f"c3_{p+1}")

for i in V:
    m.addConstr(quicksum(x[j, i] for j in V if j != i) - quicksum(x[i, j] for j in V if j != i) == 0, name=f"c4_{i}")

for p in range(2, k+1):
    for q in range(2, k+1):
        if p != q:
            m.addConstr(u[p] - u[q] + k * quicksum(x[i, j] for i in V_p[p-1] for j in V_p[q-1]) +
                        (k-2) * quicksum(x[i, j] for i in V_p[q-1] for j in V_p[p-1]) <= k-1, name=f"c7_{p}_{q}")

for p in range(2, k+1):
    m.addConstr(u[p] >= 0, name=f"c8_{p}")

# Optimize model
m.optimize()

# Extract solution
edges = []
if m.status == GRB.OPTIMAL:
    for i in V:
        for j in V:
            if i != j and x[i, j].x > 1e-6:
                edges.append((i, j))

# Visualize the solution
G = nx.DiGraph()
G.add_edges_from(edges)
pos = {i: coords[i] for i in V}

plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
edge_labels = {(i, j): f'{c[i,j]:.1f}' for i, j in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Draw clusters
colors = ['red', 'blue', 'green', 'purple', 'orange']
for cluster_idx, cluster in enumerate(V_p):
    nx.draw_networkx_nodes(G, pos, nodelist=cluster, node_color=colors[cluster_idx], node_size=700, alpha=0.6)

plt.title('Generalized TSP Solution with Distance-Based Costs and Clusters')
plt.show()
