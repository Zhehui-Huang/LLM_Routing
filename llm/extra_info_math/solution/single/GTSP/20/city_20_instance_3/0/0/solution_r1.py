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

# Objective Function
problem += pulp.lpSum([x[i, j] * distance(i, j) for i in cities for j in cities if i != j]), "Minimize_Distance"

# Constraints
for group in city_groups.values():
    problem += pulp.lpSum([x[i, j] for i in group for j in cities if j not in group]) == 1, f"One_outgoing_from_group_{group}"
    problem += pulp.lpSum([x[j, i] for i in group for j in cities if j not in group]) == 1, f"One_incoming_to_group_{group}"

# Flow conservation
for city in cities:
    problem += (pulp.lpSum([x[i, city] for i in cities if i != city]) ==
                pulp.lpSum([x[city, j] for j in cities if j != city])), f"Flow_conservation_{city}"

# Solve the problem
problem.solve()
objective_value = pulp.value(problem.objective)

# Find the tour
tour = [0]  # starting at the depot city 0
visited = set(tour)
while len(tour) < len(city_groups) + 2:  # one city per group + one more visit to depot
    for j in cities:
        if j not in visited and pulp.value(x[tour[-1], j]) == 1:
            tour.append(j)
            visited.add(j)
            break

# Calculate total distance
total_distance = sum([distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)])

print('Tour:', tour)
print('Total travel cost:', total_distance)