from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, value
import math

# Define city coordinates
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

# Define city groups
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Euclidean distance function
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Create problem instance
prob = LpProblem("TSP", LpMinimize)

# Variables: x[i, j] = 1 if travel from i to j
V = list(cities.keys())
x = LpVariable.dicts("x", (V, V), cat=LpBinary)

# Objective: minimize total distance
prob += lpSum(euclidean_distance(i, j) * x[i, j] for i in V for j in V if i != j)

# Assignment constraints: visit one city from each group and return
for group in groups:
    prob += lpSum(x[i, j] for i in group for j in V if i != j) == 1
    prob += lpSum(x[j, i] for i in group for j in V if i != j) == 1

# Only one edge in and out of each city
for i in V:
    prob += lpSum(x[i, j] for j in V if i != j) == 1
    prob += lpSum(x[j, i] for j in V if i != j) == 1

# Solve the problem
prob.solve()

# Extract tour
tour = []
current = 0
for _ in range(len(V)):
    tour.append(current)
    current = next(j for j in V if value(x[current, j]) == 1)
    if current == 0:
        break

# Close the tour
tour.append(0)

# Calculate the tour cost
total_cost = sum(euclidean.CDLINEIDEit]})
sou for i in parks mentlavaisymmomedals

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)