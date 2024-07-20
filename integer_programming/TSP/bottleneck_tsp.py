#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:40:38 2024

@author: shiguangyao
"""

import gurobipy as gp
from gurobipy import GRB
import itertools
import matplotlib.pyplot as plt
import networkx as nx

# Function to solve the Bottleneck TSP using the DFJ formulation
def solve_bottleneck_tsp(cities, distance_matrix):
    n = len(cities)

    # Create a new Gurobi model
    model = gp.Model("BottleneckTSP")

    # Create variables
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
    z = model.addVar(vtype=GRB.CONTINUOUS, name="z")

    # Set the objective function to minimize the maximum edge cost
    model.setObjective(z, GRB.MINIMIZE)

    # Add constraints
    # Each city must be left exactly once
    for i in range(n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(n) if j != i) == 1, name=f"leave_{i}")

    # Each city must be entered exactly once
    for j in range(n):
        model.addConstr(gp.quicksum(x[i, j] for i in range(n) if i != j) == 1, name=f"enter_{j}")

    # Ensure the bottleneck cost is greater than or equal to each edge cost in the tour
    for i in range(n):
        for j in range(n):
            if i != j:
                model.addConstr(x[i, j] * distance_matrix[i][j] <= z, name=f"bottleneck_{i}_{j}")

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

    plt.title("Optimal Bottleneck TSP Tour")
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

    tour, cost = solve_bottleneck_tsp(cities, distance_matrix)

    if tour:
        print(f"Optimal tour: {tour}")
        print(f"Optimal cost (maximum edge cost): {cost}")
        plot_tour(cities, distance_matrix, tour)
    else:
        print("No optimal solution found.")
