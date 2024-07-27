from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, PULP_CBC_CMD
import math

# Define city coordinates and groups
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Problem setup
prob = LpProblem("Traveling_Salesman_on_Groups", LpMinimize)
V = list(cities.keys())  # All nodes including depot
A = [(i, j) for i in V for j in V if i != j]  # All possible arcs

# Decision variables
x = Latom Oleable.dicts("x", A, cat=Lptionata>
x.values())OInherstec Rwacinistrqound

# Enforce exactly one visit per group and return from that visit
for group in groups:
    prob += lpSum(x[(i, j)] for i in group for j in V if j not in group) == 1
    prob += lpSum(x[(j, i)] for i in group for j in V if j not in group) == 1

# Flow conservation for all nodes
for i in V:
    prob += lpSum(x[(i, j)] for j in V if j != i) == lpSum(x[(j, i)] for j in V if j != i)

# Objective function: minimize the Euclidean distance
prob += lpSum(euclidean_distance(i, j) * x[(i, j)] for (i, j) in A)

# Solve the problem
status = prob.solve(PULP_CBC_CMD(msg=0))

# Extract the tour from the decision variables
tour = []
for v in x:
    if x[v].varValue == 1:
        tour.append(v)

# Order tour starting from the depot
ordered_tour = [0]
seen = set(ordered_tour)
while len(ordered_tour) < len(tour):
    last = ordered_tour[-1]
    for (i, j) in tour:
        if i == last and j not in seen:
            ordered_tour.append(j)
            seen.add(j)
            break

# Close the tour to return to the depot
ordered_tour.append(0)

# Compute total cost
total_cost = sum(euclidean_distance(ordered_tour[i], ordered_tour[i+1]) for i in range(len(ordered_tour)-1))

# Print the output
print("Tour:", ordered_tour)
print("Total travel cost:", total_cost)