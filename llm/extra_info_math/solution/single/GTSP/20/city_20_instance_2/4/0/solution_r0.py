import pulp as lp
import math

# Define city coordinates including the depot
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Groups of cities
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Number of groupings and total number of cities
k = len(city_groups) + 1  # +1 for including the depot separately
n = len(cities)

# Calculate Euclidean distance between each pair of cities
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cost matrix
cost = {(i, j): calculate_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Define the problem
prob = lp.LpProblem("RobotTour", lp.LpMinimize)

# Variables x_ij
x = lp.LpVariable.dicts("x", cost.keys(), cat=lp.LpBinary)

# Objective function
prob += lp.lpSum([cost[i, j] * x[i, j] for i, j in cost]), "Minimize Total Travel Cost"

# Constraints
for p, group in enumerate(city_groups, start=1):
    sub_vertices = group
    other_vertices = [i for i in cities if i not in sub_vertices]
    # Constraint (2) and (3)
    prob += lp.lpSum(x[i, j] for i in sub_vertices for j in other_vertices) == 1, f"One outgoing edge from group {p}"
    prob += lp.lpSum(x[j, i] for i in sub_vertices for j in other_vertices) == 1, f"One incoming edge to group {p}"

# Constraint (4) - Flow conservation constraint
for i in cities:
    incoming = [x[j, i] for j in cities if i != j and (j, i) in x]
    outgoing = [x[i, j] for j in cities if i != j and (i, j) in x]
    prob += lp.lpSum(incoming) == lp.lpSum(outgoing), f"Flow conservation at city {i}"

# Solve the problem
prob.solve()

# Extract the tour and calculate the cost
tour = []
visited = set()
current = 0

while True:
    tour.append(current)
    visited.add(current)
    next_cities = [j for j in cities if j != current and x[current, j].varValue == 1]
    if not next_cities:
        break
    current = next_cities[0]

tour.append(0)  # return to depot
tour_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", tour_cost)