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

# Define groups of cities
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Calculate Euclidean distance between each pair of cities
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance cost matrix
cost = {(i, j): calculate_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Problem setup
prob = lp.LpProblem("Minimize_Tour_Cost", lp.LpMinimize)

# Variables
x = lp.LpVariable.dicts("x", cost.keys(), cat=lp.LpBinary)

# Objective
prob += lp.lpSum([cost[i, j] * x[i, j] for i, j in cost])

# Constraints from groups
for group in city_groups:
    prob += lp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    prob += lp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

# Flow conservation
for i in cities:
     prob += lp.lpSum(x[j, i] for j in cities if j != i and (j, i) in x) == lp.lpSum(x[i, j] for j in cities if j != i and (i, j) in x), f"flow_conservation_{i}"

# Solve the problem
prob.solve()

# Check the solution and extract the tour
if prob.status == lp.LpStatusOptimal:
    optimal_path = []
    current_city = 0
    while True:
        next_cities = [j for j in cities if j != current_city and lp.value(x[current_city, j]) == 1]
        if not next_cities:
            optimal_path.append(current_city)
            break
        next_city = next_cities[0]
        optimal_path.append(current_city)
        current_city = next_city
        if current_city == 0:
            break

    # Calculate total travel cost
    travel_cost = sum(cost[optimal_path[i], optimal_path[i + 1]] for i in range(len(optimal_path) - 1))

    # Output results
    print("Tour:", optimal_path)
    print("Total travel cost:", travel_cost)
else:
    print("Failed to find an optimal solution.")