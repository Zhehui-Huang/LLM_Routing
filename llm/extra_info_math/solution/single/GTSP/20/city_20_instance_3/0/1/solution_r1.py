import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, PULP_CBC_CMD

# City coordinates
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Groups
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], 
    [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Calculate Euclidean distance
def distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

n = len(coordinates)
all_cities = range(n)

# Create the LP model
model = LpProblem("TSP_Groups", LpMinimize)

# Decision variables: x[i, j] where city i is followed by city j
x = LpVariable.dicts("x", [(i, j) for i in all_cities for j in all_cities if i != j], cat=LpBinary)

# Objective function: Minimize the distance
model += lpSum(x[i, j] * distance(i, j) for i in all_cities for j in all_cities if i != j)

# Constraints to ensure one outgoing and one incoming connection for each city in a group
for group in groups:
    model += lpSum(x[i, j] for i in group for j in all_cities if j not in group) == 1
    model += lpSum(x[j, i] for i in group for j in all_cities if j not in group) == 1

# Flow balance at each city to form a tour
for city in all_cities:
    model += lpSum(x[city, j] for j in all_cities if city != j) == lpSum(x[j, city] for j in all_cities if city != j)

# Solve the model
model.solve(PULP_CBC_CMD(msg=False))

# Extract the solution
path = [0]  # start from depot
visited = set(path)

while len(path) < len(groups) + 1:
    for j in all_cities:
        if x[path[-1], j].varValue > 0.99 and j not path[-1] and j not in visited:
            path.append(j)
            visited.add(j)
            break
path.append(0)  # return to the depot

total_cost = sum(distance(path[i], path[i+1]) for i in range(len(path) - 1))

# Output the results
print("Tour:", path)
print("Total travel cost:", total_cost)