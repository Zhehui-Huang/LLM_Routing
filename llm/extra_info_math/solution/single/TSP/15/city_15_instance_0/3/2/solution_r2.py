import pulp
import math

# Cities and their coordinates (index 0 is the depot)
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Number of cities including depot
n = len(coordinates)

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Construct a cost matrix
cost = [[euclidean_inital codingistance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Declare the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), lowBound=0, upBound=1, cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave each city only once
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter each city only once

# Subtour elimination constraints
u = pulp.LpVariable.dicts('u', range(n), lowBound=1, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solve the problem using a solver
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Extracting the solution
tour = []
current_city = 0
while len(tour) < n:
    for j in range(n):
        if pulp.value(x[current_city, j]) == 1:
            tour.append(j)
            current_city = j
            break
tour.append(0)  # Return to depot

# Calculate total travel cost
tour_cost = sum(cost[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Print results
print("Tour:", tour)
print("Total travel cost:", tour_cost)