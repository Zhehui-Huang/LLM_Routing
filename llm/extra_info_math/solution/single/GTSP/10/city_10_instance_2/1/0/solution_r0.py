from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary
from math import sqrt

# Define city coordinates and groups
city_coordinates = {
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

city_groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Function to compute Euclidean distance
def euclidean_distance(city1, city2):
    x_diff = city_coordinates[city1][0] - city_coordinates[city2][0]
    y_diff = city_coordinates[city1][1] - city_coordinates[city2][1]
    return sqrt(x_diff**2 + y_diff**2)

# Generating all relevant pairs and their distances
distances = {}
nodes = [0] + [city for sublist in city_groups.values() for city in sublist]
for i in nodes:
    for j in nodes:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Create the optimization problem
prob = LpProblem("TSP_Groups", LpMinimize)

# Decision variables x_ij
x = LpVariable.dicts("x", ((i, j) for i in nodes for j in nodes if i != j), cat=LpBinary)

# Objective function
prob += lpSum(x[(i, j)] * distances[(i, j)] for i in nodes for j in nodes if i != j)

# Constraints
# Ensure each group's city has exactly one outgoing and one incoming link
for group, cities in city_groups.items():
    prob += lpSum(x[(i, j)] for i in cities for j in nodes if i != j) == 1
    prob += lpSum(x[(j, i)] for i in cities for j in nodes if i != j) == 1

# Flow conservation at each node
for k in nodes[1:]:
    prob += lpSum(x[(i, k)] for i in nodes if i != k) - lpSum(x[(k, j)] for j in nodes if j != k) == 0

# Solve the problem
prob.solve()

# Fetch the results
tour = []
current_node = 0
visited = set()
total_cost = 0

while True:
    visited.add(current_node)
    tour.append(current_node)
    
    next_nodes = [(j, x[(current_node, j)].varValue) for j in nodes if j != current_node]
    next_node = next(j for j, v in next_nodes if v > 0)
    total_cost += distances[(current_node, next_node)]
    
    if next_node == 0:
        break
    current_node = next_name
    
tour.append(0)  # Return to starting depot

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")