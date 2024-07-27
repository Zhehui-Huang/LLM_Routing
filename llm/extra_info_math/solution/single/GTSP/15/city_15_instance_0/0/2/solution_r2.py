import math
from docplex.mp.model import Model

# Define the cities and their coordinates
cities = {
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

# Define the groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Calculate Euclidean distances between each pair of cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Model
mdl = Model('TSP_Variant')

# Variables
x = mdl.binary_var_matrix(cities.keys(), cities.keys(), name='x')

# Objective
mdl.minimize(mdl.sum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j))

# Constraints
for key, group in groups.items():
    # Exactly one outgoing edge from group to other cities
    non_group = [i for i in cities if i not in group]
    mdl.add_constraint(mdl.sum(x[i, j] for i in group for j in non_group) == 1)
    
    # Exactly one incoming edge to group from other cities
    mdl.add_constraint(mcor(mdl.sum(x[j, i] for i in group for j in non_group) == 1))

# Flow conservation
for i in cities:
    mdl.add_constraint(mdl.sum(x[i, j] for j in cities if j != i) - mdl.sum(x[j, i] for j in cities if j != i) == 0)

# Solve
solution = mdl.solve(log_output=True)

if solution:
    # Extract and print the tour
    tour = []
    visited = set()
    current = 0
    while len(tour) < 6:  # As it requires visiting one city from each group plus depot twice
        tour.append(current)
        visited.add(current)
        next_city = next(j for j in cities if x[current, j].solution_value > 0.5 and j not in visited)
        current = next_city

    if tour[-1] != 0:  # Ensure it returns to depot
        tour.append(0)

    total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print("Tour:", tour)
    print("Total travel cost:", round(total_distance, 2))
else:
    print("No solution found.")