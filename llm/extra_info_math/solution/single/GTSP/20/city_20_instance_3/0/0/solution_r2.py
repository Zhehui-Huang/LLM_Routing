import pulp
from itertools import product
from math import sqrt

# City coordinates
cities = {
    0: (30, 56), 
    1: (53, 42), 
    2: (1, 95), 
    3: (25, 61), 
    4: (69, 57), 
    5: (6, 58), 
    6: (12, 84), 
    7: (72, 77), 
    8: (98, 95), 
    9: (11, 0), 
    10: (61, 25), 
    11: (52, 0), 
    12: (60, 95), 
    13: (10, 94), 
    14: (96, 73), 
    15: (14, 47), 
    16: (18, 16), 
    17: (4, 43), 
    18: (53, 76), 
    19: (19, 72)
}

# City groups
city_groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Formulate the problem
problem = pulp.LpProblem("TSP_Grouped_Cities", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], 0, 1, pulp.LpBinary)

# One city per group, plus going back to the depot
total_groups = len(city_groups) + 1

# Objective Function
problem += pulp.lpSum([x[i, j] * distance(i, j) for i, j in x.keys()]), "Minimize_Distance"

# Each group must have exactly one outgoing edge to a node outside the group
for group, members in city_groups.items():
    problem += pulp.lpSum(x[i, j] for i in members for j in set(cities.keys()) - set(members)) == 1, f"One_outgoing_from_group_{group}"
    problem += pulp.lpSum(x[j, i] for i in members for j in set(cities.keys()) - set(members)) == 1, f"One_incoming_to_group_{group}"

# Add flow conservation constraints
for city in cities.keys():
    problem += (pulp.lpSum(x[i, city] for i in cities if i != city)
                == pulp.lpSum(x[city, j] for j in cities if j != city)), f"Flow_conservation_{city}"

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Determine the optimal tour and cost if solved
if status == pulp.LpStatusOptimal:
    tour = [0]
    while len(tour) < total_groups:
        current_city = tour[-1]
        for next_city in cities:
            if pulp.value(x[current_city, next_city]) == 1:
                tour.append(next_city)
                break
    tour.append(0)  # return to depot city
    total_distance = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
else:
    tour = []
    total_distance = None

print('Tour:', tour)
print('Total travel cost:', total_distance)