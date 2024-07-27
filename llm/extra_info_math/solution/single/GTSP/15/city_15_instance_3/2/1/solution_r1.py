import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Groups
groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Initialize the problem
prob = LpProblem("TSP_Groups", LpMinimize)

# Total number of cities
n_cities = len(coordinates)

# Create decision variables
x = LpVariable.dicts("x", ((i, j) for i in range(n_cities) for j in range(n_cities) if i != j), cat='Binary')

# Objective function
prob += lpSum(x[i, j] * math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)
              for i in range(n_cities) for j in range(n_cities) if i != j)

# Each cluster must have exactly one connection to and from non-cluster nodes
for group in groups:
    prob += lpSum(x[i, j] for i in group for j in range(n_cities) if j not in group) == 1, f"out_from_group_{group}"
    prob += lpSum(x[j, i] for i in group for j in range(n_cities) if j not in group) == 1, f"in_to_group_{group}"

# Flow conservation
for i in range(n_cities):
    prob += (lpSum(x[i, j] for j in range(n_cities) if j != i) 
             - lpSum(x[j, i] for j in range(n_cities) if j != i) == 0, f"flow_{i}")
    
# Solve the problem
prob.solve()

# Output the tour
tour = []
visited = [0]
current = 0

while len(visited) < len(groups) + 1:
    for j in range(n_cities):
        if x[current, j].varValue == 1:
            tour.append(j)
            visited.append(j)
            current = j
            break

tour.append(0)  # to return to the depot
total_cost = sum(math.sqrt((coordinates[tour[i]][0] - coordinates[tour[i + 1]][0]) ** 2 + (coordinates[tour[i]][1] - coordinates[tour[i + 1]][1]) ** 2)
                 for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")