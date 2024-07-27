import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

groups = [[1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create LP problem
prob = LpProblem("Minimize_Distance", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), cat=LpBinary)

# Objective function
prob += lpSum(x[(i, j)] * euclidean_distance(coordinates[i], coordinates[j]) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraints for selecting exactly one city from each group
for group in groups:
    prob += lpSum(x[(i, j)] for i in group for j in range(len(coordinates)) if j not in group) == 1
    prob += lpSum(x[(j, i)] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Depot constraints
prob += lpSum(x[(0, j)] for j in range(1, len(coordinates))) == 1
prob += lpSum(x[(j, 0)] for j in range(1, len(coordinates))) == 1

# Solve the problem
prob.solve()

# Extract the solution
tour = [0]
current_city = 0

while len(tour) < len(groups) + 2:
    next_city = None
    for j in range(len(coordinates)):
        if j != current_city and x[(current_city, j)].varValue > 0.9:  # considering float imprecision
            next_city = j
            break
    if next_city is None:
        print("No valid next city found, breaking.")
        break
    tour.append(next_city)
    current_city = next_city

# Output the results
total_distance = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
print("Tour:", tour)
print("Total travel cost:", total_distance)