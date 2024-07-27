import math
import pulp

# Coordinates of cities including the depot
city_positions = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

city_groups = [
    [7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]
]

# Calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cost matrix between cities
dimension = len(city_positions)
cost_matrix = [[distance(city_positions[i], city_positions[j]) for j in range(dimension)] for i in range(dimension)]

# Problem setting
problem = pulp.LpProblem("Minimize_Travel", pulp.LpMinimize)

x = pulp.LpVariable.dicts("x", [(i, j) for i in range(dimension) for j in range(dimension)], cat=pulp.LpBinary)

# Objective: Minimize the sum of the distances
problem += pulp.lpSum(x[(i, j)] * cost_matrix[i][j] for i in range(dimension) for j in range(dimension))

# Add constraints
# Exactly one city from each group
for group in city_groups:
    problem += pulp.lpSum(x[(0, i)] for i in group) == 1
    problem += pulp.lpSum(x[(i, 0)] for i in group) == 1

# In-degree and Out-degree for all nodes
for i in range(1, dimension):
    problem += pulp.lpSum(x[(i, j)] for j in range(dimension)) == 1
    problem += pulp.lpSum(x[(j, i)] for j in range(dimension)) == 1

# Solve the problem
status = problem.solve()

# Extract the results and calculate distance
tour = []
current = 0
for _ in range(len(city_groups) + 1):  # Plus one for returning to the start
    tour.append(current)
    for j in range(dimension):
        if pulp.value(x[(current, j)]) == 1:
            current = j
            break
tour.append(0)  # Closing the loop back to depot

# Calculate the cost
total_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)