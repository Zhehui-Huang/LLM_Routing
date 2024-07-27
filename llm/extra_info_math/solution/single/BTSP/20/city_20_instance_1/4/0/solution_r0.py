from pulp import *
import math

# ----------------------------
# Step 1: Data Preparation
# ----------------------------

# City coordinates including the depot as city 0
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}
n = len(cities)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
dist = {(i, j): euclidean distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# ----------------------------
# Step 2: Integer Programming Model
# ----------------------------

# Creating the problem
problem = LpProblem("Minimax_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", dist, 0, 1, LpBinary)
d = LpVariable("max_distance", 0)

# Objective Function: Minimize the maximum distance traveled between any two cities
problem += d, "Minimize the maximum distance between any two consecutive cities"

# Constraints
for i in range(n):
    problem += lpSum(x[j, i] for j in range(n) if (j, i) in x) == 1, f"One_incoming_edge_city_{i}"
    problem += lpSum(x[i, j] for j in range(n) if (i, j) in x) == 1, f"One_outgoing_edge_city_{i}"

# Subtour elimination (using Miller-Tucker-Zemlin formulation)
u = LpVariable.dicts("u", range(n), 0, n-1, LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Distance constraints
for (i, j) in dist:
    problem += x[i, j] * dist[i, j] <= d

# ----------------------------
# Step 3: Solve the Problem
# ----------------------------

# Solve the problem using a solver
problem.solve(PULP_CBC_CMD(msg=False))

# ----------------------------
# Step 4: Output Results
# ----------------------------

tour = []
visits = {}
current = 0
while True:
    tour.append(current)
    next_step = [j for j in range(n) if x[current, j].varValue == 1]
    if not next_step:
        break
    current = next_step[0]
tour.append(0)  # return to the depot

# Calculating travel cost and maximum distance
total_cost = sum(dist[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_dist = max(dist[tour[i], tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")