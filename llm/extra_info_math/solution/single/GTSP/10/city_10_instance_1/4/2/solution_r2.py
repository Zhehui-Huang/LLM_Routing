from pulp import LpVariable, LpProblem, LpMinimize, lpSum, LpStatus, PULP_CBC_CMD
import math

# Define city coordinates and groups
city_coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Compute Euclidean distance
def distance(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0]) ** 2 + (city_coords[i][1] - city_coords[j][1]) ** 2)

# Flatten and prepare a list of all nodes and a dictionary for grouped nodes
nodes = [0]  # Depot city is included in nodes
for group in city_groups.values():
    nodes.extend(group)

# Create a problem
problem = LpProblem("Minimize_Route", LpMinimize)

# Variables xij
x = LpVariable.dicts("x", [(i, j) for i in nodes for j in nodes if i != j], 0, 1, LpBinary)

# Objective function
problem += lpSum(x[i, j] * distance(i, j) for i in nodes for j in nodes if i != j)

# Constraints ensuring each group has exactly one city visited
for group in city_groups.values():
    # Exactly one outgoing connection from each group
    problem += lpSum(x[i, j] for i in group for j in nodes if i != j) == 1
    # Exactly one incoming connection to each group
    problem += lpSum(x[j, i] for i in group for j in nodes if i != j) == 1

# Ensuring depot(city 0) has exactly k outgoing/incoming connections where k is number of groups
problem += lpSum(x[0, j] for j in nodes if j != 0) == len(city_groups)
problem += lpSum(x[j, 0] for j in nodes if j != 0) == len(city_groups)

# Solve the linear problem using PULP_CBC_CMD solver
problem.solve(PULP_CBC_CMD(msg=False))

# Check the status of the solution
if LpStatus[problem.status] == 'Optimal':
    # Backtrack the route from the solution
    tour = [0]  # start from the depot
    while len(tour) < len(city_groups) + 1:
        next_cities = [j for j in nodes if x[tour[-1], j].varValue == 1]
        if next_cities:
            tour.append(next_cities[0])  # append the next city in the tour

    # Return back to depot
    tour.append(0)

    # Calculate the total cost from the variables
    travel_cost = sum(x[i, j].varValue * distance(i, j) for i in nodes for j in nodes if i != j and x[i, j].varValue > 0)

    # Output the results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {travel_cost:.2f}")
else:
    print("No optimal solution found.")