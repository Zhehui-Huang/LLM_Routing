from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# Define the cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Groups of cities (clusters)
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate a dictionary with all pairs of cities and their distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Create the problem
problem = LpProblem("TSP_For_Groups", LpMinimize)

# Each city needs to be mapped to the respective group for unique selection
city_group_map = {}
for index, group in enumerate(groups):
    for city in group:
        city_group_map[city] = f"Group_{index+1}"

# Variables x_ij, where i, j are cities indices and (i != j)
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat=LpBinary)

# Objective function
problem += lpSum(distances[(i, j)] * x[(i, j)] for i in cities for j in cities if i != j), "Total Travel Cost"

# Constraint: Ensure exactly one path enters and leaves each group
for group in groups:
    problem += lpSum(x[i,j] for i in group for j in cities if j not in group) == 1, f"Outflow_from_group_{groups.index(group)+1}"
    problem += lpSum(x[j,i] for i in group for j in cities if j not in group) == 1, f"Inflow_to_group_{groups.index(group)+1}"

# Flow conservation at each city
for i in cities:
    if i != 0:  # Avoid the depot for continuity, depot will be enforced by other constraints
        problem += lpSum(x[(j, i)] for j in cities if j != i) == lpSum(x[(i, j)] for j in cities if j != i), f"Flow_conservation_city_{i}"

# Ensure the robot returns to the starting point, constraints specifically for depot
problem += lpSum(x[(0, j)] for j in cities if j != 0) == 1, "Leave_depot"
problem += lpSum(x[(j, 0)] for j in cities if j != 0) == 1, "Return_to_depot"

# Solve the problem
problem.solve()
status = LpProblem.solve(problem)

# Check if an optimal solution was obtained:
if status == 1:
    tour = [0]
    used_edges = [(i, j) for i in cities for j in cities if i != j and x[(i, j)].varValue == 1]

    # Constructing the tour from the starting city
    current_city = 0
    while len(used_edges) > 0:
        for edge in used_edges:
            if edge[0] == current_city:
                tour.append(edge[1])
                current_city = edge[1]
                used_edges.remove(edge)
                break
    
    # Calculate the total cost of the tour
    total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found. Please check the constraints and data.")