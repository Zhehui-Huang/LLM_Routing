import pulp
import math

# Define city coordinates
coordinates = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30), 6: (52, 82),
    7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Define city groups
city_groups = {
    0: [8, 12, 14], 1: [7, 10, 11], 2: [4, 6, 9], 3: [1, 3, 13], 4: [2, 5]
}

# Function to calculate Euclidean distance
def euclidean_dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the LP problem
problem = pulp.LpProblem("RobotTour", pulp.LpMinimize)

# Variables: x_ij = 1 if the robot travels from city i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in coordinates for j in coordinates if i != j), cat='Binary')

# Objective function: Minimize total distance traveled
problem += pulp.lpSum(x[i, j] * euclidean_dist(coordinates[i], coordinates[j]) for i in coordinates for j in coordinates if i != j)

# Constraint: Each group must have exactly 1 exit and 1 entry
for _, group in city_groups.items():
    problem += pulp.lpSum(x[i, j] for i in group for j in coordinates if j not in group) == 1  # Exact 1 exit
    problem += pulp.lpSum(x[i, j] for j in group for i in coordinates if i not in group) == 1  # Exact 1 entry

# Constraint: Flow conservation
for i in coordinates:
    if i == 0:
        problem += pulp.lpSum(x[j, i] for j in coordinates if j != i) == 1
        problem += pulp.lpSum(x[i, j] for j in coordinates if j != i) == 1
    else:
        problem += pulp.lpSum(x[j, i] for j in coordinates if j != i) - pulp.lpSum(x[i, j] for j in coordinates if j != i) == 0

# Solve the problem
status = problem.solve()
if status == pulp.LpStatusOptimal:
    print("Solution Found")
    tour = []
    current = 0
    tour.append(current)
    costs = 0
    for _ in range(len(coordinates)):
        next_city = [j for j in coordinates if j != current and pulp.value(x[current, j]) == 1]
        if next_city:
            next_city = next_city[0]
            costs += euclidean_dist(coordinates[current], coordinates[next_city])
            current = next_city
            tour.append(current)
        if current == 0:
            break
    print("Tour:", tour)
    print("Total travel cost:", round(costs, 2))
else:
    print("No optimal solution found")