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
distances = [[calc_distance(positions[i], positions[j]) for j in range(n)] for i in range(n)]

# Setting up the problem
model = pulp.LpProblem("Robot_Tour_Problem", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective
model += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each group has exactly one edge leaving and one entering
for grp in groups:
    model += pulp.lpSum(x[i, j] for i in grp for j in range(n) if j not in grp) == 1
    model += pulp.lpSum(x[j, i] for i in grp for j in range(n) if j not in grp) == 1

# Flow conservation
for k in range(n):
    model += pulp.lpSum(x[i][k] for i in range(n) if i != k) == pulp.lpSum(x[k][j] for j in range(n) if k != j)

# Solve the model
model.solve()

# Check if the model has found an optimal solution
if pulp.LpStatus[model.status] == 'Optimal':
    paths = [(i, j) for i in range(n) for j in range(n) if i != j and x[i][j].value() == 1]
    tour = [0]  # start from depot
    while len(tour) < len(groups) + 1:
        for i, j in paths:
            if i == tour[-1] and j not in tour:
                tour.append(j)
                break
    tour.append(0) #return to depot

    # Calculate the travel cost
    cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", f"{cost:.2f}")
else:
    print("Could not find an optimal solution.")