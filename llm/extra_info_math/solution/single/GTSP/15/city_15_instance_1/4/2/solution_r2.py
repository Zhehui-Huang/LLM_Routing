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

# Create the problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(15) for j in range(15) if i != j], cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(distance(i, j) * x[i, j] for i in range(15) for j in range(15) if i != j)

# Constraints
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in range(15) if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in range(15) if j not in group) == 1

# Flow conservation
for node in range(1, 15):
    prob += pulp.lpSum(x[j, node] for j in range(15) if j != node) == 1
    prob += pulp.lpSum(x[node, j] for j in range(15) if j != node) == 1

# Solve the problem
status = prob.solve()

# Check and extract the route
if pulp.LpStatus[status] == 'Optimal':
    route = [0]
    while len(route) < 5:
        for j in range(15):
            if x[route[-1], j].varValue == 1:
                route.append(j)
                break
    route.append(0)  # return to the depot

    # Calculate the total distance of the route
    total_distance = sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))

    # Output result
    print("Tour:", route)
    print("Total travel cost:", total_distance)
else:
    print("No optimal solution found")