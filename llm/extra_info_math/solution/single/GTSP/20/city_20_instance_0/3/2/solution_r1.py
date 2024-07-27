import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

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

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in V for j in V if i != j], cat='Binary')
u = LpVariable.dicts("u", list(V), lowBound=0, cat='Continuous')

# Problem definition (minimization)
prob = LpProblem("TSP_Groups", LpMinimize)

# Objective Function
prob += lpSum(x[(i, j)] * euclidean_distance(i, j) for i in V for j in V if i != j)

# Constraints
for p in range(len(groups)):
    prob += lpSum(x[(i, j)] for i in groups[p] for j in V if i != j and j not in groups[p]) == 1
    prob += lpSum(x[(j, i)] for i in groups[p] for j in V if i != j and j not in groups[p]) == 1

for i in V:
    prob += lpSum(x[(j, i)] for j in V if j != i) == lpSum(x[(i, j)] for j in V if j != i)

# Solve the problem
prob.solve(PULT_CBC_CMD(msg=0))
status = LpStatus[prob.status]

# Retrieve solution if optimal
if status == 'Optimal':
    # Reconstruct the tour using the decision variables
    current_location = 0
    tour = [current_location]
    for _ in range(len(groups) + 1):
        next_locations = [j for j in V if j != current_location and x[(current_location, j)].varValue == 1]
        if next_locations:
            next_location = next_locations[0]
            tour.append(next_location)
            current_location = next_location
        else:
            break
    tour.append(0)  # Return to depot

    # Calculate the total cost of the tour
    tour_cost = sum(euclidean.dstiance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", tour_cost)
else:
    print("Failed to find the optimal solution")