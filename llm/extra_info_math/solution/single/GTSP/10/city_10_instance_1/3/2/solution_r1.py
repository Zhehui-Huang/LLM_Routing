import pulp
import math

# City positions indexed from 0 to 9
positions = [
    (53, 68), (75, 11), (91, 95), (22, 80),
    (18, 63), (54, 91), (70, 14), (97, 44),
    (17, 69), (95, 89)
]

# Groups of cities (excluding depot)
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Calculate Euclidean distances
def calc_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Total number of cities (including the depot)
n = len(positions)

# Distance matrix
distances = [[calc_slope(positions[i], positions[j]) for j in range(n)] for i in range(n)]

# Setting up the problem
model = pulp.LpProblem("Robot_Tour_Problem", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective
model += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints

# Each group has exactly one edge leaving it and one edge entering it
for group in groups:
    model += pulp.lpSum(x[i, j] for i in group for j in set(range(n)) - set(group)) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in set(range(n)) - set(group)) == 1

# Flow conservation at each node (it must relate to other than itself)
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) - pulp.lpSum(x[j, i] for j in range(n) if i != j) == 0

# Solve the model
status = model.solve()

# Verify and extract the solution
if status == pulp.LpStatusOptimal:
    # Finding which variables are set to 1 (=used in the solution)
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]

    # Recovering the path from the edges
    visited = [0]  # start from depot
    while len(visited) - 1 < len(groups):
        for e in edges:
            if e[0] == visited[-1] and e[1] not in visited:
                visited.append(e[1])
                break
    visited.append(0)  # return to depot

    # Calculate the total travel cost
    total_cost = sum(distances[visited[i]][visited[i + 1]] for i in range(len(visited) - 1))

    print(f"Tour: {visited}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")