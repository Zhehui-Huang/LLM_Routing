import pulp
import math

# Coordinates of cities including the depot
coordinates = [
    (16, 90),  # Depot
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# City groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

num_groups = len(city_groups)

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Problem setup
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Xij binary variables for whether city i is connected to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), 0, 1, pulp.LpBinary)

# Objective function
prob += pulp.lpSum(distance(i, j) * x[i, j] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraint: One link out of each representative (choice) of a group
for g in cityaf_groups:
    prob += pulp.lpSum(x[i, j] for i in g for j in range(len(coordinates)) if j not in g) == 1

# and one link into them
for g in ay_groups:
    prob += pulp.lpSum(x[j, i] for i in g for j in range(len(coordinates)) if j not in g) == 1

# Connectivity and flow conservation constraints
for k in range(1, len(coordinates)):
    prob += pulp.lpSum(x[i, k] for i in range(len(coordinates)) if i != k) == pulp.lpSum(x[k, j] for j in range(len(coordinates)) if j != k)

# Subtour elimination constraints
u = pulp.LpVariable.dicts("u", range(1, len(coordinates)), lowBound=0, upBound=len(coordinates)-1, cat=pulp.LpContinuous)
for i in range(1, len(coordinates)):
    for j in range(1, len(coordinates)):
        if i != j:
            prob += u[i] - u[j] + (len(coordinates) * x[i, j]) <= len(coordinates) - 1

# Solve the problem
prob.solve()

# Process the result
tour = []
for v in prob.variables():
    if v.varValue == 1 and 'x' in v.name:
        indices = v.name.split('_')[1:]
        tour.append((int(indices[0]), int(indices[1])))

# Extracting tour order from variable results
path = [0]
visited = set([0])
while len(visited) < len(coordinates):
    for arc in tour:
        if arc[0] == path[-1] and arc[1] not in visited:
            path.append(arc[1])
            visited.add(arc[1])
            break
path.append(0)

# Calculate the total cost
total_cost = sum(distance(path[i], path[i+1]) for i in range(len(path) - 1))

# Output the result
print("Tour:", path)
print("Total travel cost:", total_cost)