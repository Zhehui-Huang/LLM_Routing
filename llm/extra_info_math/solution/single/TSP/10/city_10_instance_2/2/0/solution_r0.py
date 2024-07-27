import pulp
import math
from itertools import combinations

# City coordinates
cities = {
    0: (90, 3),
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

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate the cost dictionary based on coordinates
costs = {(i, j): distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Set up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if route from i to j is chosen
x = pulp.LpVariable.dicts('x', costs, lowBound=0, upBound=1, cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum([x[(i, j)] * costs[(i, j)] for i, j in costs]), "Total Travel Cost"

# Constraints

# Each city is left exactly once
for i in cities:
    prob += pulp.lpSum([x[(i, j)] for j in cities if (i, j) in x]) == 1, f"Leave_city_{i}"

# Each city is entered exactly once
for j in cities:
    prob += pulp.lpSum([x[(i, j)] for i in cities if (i, j) in x]) == 1, f"Enter_city_{j}"

# Subtour elimination constraints
for k in range(2, len(cities)):
    for S in combinations(cities, k):
        prob += pulp.lpSum([x[i, j] for i in S for j in S if (i, j) in x]) <= len(S) - 1

# Solve the problem
status = prob.solve()

# Output the tour and total cost
if status == pulp.LpStatusOptimal:
    print("Tour has been found.")
    tour = []
    total_cost = 0
    for var in x:
        if x[var].value() == 1:
            tour.append(var)
            total_cost += costs[var]

    # Find a way to construct a tour path from binary decision variables
    current_city = 0
    path = [0]

    while len(path) < len(cities):
        for _, next_city in tour:
            if _ == current_city:
                path.append(next_city)
                current_city = next_city
                break

    path.append(0)  # Return to the depot

    print("Tour:", path)
    print("Total travel cost:", total_cost)
else:
    print("Failed to find a valid tour")