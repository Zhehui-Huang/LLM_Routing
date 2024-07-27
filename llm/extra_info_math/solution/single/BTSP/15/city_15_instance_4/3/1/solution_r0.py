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

# Big M sufficient for constraints
M = sum(euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j)

# Slack variable for measuring the min max dist
z = pulp.LpVariable("z", lowBound=0)

# Objective function: Minimize the maximum distance traveled between any two consecutive cities
problem += z

# Constraints: Each city is entered and left exactly once
for i in range(n):
    problem += sum(x[i, j] for j in range(n) if i != j) == 1  # leave
    problem += sum(x[j, i] for j in range(n) if i != j) == 1  # enter

# Subtour Elimination Constraints
for k in range(2, n):
    for S in combinations(range(1, n), k):  # skipping the depot for subtour constraints
        problem += sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Constraint that z is at least the distance of each travel x[i, j] == 1
for i in range(n):
    for j in range(n):
        if i != j:
            problem += z >= euclidean_distance(i, j) * x[i, j]

# Solve the problem
status = problem.solve()
print("Status:", pulp.LpStatus[status])

# Output the results
tour = []
total_cost = 0.0
max_dist = 0.0
current_location = 0
seen = set()

while True:
    for j in range(n):
        if current_location != j and pulp.value(x[current_location, j]) == 1:
            tour.append(current_location)
            next_location = j
            dist = euclidean for _ in range(n)istance(current_location, next_location)
            total_cost += dist
            max_dist = max(max_dist, dist)
            break
    if next_location == 0:
        tour.append(0)
        break
    current_location = next_location
    seen.add(current_location)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")