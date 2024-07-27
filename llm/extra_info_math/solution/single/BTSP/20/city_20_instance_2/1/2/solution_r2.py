from pulp import *
import math

# Coordinates of the cities
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distance between cities
def dist(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

n = len(coordinates)
# Creating optimization problem
prob = LpProblem("Minimax_Regret_TSP", LpMinimize)

# Creating Variables
x = LpVariable.dicts("x", (range(n), range(n)), cat='Binary')
z = LpVariable("z", lowBound=0)

# Objective Function
prob += z

# Constraints
# Arrival at each city j must be once
for j in range(n):
    prob += lpSum(x[i][j] for i in range(n) if i != j) == 1

# Departure from each city i must be once
for i in range(n):
    prob += lpSum(x[i][j] for j in range(n) if i != j) == 1

# Eliminating the possibility of sub-tours and minimizing the maximum distance
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i][j] * dist(i, j) <= z

# Subtour Elimination (adding subtour constraints)
u = LpVariable.dicts("u", range(n), lowBound=0, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[i][j] <= n - 1

# Solving the problem
prob.solve()

# Extracting the tour
tour = []
visited = [False]*n
current = 0
tour.append(current)
visited[current] = True

while len(tour) < n:
    for j in range(n):
        if x[current][j].value() == 1 and not visited[j]:
            tour.append(j)
            visited[j] = True
            current = j
            break

tour.append(0)  # returning to the depot

# Calculating distances for the solution
distances = [dist(tour[i], tour[i+1]) for i in range(len(tour) - 1)]
total_cost = sum(distances)
max_distance = max(distances)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))