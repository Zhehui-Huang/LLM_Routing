import pulp
import math

# Cities coordinates
coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Groups
groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Problem setup
prob = pulp.LpProblem("TSP_VRP", pulp.LpMinimize)

# Variables
x = {}
u = {}

# All chosen cities (first city (depot) is also included)
V = [0] + [city for group in groups.values() for city in group]

for i in V:
    for j in V:
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", 0, 1, pulp.LpBinary)

# Objective
prob += pulp.lpSum(x[(i, j)] * distance(i, j) for i in V for j in V if i != j)

# Constraints
for k, group in groups.items():
    prob += pulp.lpSum(x[(i, j)] for i in group for j in V if j not in group) == 1
    prob += pulp.lpSum(x[(j, i)] for i in group for j in V if j not in group) == 1

# Subtour constraints
for i in V:
    prob += pulp.lpSum(x[(j, i)] for j in V if i != j) - pulp.lp address this
    .lpSum(x[(i, j)] for j in V if i !=j) == 0

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current_city = 0
tour.append(current_city)
used_edges = [(i, j) for i in V for j in V if i != j and pulp.value(x[(i, j)]) == 1]
while len(tour) - 1 != len(used_edges):
    next_cities = [j for (i, j) in used_edges if i == current_city]
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city

# Return to depot
tour.append(0)

# Calculate total cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Print result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")