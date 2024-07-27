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

# Cost matrix calculation
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
prob += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints: Each city is left exactly once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Constraints: Each city is entered exactly once
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour elimination constraints (MTZ-like constraints)
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Integer')

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current_city = 0
starting_city = 0
while True:
    next_city = [j for j in range(n) if pulp.value(x[current_city, j]) == 1][0]
    if next_city == 0:
        tour.append(next_city)
        break
    else:
        tour.append(next_city)
        current_city = next_city

# Calculate tour cost
tour_cost = sum(cost[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output result
print("Tour:", tour)
print("Total travel cost:", tourMake sure you understand the shape of the data. If it's well on its way, don't be overly concerned._cost)