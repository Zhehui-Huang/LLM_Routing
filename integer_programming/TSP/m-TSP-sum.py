import gurobipy as gp
from gurobipy import GRB
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def generate_random_costs(num_locations):
    # Generate random coordinates for the locations
    coordinates = np.random.rand(num_locations, 2) * 100  # Scale up for better visualization
    # Calculate the Euclidean distance between each pair of locations
    costs = np.zeros((num_locations, num_locations))
    for i in range(num_locations):
        for j in range(num_locations):
            costs[i, j] = np.linalg.norm(coordinates[i] - coordinates[j])
    return coordinates, costs

def solve_mTSP(num_locations, num_salesmen):
    coordinates, costs = generate_random_costs(num_locations)
    n = num_locations  # Number of nodes (including depot)
    m = num_salesmen   # Number of salesmen

    # Model
    model = gp.Model()

    # Variables
    x = model.addVars(n, n, vtype=GRB.BINARY, name='x')
    u = model.addVars(n, vtype=GRB.CONTINUOUS, name='u')

    # Objective
    model.setObjective(gp.quicksum(costs[i][j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)

    # Constraints
    model.addConstr(gp.quicksum(x[0, j] for j in range(1, n)) == m, "depot_departure")
    model.addConstr(gp.quicksum(x[j, 0] for j in range(1, n)) == m, "depot_return")

    for i in range(1, n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(n) if j != i) == 1, f"visit_{i}")
        model.addConstr(gp.quicksum(x[j, i] for j in range(n) if j != i) == 1, f"return_{i}")

    # Subtour elimination (MTZ constraints)
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model.addConstr(u[i] - u[j] + (n * x[i, j]) <= n - 1)

    # Optimize
    model.optimize()

    # Extract solution
    solution = []
    for i in range(n):
        for j in range(n):
            if x[i, j].X > 0.5:
                solution.append((i, j))

    # Visualization
    G = nx.DiGraph()
    G.add_nodes_from(range(n))
    G.add_edges_from(solution)

    pos = {i: coordinates[i] for i in range(n)}
    labels = {i: f"{i}" for i in range(n)}
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
    edge_labels = {(i, j): f"{costs[i][j]:.2f}" for i, j in solution}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Multiple Traveling Salesman Problem Solution")
    plt.show()

# Adjustable parameters
num_locations = 20  # Adjust this for different number of locations
num_salesmen = 3    # Adjust this for different number of salesmen

solve_mTSP(num_locations, num_salesmen)
