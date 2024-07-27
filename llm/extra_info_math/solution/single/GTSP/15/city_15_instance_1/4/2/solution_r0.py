import pulp
import math

# Coordinates of the cities
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Groups of cities
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Define the problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variable: x_ij = 1 if the path is taken from i to j
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(15) for j in range(15) if i != j], cat="Binary")

# Objective Function
prob += pulp.lpSum([x[i, j] * distance(i, j) for i in range(15) for j in range(15) if i != j]), "Minimize_Total_Distance"

# Constraints
for grp in groups:
    # Outgoing from each group
    prob += pulp.lpSum([x[i, j] for i in grp for j in range(15) if j not in grp]) == 1, f"One_outbound_{grp}"
    # Incoming to each group
    prob += pulp.lpSum([x[j, i] for i in grp for j in range(15) if j not in grp]) == 1, f"One_inbound_{grp}"

# Flow conservation
for k in range(1, 15):
    prob += (pulp.lpSum([x[j, k] for j in range(15) if j != k]) ==
             pulp.lpSum([x[k, i] for i in range(15) if i != k])), f"Flow_conservation_{k}"

prob.solve()

tour = []
visited = [0]
current = 0

# Compute the route by following the decision variables
while True:
    next_city = [j for j in range(15) if pulp.value(x[current, j]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    visited.append(next_city)
    current = next_city
    if current == 0:
        break

total_cost = pulp.value(prob.objective)

# Print output format
print("Tour:", visited)
print("Total travel cost:", total_cost)