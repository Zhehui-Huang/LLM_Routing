import pulp
import math

# Coordinates of the cities
coordinates = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
               (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
               (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Number of cities
n = len(coordinates)

# Precompute the euclidean distances between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Cost matrix
cost = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij is 1 if the tour goes directly from city i to city j, 0 otherwise
x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(cost[i, j] * x[i][j] for i in range(n) for j in range(n))

# Constraints:
# Each city is left exactly once
for i in range(n):
    prob += pulp.lpSum(x[i][j] for j in range(n) if j != i) == 1

# Each city is entered exactly once
for j in range(n):
    prob += pulp.lpSum(x[i][j] for i in range(n) if i != j) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += x[i][j] <= pulp.lpSum(x[k][i] for k in range(n) if k != i)

# Solve the problem
prob.solve()

# Output the optimal tour
tour = []
current_city = 0
starting_city = 0

while True:
    for j in range(n):
        if pulp.value(x[current_city][j]) == 1 and j not in tour:
            tour.append(j)
            current_city = j
            break
    if current_city == starting_city:
        break

tour.insert(0, starting_city) # Ensure the tour starts from the depot city
tour.append(starting_city) # End the tour at the depot city

# Calculate the total cost of the tour
total_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Result
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))