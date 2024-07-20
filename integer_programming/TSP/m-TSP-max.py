import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from gurobipy import Model, GRB, quicksum

# Parameters
N = 10  # Number of cities (including depot)
M = 3   # Number of salesmen
#np.random.seed(40)  # For reproducibility

# Generate random coordinates for cities
coords = np.random.rand(N, 2) * 100

# Compute the distance matrix using Euclidean distance
d = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        d[i, j] = np.linalg.norm(coords[i] - coords[j])

# Create model
m = Model()

# Variables
x = m.addVars(N, N, M, vtype=GRB.BINARY, name='x')
u = m.addVars(N, M, vtype=GRB.CONTINUOUS, name='u')
L = m.addVar(vtype=GRB.CONTINUOUS, name='L')

# Objective: Minimize the maximum route length
m.setObjective(L, GRB.MINIMIZE)

# Constraints
# Each city is visited exactly once
m.addConstrs((quicksum(x[i, j, k] for k in range(M) for j in range(N) if j != i) == 1 for i in range(1, N)), name='visit_once')

# Each salesman starts and ends at the depot
m.addConstrs((quicksum(x[0, j, k] for j in range(1, N)) == 1 for k in range(M)), name='start_depot')
m.addConstrs((quicksum(x[i, 0, k] for i in range(1, N)) == 1 for k in range(M)), name='end_depot')

# Subtour elimination (MTZ constraints)
m.addConstrs((u[i, k] - u[j, k] + N * x[i, j, k] <= N - 1 for i in range(1, N) for j in range(1, N) if i != j for k in range(M)), name='subtour_elimination')
m.addConstrs((u[i, k] >= 2 for i in range(1, N) for k in range(M)), name='u_lower_bound')
m.addConstrs((u[i, k] <= N for i in range(1, N) for k in range(M)), name='u_upper_bound')

# Flow constraints to ensure the continuity of each tour
m.addConstrs((quicksum(x[i, j, k] for j in range(N) if j != i) - quicksum(x[j, i, k] for j in range(N) if j != i) == 0 for i in range(N) for k in range(M)), name='flow_continuity')

# Maximum route length constraint
m.addConstrs((quicksum(d[i][j] * x[i, j, k] for i in range(N) for j in range(N) if i != j) <= L for k in range(M)), name='max_route_length')

# Optimize model
m.optimize()

# Print solution
if m.status == GRB.OPTIMAL:
    print('Optimal value:', L.X)
    for k in range(M):
        print(f'Salesman {k + 1}:')
        for i in range(N):
            for j in range(N):
                if x[i, j, k].X > 0.5:
                    print(f'  {i} -> {j}')

    # Visualization
    G = nx.DiGraph()
    for i in range(N):
        G.add_node(i, pos=(coords[i][0], coords[i][1]))

    edge_labels = {}
    colors = ['r', 'b', 'g', 'c', 'm']
    for k in range(M):
        for i in range(N):
            for j in range(N):
                if x[i, j, k].X > 0.5:
                    G.add_edge(i, j, color=colors[k % len(colors)], weight=2)
                    edge_labels[(i, j)] = f'{d[i][j]:.2f}'

    pos = nx.get_node_attributes(G, 'pos')
    edges = G.edges()
    edge_colors = [G[u][v]['color'] for u, v in edges]
    weights = [G[u][v]['weight'] for u, v in edges]

    nx.draw(G, pos, edge_color=edge_colors, width=weights, with_labels=True, node_size=500, node_color='orange')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

else:
    print('No optimal solution found')
