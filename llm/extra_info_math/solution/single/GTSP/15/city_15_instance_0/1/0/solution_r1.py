import pulp
import math

# City coordinates
coordinates = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# City Groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Compute the distance function
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# All nodes, including the depot
all_nodes = list(coordinates.keys())

# Variable to store each city assigned to one group only for simplicity
city_to_group = {}
for group_id, cities in groups.items():
    for city in cities:
        city_to_group[city] = group_id

# Instantiate the problem
problem = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Variables: x[i, j] = 1 if path i to j is taken
x = pulp.LpVariable.dicts("x", ((i, j) for i in all_nodes for j in all_nodes if i != j), cat='Binary')

# Objective Function
problem += pulp.lpSum(distance(i, j) * x[i, j] for i in all_nodes for j in all_nodes if i != j)

# Constraints
# We need exactly one outgoing connection from the depot and one incoming connection to the depot
problem += pulp.lpSum(x[(0, j)] for j in all_nodes if j != 0) == 1
problem += pulp.lpSum(x[(i, 0)] for i in all_nodes if i != 0) == 1

# Flow conservation constraints(Every city must have one entry and one exit if it's not depot)
for city in all_nodes[1:]:
    problem += pulp.lpSum(x[(j, city)] for j in all_nodes if j != city) == 1
    problem += pulp.lpSum(x[(city, j)] for j in all_nodes if j != city) == 1

# Each group must be connected exactly to two different cities, one from inside and one from outside
for group_id, cities in groups.items():
    other_cities = [city for city in all_nodes if city not in cities]
    problem += pulp.lpSum(x[(i, j)] for i in cities for j in other_cities) == 1 # Exactly one connection from group to outside
    problem += pulp.lpSum(x[(j, i)] for i in cities for j in other_cities) == 1 # Exactly one connection to group from outside

# Solve the problem
problem.solve()

# Calculate the tour and cost based on the LP solution
tour = [0]
current_city = 0
cost = 0

# Extracting the tour from the variables
while True:
    next_city = next(j for j in all_nodes if j != current_city and pulp.value(x[(current_city, j)]) == 1)
    cost += distance(current_city, next_city)
    current_city = next_city
    tour.append(current_city)
    if current_city == 0:
        break

print("Tour:", tour)
print("Total travel cost:", cost)