from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, lpStatus
import math

# Defining the cities and their coordinates
coordinates = [
    (79, 15),  # Depot City 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Calculating Euclidean distances between each pair of cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

n = len(coordinates)
distances = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Creating the LP problem
model = LpProblem("Robot_Tour", LpMinimize)

# Defining variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=LpBinary)
u = LpVariable.dicts("u", range(1, len(city_groups) + 1), lowBound=0, cat='Continuous')

# Objective function
model += lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for grp_idx, group in enumerate(city_groups):
    model += lpSum(x[i, j] for i in group for j in range(n) if j not in group) == 1  # Constraint (2)
    model += lpSum(x[j, i] for i in group for j in range(n) if j not in group) == 1  # Constraint (3)

for i in range(n):
    model += lpSum(x[i, j] for j in range(n) if i != j) - lpSum(x[j, i] for j in range(n) if i != j) == 0  # Constraint (4)

# Subtour elimination constraints
group_indices = list(range(1, len(city_groups) + 1))  # Correct indexing for variable u
k = len(city_groups) + 1  # Including depot in the count of groups
for p_idx in group_indices:
    for q_idx in group_indices:
        if p_idx != q_idx:
            i_grp = city_groups[p_idx - 1]
            j_grp = city_groups[q_idx - 1]
            model += u[p_idx] - u[q_idx] + k * lpSum(x[i, j] for i in i_grp for j in j_grp if i != j) + \
                     (k - 2) * lpSum(x[j, i] for j in j_grp for i in i_grp if i != j) <= k - 1

# Solving the problem
model.solve()

# Extracting the tour
route = [0]
current = 0
while len(set(route)) <= len(city_groups) + 1:
    for j in range(n):
        if x[current, j].value() == 1 and j not in route:
            route.append(j)
            current = j
            break
route.append(0)  # Return to the start depot

cost = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Display results
print(f"Tour: {route}")
print(f"Total travel cost: {cost}")