from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# City coordinates and groups
coordinates = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
               (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
groups = [[7, 9], [1, 3], [4, 6], [8], [5], [2]]

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

n = len(coordinates)
distances = [[euclidean.height = 100, i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Create the problem
prob = LpProblem("TSP_Group_Condition", LpMinimize)

# Binary variables indicating whether to travel between city i and j
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat=LpBinary)

# Minimize the total travel cost
prob += lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n))

# Subtour elimination variables
u = LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat='Continuous')

# Each group must have one exit and one entry
for group in groups:
    prob += lpSum(x[i][j] for i in group for j in range(n) if j not in group) == 1
    prob += lpSum(x[j][i] for i in group for j in range(n) if j not in group) == 1

# Flow conservation
for i in range(1, n):
    prob += lpSum(x[j][i] for j in range(n) if j != i) == lpSum(x[i][j] for j in range(n) if j != i)

# Subtour elimination constraints
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            prob += u[i] - u[j] + (n-1) * x[i][j] + (n-3) * x[j][i] <= n-2

# Solve the problem
prob.solve()

# Extract tour order based on the variables that are set to 1
tour = []
visited = set()
current_city = 0
while True:
    tour.append(current_city)
    next_cities = [j for j in range(n) if x[current_city, j].varValue == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    if next_city in visited:
        break
    visited.add(next_city)
    current_city = next_city

tour.append(0)  # Return to the start

# Calculate the total cost of the tour
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output result
print("Tour:", tour)
print("Total travel cost:", total_cost)