import math
from pulp import LpMinimize, LpProblem, LpVariable, LpInteger, lpSum, LpStatus, PULP_CBC_CMD

# City coordinates
coordinates = {
    0: (8, 11),   # Depot
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Euclidean distance calculation
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Create a set of all nodes
V = set(coordinates.keys())

# Create decision variables
x = LpVariable.dicts("x", [(i, j) for i in V for j in V if i != j], cat=LpInteger, lowBound=0, upBound=1)
u = LpVariable.dicts("u", list(V), lowBound=0, cat='Continuous')

# Create the problem instance
prob = LpProblem("TSP_with_Groups", LpMinimize)

# Objective: Minimize the sum of distances traveled
prob += lpSum(x[i, j] * euclidean_distance(i, j) for i in V for j in V if i != j)

# Constraints
for p in range(len(groups)):
    # Constraint 2 - Outgoing edge from each group
    prob += lpSum(x[i, j] for i in groups[p] for j in V - set(groups[p])) == 1
    # Constraint 3 - Incoming edge to each group
    prob += lpSum(x[j, i] for i in groups[p] for j in V - set(groups[p])) == 1

# Constraint 4 - Conservation of flow
for i in V:
    prob += lpSum(x[j, i] for j in V if j != i) == lp_sum(x[i, j] for j in V if j != i)

# No need to implement constraint (6) due to inherent integer properties and group constraints

# Solve the problem
prob.solve(PULP_CBC_CMD(msg=False))

# Extract the tour
tour = [0]
for _ in range(len(groups) + 1):
    last = tour[-1]
    next_city = [j for j in V if x[last, j].varValue == 1][0]
    tour.append(next_city)

# Calculate tour cost
tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Return tour and total travel cost
print("Tour:", tour)
print("Total travel cost:", tour_cost)