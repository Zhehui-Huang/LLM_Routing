import pulp
import math

# Define the locations of the 20 cities including the depot (city 0)
locations = [
    (8, 11),   # Depot city 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Group assignment
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Euclidean distance formula
def calculate_distance(city1, city2):
    x1, y1 = locations[city1]
    x2, y2 = locations[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create the LP problem object.
problem = pulp.LpProblem("Minimize_Route_Cost", pulp.LpMinimize)

# Define decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(20) for j in range(20) if i != j], cat='Binary')

# Objective Function: Minimize the sum of distances for all possible paths
objective_function = pulp.lpSum([calculate_distance(i, j) * x[(i, j)] for i in range(20) for j in range(20) if i != j])
problem += objective_function

# Each group should have exactly one outgoing and incoming connection to another city
for g in groups:
    problem += pulp.lpSum(x[(i, j)] for i in g for j in range(20) if j not in g and i != j) == 1, f"One_outgoing_from_group_{groups.index(g)}"
    problem += pulp.lpSum(x[(j, i)] for i in g for j in range(20) if j not in g and i != j) == 1, f"One_incoming_to_group_{groups.index(g)}"

# All cities must have one incoming and one outgoing connection
for city in range(20):
    problem += pulp.lpSum(x[(i, city)] for i in range(20) if i != city) == 1, f"Incoming_to_{city}"
    problem += pulp.lpSum(x[(city, j)] for j in range(20) if j != city) == 1, f"Outgoing_from_{city}"

# Solve the problem using a solver
solver = pulp.PULP_CBC_CMD(msg=0)
status = problem.solve(solver)

# Retrieving the optimal route
route = []
current_city = 0
while len(route) < 20:
    for j in range(20):
        if j != current_city and pulp.value(x[(current_city, j)]) == 1:
            route.append(j)
            current_city = j
            break
    if current_city == 0:
        break

# Adding the start city at end to complete the cycle for visualization clarity
route.insert(0, 0)

# Calculate the route cost
route_cost = sum(calculateable_distance_from_route[i, route[i + 1]]) for i in range(len(route) - 1))
print(f"Tour: {route}")
print(f"Total travel cost: {route_cost}")