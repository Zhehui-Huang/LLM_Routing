import pulp
import math
from itertools import combinations

# Coordinates of cities including the depot
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Number of cities (including depot)
n = len(coordinates)

# Function to compute Euclidean distance
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables, x_ij is 1 if travel from city i to city j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Slack variable for measuring the min max dist
z = pulp.LpVariable("z", lowBound=0)

# Objective function: Minimize the maximum distance traveled between any two consecutive cities
problem += z

# Each city must be entered and left exactly once
for i in range(n):
    problem += sum(x[i, j] for j in range(n) if i != j) == 1  # leave i
    problem += sum(x[j, i] for j in range(n) if i != j) == 1  # enter i

# Subtour Elimination Constraints
for k in range(2, n):
    for S in combinations(range(1, n), k):  # skip the depot
        problem += sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Constraint that z is at least the distance of each travel x[i, j] == 1
for i in range(n):
    for j in range(n):
        if i != j:
            problem += z >= euclidean_distance(i, j) * x[i, j]

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))
print("Status:", pulp.LpStatus[status])

# Construct the tour from the decision variables
tour = []
reverse_x = {(i, j): x[i, j].varValue for i, j in x}
current_location = 0
for _ in range(n):
    next_location = next(j for j in range(n) if j != current_location and reverse_x[current_location, j] == 1.0)
    tour.append(current_location)
    current_location = next_location
tour.append(0)  # Return to depot

# Calculating total cost and maximum distance
total_cost = 0.0
max_distance = 0.0
for i in range(len(tour) - 1):
    dist = euclidean_distance(tour[i], tour[i + 1])
    total_cost += dist
    max_distance = max(max_distance, dist)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)