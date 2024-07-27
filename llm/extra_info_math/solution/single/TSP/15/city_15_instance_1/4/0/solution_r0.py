import math
from pulp import LpProblem, LpVariable, LpMinimize, LpBinary

# Calculate Euclidean distance between two points
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# City coordinates
coordinates = [
    (29, 51),  # Depot city 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

n = len(coordinates)  # number of cities including depot
cost = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the optimization problem
prob = LpProblem("TSP", LpMinimize)

# Decision variables
x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in range(n)] for i in range(n)]

# Objective function
prob += lpSum(cost[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += lpSum(x[i][j] for j in range(n) if i != j) == 1  # leave city i exactly once
    prob += lpSum(x[j][i] for j in range(n) if i != j) == 1  # enter city i exactly once

# Solve the problem
prob.solve()

# Extract the solution
solution = []
current_city = 0
visited = set()
tour_cost = 0

while True:
    visited.add(current_city)
    for next_city in range(n):
        if x[current_city][next_city].varValue == 1:
            solution.append(current_city)
            tour_cost += cost[current_city][next_city]
            current_city = next_city
            break
    if current_city == 0:
        break

solution.append(0)  # end at the depot city

print("Tour:", solution)
print("Total travel cost:", tour_cost)