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

# Generating all possible pairs and their distances
distances = {}
nodes = [0] + [city for sublist in city_groups.values() for city in sublist]
for i in nodes:
    for j in nodes:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Optimization problem
prob = LpProblem("Minimize_Travel_Cost", LpMinimize)

# Decision variables x_ij
x = LpVariable.dicts("route", [(i, j) for i in nodes for j in nodes if i != j], cat='Binary')

# Objective function: Minimize total distance
prob += lpSum(distances[i, j] * x[i, j] for i in nodes for j in nodes if i != j)

# Constraints
# Ensure one outgoing and one incoming connection for each group representative
for group, cities in city_groups.items():
    prob += lpSum(x[i, j] for i in cities for j in nodes if j not in cities) == 1
    prob += lpSum(x[j, i] for i in cities for j in nodes if j not in cities) == 1

# Flow conservation for each city
for k in nodes:
    prob += lpSum(x[i, k] for i in nodes if i != k) == lpSum(x[k, j] for j in nodes if k != j)

# Solve the problem
prob.solve()

tour = []
current = 0
visited = set([0])
path_cost = 0

while len(visited) < len(nodes):
    for j in nodes:
        if x[(current, j)].varValue > 0.5 and j not in visited:
            path_cost += distances[(current, j)]
            tour.append(j)
            visited.add(j)
            current = j
            break
tour.append(0)
path_cost += distances[(current, 0)]

# Output the optimized tour and its cost
print("Tour:", tour)
print("Total travel cost:", round(path_cost, 2))