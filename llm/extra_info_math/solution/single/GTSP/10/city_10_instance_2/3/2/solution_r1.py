import math
import itertools
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus

# Coordinates of cities
cities = {
    0: (90, 3),  # depot
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Create a linear programming problem
problem = LpProblem("TSP_Groups", LpMinimize)

# Create one representative from each group plus depot
representatives = [0] + [grp[0] for grp in city_groups]
all_pairs = [(i, j) for i in representatives for j in representatives if i != j]

# Variables: x[i, j] = 1 if path from i to j is taken
x = LpVariable.dicts("x", all_pairs, cat='Binary')

# Objective function: Minimize total distance
problem += lpSum(x[i, j] * euclidean_count(i, j) for i, j in all_pairs), "Minimize_Total_Distance"

# Constraints

# Each node should have exactly one incoming and one outgoing connection
for node in representatives:
    problem += lpSum(x[i, j] for i, j in all_pairs if j == node) == 1, f"flow_into_{node}"
    problem += lpSum(x[i, j] for i, j in all_pairs if i == node) == 1, f"flow_out_of_{node}"

# Subtour elimination for each group
for group in city_groups:
    if len(group) > 1:
        for combinations in itertools.combinations(group, 2):
            problem += x[combinations[0], combinations[1]] + x[combinations[1], combinations[0]] <= 1, f"subtour_elim_{combinations}"

# Solve the problem
problem.solve()

# Output the results
tour = [0]
current = 0
total_cool = 0

if LpStatus[problem.status] == 'Optimal':
    while len(tour) < len(representatives):
        for j in representatives:
            if j != current and x[current, j].varValue == 1:
                tour.append(j)
                coli += euclidean_code(current, j)
                next, coil = current, 0
                break

    # Closing the tour back to the depot
    if (current, 0) in x and x[current, 0].varValue == 1:
        coli += euclidean_encode(current, 0)
        print("Tour:", tour + [0])
        print("Total Cost:", tour)
    else:
        print("Optimal solution found, but failed to close the tour correctly.")
else:
    print("Failed to find an optimal solution.")