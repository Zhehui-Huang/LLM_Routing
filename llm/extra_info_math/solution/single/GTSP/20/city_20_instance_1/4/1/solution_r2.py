import pulp
import math

# City coordinates
coordinates = [
    (14, 77),  # Depot city
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# City groups
city_groups = [
    [5, 6, 7, 11, 17],  # Group 0
    [1, 4, 8, 13, 16],  # Group 1
    [2, 10, 15, 18, 19],# Group 2
    [3, 9, 12, 14]      # Group 3
]

# Euclidean distance function
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

n = len(coordinates)
model = pulp.LpProblem("MinCostPath", pulp.LpMinimize)

# Decision variable, x[i, j] = 1 if the path is travelled from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')

# Objective function: Minimize the sum of the distances
model += pulp.lpSum(x[(i, j)] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Each group must be visited exactly once
for group in city_groups:
    model += pulp.lpSum(x[(0, j)] for j in group) == 1

# Flow conservation at intermediate cities
for j in range(1, n):
    model += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == pulp.lpSum(x[(j, k)] for k in range(n) if j != k)

# Returning to the depot
model += pulp.lpSum(x[(j, 0)] for j in range(1, n)) == len(city_groups)

# Subtour elimination
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1) * x[(i, j)] <= n-2

# Solve the problem
model.solve()

# Analyze the results
if model.status == 1:  # 1 means the optimization succeeded
    path = []
    cur_location = 0
    path.append(cur_location)
    for _ in range(len(city_groups)):  # since we should visit one city from each group only
        next_moves = [j for j in range(n) if x[cur_location, j].varValue == 1]
        if not next_moves:
            break
        next_location = next_moves[0]
        path.append(next_location)
        cur_location = next_location
    path.append(0)  # to return to depot

    total_cost = sum(distance(path[i], path[i+1]) for i in range(len(path) - 1))

    print(f"Tour: {path}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")