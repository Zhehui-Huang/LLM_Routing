from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary
import math

# City coordinates
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

# City groups
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

# Variables
V = list(cities.keys())  # Vertex set
A = [(i, j) for i in V for j in V if i != j]  # Arcs

# Problem
prob = LpProblem("Traveling_Salesman_on_Groups", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", A, 0, 1, LpBinary)  # Travel choice

# Objective function
prob += lpSum(euclidean_distance(i, j) * x[(i, j)] for (i, j) in A)

# Constraints
for group in groups:
    prob += lpSum(x[(i, j)] for i in group for j in V if j not in group) == 1  # Constraint (2)
    prob += lpSum(x[(j, i)] for i in group for j in V if j not in group) == 1  # Constraint (3)

# More constraints for subtour elimination
u = LpVariable.dicts("u", V, 1, len(V) - 1)  # Position in tour

for i in V:
    for j in V:
        if i != j and i != 0 and j != 0:  # We do not create constraints for the depot
            prob += u[i] - u[j] + len(V) * x[(i, j)] <= len(V) - 1

# Solving the problem
prob.solve()

# Calculating results
tour = [0]
current_city = 0
while True:
    next_cities = [j for j in V if pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_name)
    current_city = next_city
    if current_city == 0:
        break

# Total travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")