from pulp import *
import math

# City coordinates
coordinates = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84), 6: (4, 56), 7: (54, 82),
    8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Groups of cities
groups = {
    0: [0],  # Depot
    1: [5, 6, 7, 11, 17],
    2: [1, 4, 8, 13, 16],
    3: [2, 10, 15, 18, 19],
    4: [3, 9, 12, 14]
}

# Distance function
def distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Create the problem
prob = LpProblem("Minimize_Route", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in coordinates for j in coordinates if i != j), cat='Binary')
u = LpVariable.dicts("u", (i for i in coordinates), lowBound=1, upBound=len(coordinates), cat='Continuous')

# Objective
prob += lpSum(distance(i, j) * x[i, j] for i in coordinates for j in coordinates if i != j)

# Constraints: Connect all groups via selecting one city from each
for g in groups.keys():
    prob += lpSum(x[i, j] for i in groups[g] for j in coordinates if i != j) == 1  # Each group sends out 1 connection
    prob += lpSum(x[j, i] for i in groups[g] for j in coordinates if i != j) == 1  # Each group receives 1 connection

# Subtour prevention
for i in coordinates:
    for j in coordinates:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + len(coordinates) * x[i, j] <= len(coordinates) - 1

# Solve the problem
prob.solve()

# Extract tour
tour = []
current = 0
for _ in range(len(coordinates)):
    for k in coordinates:
        if k != current and pulp.value(x[current, k]) == 1:
            tour.append(k)
            current = k
            break

# Closing the tour by adding the depot
tour.insert(0, 0)
tour.append(0)

# Calculate the total distance
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)