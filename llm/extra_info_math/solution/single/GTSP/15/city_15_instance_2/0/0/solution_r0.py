import pulp
import math

# Coordinates of the cities
coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Groups of cities (including depot in all groups artificially for modeling convenience)
groups = [
    [0, 8, 12, 14],
    [0, 7, 10, 11],
    [0, 4, 6, 9],
    [0, 1, 3, 13],
    [0, 2, 5]
]

# Euclidean distance calculation
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Problem setup
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if the robot travels from city_i to city_j
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in coordinates for j in coordinates if i != j}

# Objective Function
problem += pulp.lpSum(x[i, j] * distance(i, j) for i in coordinates for j in coordinates if i != j), "Total_Travel_Cost"

# Constraints
# Each group must have exactly one outgoing edge to non-group nodes
for group in groups:
    problem += pulp.lpSum(x[i, j] for i in group for j in coordinates if j not in group and i != j) == 1, f"One_outgoing_from_group_{group}"

# Each group must have exactly one incoming edge from non-group nodes
for group in groups:
    problem += pulp.lpSum(x[j, i] for i in group for j in coordinates if j not in group and i != j) == 1, f"One_incoming_to_group_{group}"

# Ensuring tour continuity
for i in coordinates:
    problem += pulp.lpSum(x[j, i] for j in coordinates if j != i) == pulp.lpSum(x[i, k] for k in coordinates if k != i), f"Flow_conservation_{i}"

# Solve the problem
problem.solve()

# Extract the solution
tour = []
visited = set()
current = 0
while True:
    visited.add(current)
    tour.append(current)
    next_city = next(j for j in coordinates if j != current and pulp.value(x[current, j]) == 1)
    if next_city == 0:
        break
    current = next_city
tour.append(0)  # return to the depot

# Calculate total cost
total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Results output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")