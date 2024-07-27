from pulp import *
import math

# ----------------------------
# Data Preparation
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
dist = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# ----------------------------
# Integer Programming Model
# ----------------------------

# Problem
problem = LpProblem("Minimax_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", dist.keys(), 0, 1, LpBinary)
d = LpVariable("max_distance", 0)

# Objective Function
problem += d, "Minimize the maximum distance between any two consecutive cities"

# Constraints
# Degree constraints
for i in cities:
    problem += lpSum(x[(i, j)] for j in cities if j != i) == 1, f"Outgoing_from_{i}"
    problem += lpSum(x[(j, i)] for j in cities if j != i) == 1, f"Incoming_to_{i}"

# Subtour elimination (avoid using variables for all pairs of nodes, constraint may require adaptation)
for i in cities:
    for j in cities:
        if i != j and (i != 0 and j != 0) and (i, j) in dist:
            problem += x[(i, j)] * dist[(i, j)] <= d

# Solving the problem
status = problem.solve(PULP_CBC_CMD(msg=True))

# Extracting the results and the tour order
if status == LpStatusOptimal:
    edges = [(i, j) for i, j in x if x[(i, j)].varValue == 1]
    tour = [0]
    while len(tour) < n:
        last = tour[-1]
        next_city = [j for i, j in edges if i == last][0]
        tour.append(next_city)
    tour.append(0)  # Return to the depot
    
    # Calculate tour cost and the largest distance
    total_cost = sum(dist[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    max_dist = max(dist[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist}")
else:
    print("An optimal solution could not be found.")