import math
from pulp import LpProblem, LpVariable, LpMinimize, LpBinary, lpSum

# Define the Euclidean distance function
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# City coordinates indexed by city ID
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}
city_groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]
V = [0] + [city for group in city subtour elimination constraints to prevent subtours.
    item for item in group]

# Problem
problem = LpProblem("RobotRouting", LpMinimize)

# Decision variables
x = {}
for i in V:
    for j in V:
        if i != j:
            x[(i, j)] = LpVariable(f"x_{i}_{j}", cat=LpBinary)

# Objective function
problem += lpSum(x[(i, j)] * euclidean_distance(cities[i], cities[j]) for i in V for j in V if i != j)

# Constraints
# Each cluster must be exited exactly once and entered exactly once
for group in city_groups:
    problem += lpSum(x[(i, j)] for i in group for j in V if j not in group) == 1
    problem += lpSum(x[(j, i)] for i in group for j in V if j not in group) == 1

# Flow conservation at each node
for k in V:
    problem += lpSum(x[(i, k)] for i in V if i != k) == lpSum(x[(k, j)] for j in V if j != k)

# Solve the problem
problem.solve()

# Collect results
tour = []
active_edges = [(i, j) for i in V for j in V if i != j and x[(i, j)].varValue > 0.5]
current_city = 0
tour.append(current_city)

# Reconstruct the tour from decision variables
for _ in range(len(active_edges)):
    next_city = next(j for i, j in active_edges if i == current_city)
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Calculate the total travel cost
total_cost = sum(euclidean_distance(cities[i], cities[j]) for i, j in zip(tour[:-1], tour[1:]))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)