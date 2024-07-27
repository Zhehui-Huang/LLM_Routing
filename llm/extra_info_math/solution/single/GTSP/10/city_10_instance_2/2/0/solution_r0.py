import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Groups of cities
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Calculate Euclidean distances between each pair of cities
def euclidean(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

distances = {(i, j): euclidean(i, j) for i in cities for j in cities if i != j}

# Set up the Optimization Problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", distances, 0, 1, pulp.LpBinary)

# Objective
prob += pulp.lpSum([distances[(i, j)] * x[i, j] for i, j in distances]), "Minimize_Total_Distance"

# Constraints
# Each city in a group is connected to exactly one city not in the group (outgoing and incoming)
for group in groups:
    prob += pulp.lpSum([x[i, j] for i in group for j in cities if j not in group]) == 1, f"Outgoing_from_group_{groups.index(group)}"
    prob += pulp.lpSum([x[j, i] for i in group for j in cities if j not in group]) == 1, f"Incoming_to_group_{groups.index(group)}"

# Flow conservation constraint to maintain the tour
for city in cities.keys():
    prob += (pulp.lpSum([x[j, city] for j in cities if (j, city) in x]) ==
             pulp.lpSum([x[city, k] for k in cities if (city, k) in x])), f"Flow_conservation_{city}"

# Solving the problem
solver = pulp.PULP_CBC_CMD(msg=0)
prob.solve(solver)

# Check the result
if prob.status == -1:
    print("The problem is infeasible.")
else:
    # Retrieve the result
    tours = [(i, j) for i, j in x if pulp.value(x[i, j]) == 1]
    # Extract the path from the tours
    path = [0]
    while len(path) < len(tours) + 1:
        next_city = [j for i, j in tours if i == path[-1]][0]
        path.append(next_city)

    # Calculate total cost of the tour
    total_cost = sum(distances[(path[i], path[i+1])] for i in range(len(path) - 1))
    
    print(f"Tour: {path}")
    print(f"Total travel cost: {total_cost}")