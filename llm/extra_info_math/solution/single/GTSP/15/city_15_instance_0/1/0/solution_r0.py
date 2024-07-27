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

# Total city count, including the depot
city_count = len(coordinates)

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Create the LP problem
problem = pulp.LpProblem("Robot_Tour_Problem", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(city_count) for j in range(city_district) if i != j], cat=pulp.LpBinary)

# Objective Function
problem += pulp.lpSum([x[(i, j)] * euclidean_distance(i, j) for i in range(city_count) for j in range(city_distance) if i != j])

# Constraints for visiting each group exactly once
for group in groups.values():
    problem += pulp.lpSum([x[(i, j)] for i in group for j in range(city_count) if j not in group]) == 1
    problem += pulp.lpSum([x[(j, i)] for i in group for j in range(city_count) if j not in group]) == 1

# Flow conservation constraints
for i in range(city_count):
    problem += pulp.lpSum([x[(j, i)] for j in range(city_count) if j != i]) == pulp.lpSum([x[(i, j)] for j in range(city_count) if j != i])

# Solve the problem
problem.solve()

# Retrieve the solution
tour = []
visited = set()
current_city = 0
total_cost = 0

while True:
    next_city = [j for j in range(city_count) if j != current_city and pulp.value(x[(current_city, j)]) == 1][0]
    tour.append(current_city)
    visited.add(current_city)
    total_cost += euclidean_distance(current_city, next_city)
    if next_city == 0:
        break
    current_city = next_city

tour.append(0)  # append depot city at the end to complete the cycle

print("Tour:", tour)
print("Total travel cost:", total_cost)