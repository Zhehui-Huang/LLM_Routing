import gurobipy as gp
from gurobipy import GRB
import itertools
import matplotlib.pyplot as plt
import networkx as nx

# Function to solve the TSP using the DFJ formulation
def solve_tsp(cities, distance_matrix):
    n = len(cities)

    # Create a new Gurobi model
    model = gp.Model("TSP")

    # Create variables
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")

    # Set the objective function
    model.setObjective(gp.quicksum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)

    # Add constraints
    # Each city must be left exactly once
    for i in range(n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(n) if j != i) == 1, name=f"leave_{i}")

    # Each city must be entered exactly once
    for j in range(n):
        model.addConstr(gp.quicksum(x[i, j] for i in range(n) if i != j) == 1, name=f"enter_{j}")

    # DFJ subtour elimination constraints
    def add_subtour_elimination_constraints(model, x, n):
        subsets = []
        for r in range(2, n):
            subsets.extend(itertools.combinations(range(n), r))
        
        for subset in subsets:
            S = set(subset)
            if 1 <= len(S) <= n - 1:
                model.addConstr(gp.quicksum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1)

    add_subtour_elimination_constraints(model, x, n)

    # Optimize the model
    model.optimize()

    # Extract the solution
    if model.status == GRB.OPTIMAL:
        tour = []
        for i in range(n):
            for j in range(n):
                if x[i, j].x > 0.5:
                    tour.append((i, j))
        return tour, model.objVal
    else:
        return None, None

# Function to plot the TSP tour
def plot_tour(cities, distance_matrix, tour):
    G = nx.DiGraph()
    
    pos = {i: (i, 0) for i in range(len(cities))}

    # Add nodes
    for i in range(len(cities)):
        G.add_node(i, pos=pos[i])

    # Add edges
    for (i, j) in tour:
        G.add_edge(i, j)

    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)
    edge_labels = {(i, j): f'{distance_matrix[i][j]}' for i, j in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Optimal TSP Tour")
    plt.show()

# Example usage
if __name__ == "__main__":
    cities = ["A", "B", "C", "D"]
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    tour, cost = solve_tsp(cities, distance_matrix)

    if tour:
        print(f"Optimal tour: {tour}")
        print(f"Optimal cost: {cost}")
        plot_tour(cities, distance_matrix, tour)
    else:
        print("No optimal solution found.")
