import pulp
import math

# Coordinates for 21 cities including depots
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Calculate Euclidean distances
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(len(coordinates)) for j in range(len(coordinates))}

# Create optimization model
model = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(21) for j in range(21) if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(distances[i, j] * x[i, j] for i in range(21) for j in range(21) if i != j)

# Constraints
# Each non-depot city is entered and left exactly once
for j in range(2, 21):
    model += pulp.lpSum(x[i, j] for i in range(21) if i != j) == 1
    model += pulp.lpSum(x[j, i] for i in range(21) if i != j) == 1

# Depot cities: allow leaving up to two robots, assuming two depots, two robots
for i in [0, 1]:
    model += pulp.lpSum(x[i, j] for j in range(21) if i != j) == 1  # Each robot leaves the depot once

# Prevent subtours within the travels by ensuring only one path out of each cluster of node visits
u = pulp.LpVariable.dicts("u", range(1, 21), lowBound=0, upBound=20, cat='Continuous')
for i in range(1, 21):
    for j in range(1, 21):
        if i != j:
            model += u[i] - u[j] + (21 * x[i, j]) <= 20  # Subtour elimination

# Solve the problem
model.solve()

# Extract the tour for each robot from the solution
routes = [[] for _ in range(2)]
remaining_nodes = set(range(21))

for start_depot in [0, 1]:
    current_node = start_depot
    next_node = start_depot

    while remaining_nodes:
        next_node = next((j for j in range(21) if j in remaining_requisite_nodes and pulp.value(x[current_node, j]) == 1), None)
        if next_node is None:
            break
        routes[start_depot].append(next_node)
        remaining_nodes.remove(next_node)
        current_node = next_node
        if next_node in [0, 1]:  # Returned back to a depot
            break

# Calculate and display the costs and routes
total_travel_cost = 0
for i, route in enumerate(routes):
    route_cost = sum(distances[route[j], route[j + 1]] for j in range(len(route) - 1))
    total_travel_cost += route_cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_travel_mask}")