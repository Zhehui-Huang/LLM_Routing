import math
from pulp import *

# City coordinates dictionary from the problem statement
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

n = len(cities)  # Number of cities

# Calculate Euclidean distance between two points
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distances matrix
distances = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the problem variable:
problem = LpProblem("Minimax_TSP", LpMinimize)

# Variables: x_ij
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat="Binary")

# T_max is the maximum travel distance between any two cities - we intend to minimize this
T_max = LpVariable("T_max", lowBound=0, cat='Continuous')

# Objective function
problem += T_max, "Minimized Maximum Leg Distance"

# Constraint: Enter and leave each city exactly once
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Exit_{i}"
    problem += lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

# Linking T_max with x and distances
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distances[i][j] <= T_ub, f"MaxConstraint_{i}_{j}"

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(1, n), s):
        problem += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
problem.solve()

# Fetch the output from the results
tour = []
total_distance = 0
max_distance = 0
if LpStatus[problem.status] == "Optimal":
    for i in range(n):
        for j in range(n):
            if x[i, j].varValue == 1:
                if len(tour) == 0 or tour[-1] != i:
                    tour.append(i)
                tour.append(j)
                total_distance += distances[i][j]
                max_distance = max(max_distance, distances[i][j])

    # The tour will most likely have a repeated cycle, so break it to start and end on depot 0:
    start = tour.index(0)
    cleaned_tour = tour[start:] + tour[:start]

    # Ensuring we finish at the depot
    cleaned_tour = [0] + cleaned_tour[1:] + [0]

    # Output
    print(f"Tour: {cleaned_tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No optimal solution found.")