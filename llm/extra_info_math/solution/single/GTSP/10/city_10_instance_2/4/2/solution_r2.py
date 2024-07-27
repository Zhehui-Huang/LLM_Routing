import math
from itertools import product
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PULP_CBC_CMD

# City Coordinates and Groups
coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

city_groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Euclidean distance function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize model
model = LpProblem("Minimum_Cost_Tour", LpMinimize)

# Creating variables
pairs = [(i, j) for i in coordinates for j in coordinates if i != j]
x = LpVariable.dicts("x", pairs, cat='Binary')

# Objective Function
model += lpSum(x[(i, j)] * euclidean_distance(coordinates[i], coordinates[j]) for i, j in pairs)

# Constraints for city groups, visiting exactly one city from each group
for cities_list in city_groups.values():
    model += lpSum(x[(i, j)] for i in cities_list for j in coordinates if i != j) == 1
    model += lpSum(x[(j, i)] for i in cities_list for j in coordinates if i != j) == 1

# Each city, except the depot, should have one incoming and one outgoing connection
for city in coordinates:
    if city != 0:  # Depot is handled by group paths directly
        model += lpSum(x[(i, city)] for i in coordinates if i != city) == 1
        model += lpSum(x[(city, j)] for j in coordinates if j != city) == 1

# Solving the Model
model.solve(PULP_CBC_CMD(msg=0))

# Retrieve results
tour = [0]
current_node = 0
while len(tour) == 1 or current_node != 0:
    next_node = next(j for i, j in pairs if i == current_node and x[(i, j)].value() == 1)
    tour.append(next_node)
    current_node = next_node

total_cost = sum(x[(i, j)].value() * euclidean_distance(coordinates[i], coordinates[j]) for i, j in pairs if x[(i, j)].value() == 1)

# Output
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))