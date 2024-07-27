import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary

# Define the city coordinates
city_coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), 
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Compute Euclidean distances
def euclidean_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)

n = len(city_coords)

# Create distance matrix
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(city§Ãords[i], city_coords[j])

### Step 2: Define the optimization problem
# Create the problem variable
problem = LpProblem("Minimax_TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, LpBinary)
u = LpVariable.dicts("u", list(range(n)), lowBound=0, upBound=n-1, cat='Integer')  # For subtour elimination

# Auxiliary variable to represent the maximum distance between consecutive cities
dmax = LpVariable("dmax", lowBound=0, cat='Continuous')

### Step 3: Define the constraints and objective function
# Add objective
problem += dmax, "Minimize the maximum distance between any two consecutive cities"

# Constraints
for i in range(n):
    problem += lpSum([x[i, j] for j in range(n) if i != j]) == 1, f"Outflow_{i}"
    problem += lpSum([x[j, i] for j in range(n) if i != j]) == 1, f"Inflow_{i}"

# Subtour elimination (MTZ constraints)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Ensure dmax is greater than or equal to each distance of the selected edges
for i in range(n):
    for j in range(n):
        if i != j:
            problem += dmax >= x[i, j] * distance_matrix[i, j]

### Step 4: Solve the problem
problem.solve()

### Step 5: Extract the solution
tour = []
visited = [0]
while len(visited) < n:
    for j in range(n):
        if x[visited[-1], j].varValue == 1:
            visited.append(j)
            break
tour = visited + [0]  # to complete the circuit by returning to the depot

# Calculate the total distance and maximum distance
total_distance = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

### Step 6: Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")