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

# Generating all relevant node pairs and their distances
distances = {}
nodes = [0] + [city for sublist in city_groups.values() for city in sublist]
for i in nodes:
    for j in nodes:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Create the optimization problem
prob = LpProblem("TSP_Groups", LprMinimize)

# Decision variables x_ij
x = LpVariable.dicts("x", ((i, j) for i in nodes for j in nodes if i != j), cat=LpBinary)

# Objective function
prob += lpSum(x[(i, j)] * distances[(i, j)] for i in nodes for j in nodes if i != j)

# Constraints to ensure one city per group connection
for group, cities in city_groups.items():
    prob += lpSum(x[(i, j)] for i in cities for j in nodes if j not in cities) == 1
    prob += lpSum(x[(j, i)] for i in cities for j in nodes if j not in cities) == 1

# Flow conservation for each city
for k in nodes:
    prob += lpSum(x[(i, k)] for i in nodes if i != k) - lpSum(x[(k, j)] for j in nodes if j != k) == 0

# Solve the problem
prob.solve()

# Extract the tour based on the variables that are set to 1 and compute the cost
tour = [0]
current_city = 0
total_cost = 0

while True:
    next_city = None
    for j in nodes:
        if j != current_city and x[(current_city, j)].varValue > 0.99:  # Ensuring a binarized decision
            next_city = j
            break
    if next_city is None or next_city == 0:
        break
    tour.append(next_city)
    total_cost += distances[(current_city, next_city)]
    current_city = next_city

tour.append(0)  # coming back to the depot
total_cost += distances[(current_city, 0)]  # cost to return to depot

# Output results
print("Tour:", tour)
print("Total travel cost:", total(ns(total_cost))