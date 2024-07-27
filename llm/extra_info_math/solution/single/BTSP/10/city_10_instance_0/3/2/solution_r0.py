import pulp
import math

# Define the coordinates of each city including the depot city
coordinates = [
    (50, 42), # City 0 (Depot)
    (41, 1),  # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49)  # City 9
]

# Calculate distances between all pairs of cities using Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Set up the optimization problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define decision variables
x = pulp.LpVariable.dicts('x', [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Dummy variable to represent the maximum distance in the objective
max_distance = pulp.LpVariable("max_distance", lowBound=0)

# Objective: minimize the maximum distance between any two consecutive cities
problem += max_distance

# Constraints
# Each city must be entered and left only once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leaving city i
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Entering city i

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += x[i, j] + x[j, i] <= 1

# Link max_distance to the x_ij variables
for i in range(n):
    for j in range(n):
        if i != j:
            problem += max_distance >= distances[i][j] * x[i, j]

# Solve the problem
status = problem.solve()

if pulp.LpStatus[status] == 'Optimal':
    print("Tour found")
    path = []
    # Retrieve tour path
    curr = 0
    while True:
        path.append(curr)
        next_city = [j for j in range(n) if pulp.value(x[curr, j]) == 1][0]
        if next_city == 0:
            break
        curr = next_city
    path.append(0)  # Return to depot
    
    # Calculate the total cost and maximum distance between consecutive cities
    total_cost = sum(distances[path[i]][path[i + 1]] for i in range(len(path) - 1))
    max_dist = max(distances[path[i]][path[i + 1]] for i in range(len(path) - 1))
    
    print(f"Tour: {path}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist}")
else:
    print("No optimal solution found")