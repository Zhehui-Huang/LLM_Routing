import pulp
import math

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
    (64, 72), (14, 89)
]
n = len(coordinates)

# Calculate Euclidean distance between any two cities
def get_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost matrix
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[(i, j)] = get_distance(coordinates[i], coordinates[j])
        else:
            cost_matrix[(i, j)] = float('inf')  # Self loop, not possible

# Define the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", cost_matrix.keys(), lowBound=0, upBound=1, cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum([x[(i, j)] * cost_matrix[(i, j)] for i in range(n) for j in range(n) if i != j])

# Constraints
for i in range(n):
    prob += pulp.lpSum([x[(i, j)] for j in range(n) if j != i]) == 1  # leave each city
    prob += pulp.lpSum([x[(j, i)] for j in range(n) if j != i]) == 1  # enter each city

# Subtour elimination constraints handled using u (MTZ formulation)
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[(i, j)] <= n - 1

# Solve the problem using an appropriate solver
solver = pulp.PULP_CBC_CMD(msg=0)  # You can use any solver of your choice
prob.solve(solver)

# Extract the path based on x values
tour = []
visited = {0}
current = 0
for _ in range(n):
    tour.append(current)
    for j in range(n):
        if pulp.value(x[(current, j)]) == 1:
            current = j
            visited.add(current)
            break

tour.append(0)  # return to start
total_cost = sum(cost_matrix[(tour[i], tour[i+1])] for i in range(n))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")