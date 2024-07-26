import os
import math
import random
import itertools
import sys

import numpy as np
import gurobipy as gp
import matplotlib.pyplot as plt
from gurobipy import GRB

from verifier_ip.utils import calculate_distance_matrix, TASK_BASE_PATH, read_city_locations, route2edges


def solve_tsp_verifier(cities, distance_matrix, sol_x):
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

    # enforce solution to be the same as sol_x
    for i in range(n):
        for j in range(n):
            model.addConstr(x[i, j] == sol_x[i][j])
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


def main():
    task_folder_path = os.path.join(TASK_BASE_PATH, 'single/TSP')
    file_list = os.listdir(task_folder_path)
    file_list.sort()

    for file_name in file_list:
        task_instance_path = os.path.join(task_folder_path, file_name)
        cities = read_city_locations(task_instance_path)
        distance_matrix = calculate_distance_matrix(cities)

        # route = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        # TODO: Extract routes from the results
        route = []

        sol_x = route2edges(route, len(cities))
        tour, cost = solve_tsp_verifier(cities=cities, distance_matrix=distance_matrix, sol_x=sol_x)

        if tour:
            print("***********\tSTART\t***************")
            print(f"feasible route: {route}\t\tcost: {cost}")
            print("***********\tEND\t***************")
            # plot_tour(cities, distance_matrix, tour)
            # visualize_tour(cities, tour)
        else:
            print("***********\tSTART\t***************")
            print("Infeasible route.")
            print("***********\tEND\t***************")


# Example usage
if __name__ == "__main__":
    sys.exit(main())
