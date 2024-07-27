import pulp
import math

# Coordinates of the cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Create all-to-all distance matrix
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(21) for j in range(21)}

# Create the problem
problem = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision variables: x[i, j] is 1 if travel from i to j occurs
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(21) for j in range(21)), cat='Binary')

# Objective: Minimize the total distance
problem += pulp.lpSum(x[i, j] * distances[i, j] for i in range(21) for j in range(21))

# Constraints
# Each city must be left exactly once
for j in range(21):
    problem += pulp.lpSum(x[i, j] for i in range(21)) == 1

# Each city must be entered exactly once
for i in range(21):
    problem += pulp.lpSum(x[i, j] for j in range(21)) == 1

# No self loops
for i in range(21):
    x[i, i].setInitialValue(0)
    x[i, i].fixValue()

# Each robot must start from a depot
# Just assign one robot per depot for simplicity in this case
problem += pulp.lpSum(x[0, j] for j in range(1, 21)) == 1
problem += pulp.lpSum(x[1, j] for j in range(21) if j != 1) == 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Check if a feasible solution was found
if status != pulp.LpStatusOptimal:
    print("No optimal solution found.")
else:
    # Output the routes
    total_cost = 0
    for start_node in [0, 1]:
        node = start_node
        route = [node]
        while True:
            next_nodes = [j for j in range(21) if pulp.value(x[node, j]) == 1]
            if not next_nodes:
                break
            node = next_nodes[0]
            route.append(node)
            if node in [0, 1]:
                break
        route_cost = sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1))
        total_cost += route_cost
        print(f"Robot {start_node} Tour: {route}")
        print(f"Robot {start_node} Total Travel Cost: {route_cost}")

    print(f"Overall Total Travel Cost: {total_cost}")