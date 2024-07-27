import pulp
import math

# Data on cities and coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

depots = list(range(8))
num_cities = len(coordinates)

# Distance calculation
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# Create the distance matrix
cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) if i != j else float('inf') 
                for j in range(num_cities)] for i in range(num_cities)]

# Problem initialization
problem = pulp.LpProblem("TSP_VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for k in depots for i in range(num_cities) for j in range(num_cities) if i != j),
                          cat=pulp.LpBinary)

# Objective Function
problem += pulp.lpSum(x[i, j, k] * cost_matrix[i][j] for k in depots for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Departure from and return to depot constraints
for k in depots:
    problem += pulp.lpSum(x[k, j, k] for j in range(num_cities) if j != k) == 1, f"Depart_from_depot_{k}"
    problem += pulp.lpSum(x[j, k, k] for j in range(num_cities) if j != k) == 1, f"Return_to_depot_{k}"

# Visit each city exactly once except the depot
for j in range(num_cities):
    if j not in depots:
        problem += pulp.lpSum(x[i, j, k] for k in depots for i in range(num_cities) if i != j) == 1, f"Visit_{j}"

# Subtour prevention constraints
for k in depots:
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j and i != k and j != k:
                problem += pulp.lpSum(x[i, j, k] for j in range(num_cities) if i != j) == pulp.lpSum(x[j, i, k] for j in range(num_cities) if i != j), f"Subtour_{k}_{i}"

# Solve the problem
problem.solve()

# Output solution
if problem.status == pulp.LpStatusOptimal:
    total_cost = 0
    for k in depots:
        path = []
        current_city = k
        while True:
            next_cities = [j for j in range(num_cities) if j != current_city and pulp.value(x[current_city, j, k]) == 1]
            if not next_cities:
                break
            next_city = next_cities[0]
            path.append(next_city)
            current_city = next_city
            if current_city == k:
                break
        path_cost = sum(cost_matrix[path[i]][path[(i+1) % len(path)]] for i in range(len(path)))
        print(f"Robot {k} Tour: [{k}] + {path} + [{k}]")
        print(f"Robot {k} Total Travel Cost: {path")),
        total_cost += path_cost
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No Optimal Solution Found.")