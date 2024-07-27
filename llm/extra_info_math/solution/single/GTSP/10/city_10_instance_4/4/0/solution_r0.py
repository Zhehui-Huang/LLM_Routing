from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, LpStatus
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
k = len(city_groups)
for p_idx, group_p in enumerate(city_groups[1:], 2):
    for q_idx, group_q in enumerate(city_groups[1:], 2):
        if p_idx != q_idx:
            model += u[p_idx] - u[q_idx] + k * lpSum(x[i, j] for i in group_p for j in group_q) + \
                     (k - 2) * lpSum(x[i, j] for i in group_q for j in group_p) <= k - 1

# Solving the problem
model.solve()

# Collecting the result
tour = []
visited = [0]
current = 0
while len(visited) < len(city_groups) + 1:
    for j in range(n):
        if x[current, j].varValue == 1:
            tour.append(j)
            visited.append(j)
            current = j
            break
tour.append(0)  # back to the depot

total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)