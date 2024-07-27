import math
import pulp

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Define the number of robots (vehicles)
m = 8

# Coordinates for the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
n = len(coordinates)

# Set problem
prob = pulp.LpProblem("Multiple_TSP_Problem", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], cat='Binary')

# Objective
prob += pulp.lpSum(x[(i, j, k)] * euivclidian_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
for j in range(1, n):
    prob += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(m) if i != j) == 1

for k in range(m):
    prob += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[(j, 0, k)] for j in range(1, n)) == 1

    for i in range(1, n):
        prob += pulp.lpSum(x[(i, j, k)] for j in range(n) if i != j) - pulp.lpSum(x[(j, i, k)] for j in range(n) if i != j) == 0

# Solve the problem
status = prob.solve()

# Output results
if status == pulp.LpStatusOptimal:
    print("Optimal solution found.")
    for k in range(m):
        route = [0]
        for i in range(n):
            next_city = [j for j in range(n) if pulp.value(x[(route[-1], j, k)]) == 1]
            if next_city:
                route.extend(next_city)
        route.append(0)  # Return to depot
  
        # Calculate the cost of the route
        route_cost = sum(euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]]) for i in range(len(route) - 1))
        print(f"Robot {k} Tour: {route}")
        print(f"Robot {k} Total Travel Cost: {route_cost}")
else:
    print("Optimal solution not found. Status:", pulp.LpStatus[status])