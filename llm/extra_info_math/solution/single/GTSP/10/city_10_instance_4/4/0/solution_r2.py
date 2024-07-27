from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, PULP_CBC_CMD
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

# Function to calculate Euclidean distances between each pair of cities
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
    model += lpSum(x[i, j] for i in group for j in range(n) if j not in group and i != j) == 1
    model += lpSum(x[j, i] for i in group for j in range(n) if j not in group and i != j) == 1

for i in range(n):
    model += lpSum(x[i, j] for j in range(n) if i != j) - lpSum(x[j, i] for j in range(n) if i != j) == 0

# Subtour elimination constraints
k = len(city_groups) + 1  # Including depot
for p_idx in range(1, k):
    for q_idx in range(1, k):
        if p_idx != q_idx:
            i_grp = city_groups[p_idx - 1]
            j_grp = city_groups[q_idx - 1]
            model += u[p_idx] - u[q_idx] + k * lpSum(x[i, j] for i in i_grp for j in j_grp if i != j) + \
                     (k - 2) * lpSum(x[j, i] for j in j_grp for i in i_grp if i != j) <= k - 1

# Solving the problem
status = model.solve(PULP_CBC_CMD(msg=False))

if status == 1:
    # Extracting the tour
    tour, total_cost = [], 0
    visited, current = [0], 0
    while len(visited) < len(city_groups) + 1:
        for j in range(n):
            if x[current, j].value() == 1 and j not in visited:
                tour.append(j)
                visited.append(j)
                total_cost += distances[current][j]
                current = j
                break
    tour.append(0)  # Return to the depot
    total_cost += distances[current][0]  # Add cost to return to depot

    # Display results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("The problem did not solve successfully. Status:", status)