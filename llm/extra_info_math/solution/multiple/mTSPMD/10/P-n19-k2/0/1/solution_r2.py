import pulp
import math

# Setup the coordinate data
coords = {
    0: (30, 40),   # Depot for Robot 0
    1: (37, 52),   # Depot for Robot 1
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35),
}

# Distance function using Euclidean distance
def distance(city1, city2):
    return math.sqrt((coords[city1][0] - coords[city2][0]) ** 2 + (coords[city1][1] - coords[city2][1]) ** 2)

# Constants
num_cities = len(coords)
depots = {0: 0, 1: 1}
cities = list(set(range(num_cities)) - set(depots.values()))

# Declare the problem
problem = pulp.LpProblem("Multi-depot Vehicle Routing Problem", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for k in depots for i in range(num_cities) for j in range(num_cities) if i != j], cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", [(i, k) for i in range(num_cities) for k in depots], lowBound=0, cat=pulp.LpInteger)

# Objective function
problem += pulp.lpSum(distance(i, j) * x[i, j, k] for k in depots for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Each city is visited exactly once
for j in cities:
    problem += pulp.lpSum(x[i, j, k] for k in depots for i in range(num_cities) if i != j) == 1

# Each robot returns to its starting depot and route continuity
for k in depots:
    problem += pulp.lpSum(x[depots[k], j, k] for j in range(num_cities) if j != depots[k]) == 1
    problem += pulp.lpSum(x[j, depots[k], k] for j in range(num_cities) if j != depots[k]) == 1
    for i in range(num_cities):
        if i != depots[k]:
            problem += pulp.lpSum(x[i, j, k] for j in range(num_cities) if j != i) == pulp.lpSum(x[j, i, k] for j in range(num_cities) if j != i)

# Subtour Elimination
for k in depots:
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j and i != depots[k] and j != depots[k]:
                problem += u[i, k] - u[j, k] + (num_cities - 1) * x[i, j, k] <= num_cities - 2

# Solve the problem
problem.solve()

# Outputting the solution
for k in depots:
    current_location = depots[k]
    route = [current_location]
    while True:
        next_cities = [j for j in range(num_cities) if pulp.value(x[current_location, j, k]) == 1]
        if not next_cities:
            break
        next_location = next_cities[0]
        route.append(next_location)
        current_location = next_location
        if current_location == depots[k]:
            break
    
    route_cost = sum(distance(route[i], route[i+1]) for i in range(len(route)-1))
    print(f"Robot {k} Tour: {route}")
    print(f"Robot {t} Total Travel Cost: {route_cost}")

overall_cost = sum(distance(i, j) * pulp.value(x[i, j, k]) for k in depots for i in range(num_cities) for j in range(num_cities) if i != j)
print(f"Overall Total Travel Cost: {overall_cost}")