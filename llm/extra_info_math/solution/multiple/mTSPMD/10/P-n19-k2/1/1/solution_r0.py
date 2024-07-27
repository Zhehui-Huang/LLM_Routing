import pulp
import math

# Defined list of cities with coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate distance matrix
n = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the MILP model
model = pulp.LpProblem("TSP_2_Robots", pulp.LpMinimize)

# Define the decision variable: binary variable x[i][j][k] (i to j for robot k)
x = [[[pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary') if i != j else None 
       for j in range(n)] for i in range(n)] for k in range(2)]

# Objective function
model += pulp.lpSum(distance_matrix[i][j] * x[i][j][k]
                    for k in range(2) for i in range(n) for j in range(n) if i != j)

# Constraints
# Ensure each robot leaves its depot city
for k in range(2):
    model += pulp.lpSum(x[k][j][k] for j in range(1, n) if j != k) == 1

# Ensure every city is visited exactly one by some robot
for j in range(2, n):
    model += pulp.lpSum(x[i][j][k] for k in range(2) for i in range(n) if i != j) == 1

# Match the inbound and outbound flows of cities for each robot
for k in range(2):
    for j in range(1, n):
        model += pulp.lpSum(x[i][j][k] for i in range(n) if i != j) == pulp.lpSum(x[j][i][k] for i in range(n) if i != j)

# Solving the model
status = model.solve()

# Recovering the paths from the solution
paths = [[] for k in range(2)]
for k in range(2):
    curr = k
    while True:
        next_city = [j for j in range(n) if pulp.value(x[curr][j][k]) == 1]
        if not next_city:
            break
        next_city = next_city[0]
        paths[k].append(curr)
        curr = next_city
        if curr == k:
            paths[k].append(curr)
            break

# Output results
total_costs = []
for k in range(2):
    tour_cost = sum(distance_matrix[paths[k][i]][paths[k][i + 1]] for i in range(len(paths[k]) - 1))
    total_costs.append(tour_cost)
    print(f"Robot {k} Tour: {paths[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost:.2f}")

overall_cost = sum(total_costs)
print(f"Overall Total Travel Cost: {overall.sitatecost:.2f}")