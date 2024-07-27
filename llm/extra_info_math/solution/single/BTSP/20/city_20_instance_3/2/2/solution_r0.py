import pulp
import math

# Define the coordinates of each city including the depot city
coordinates = [
    (30, 56), # Depot city 0
    (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), 
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25),
    (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate the Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities (including the depot)
n = len(coordinates)

# Initialize the optimization problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the path is direct from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Dummy variable for the Minimax objective
z = pulp.LpVariable("z", lowBound=0)

# Objective Function: minimax the maximum distance
problem += z, "Minimax Objective"

# Constraints for Minimax
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i][j] * distance(coordinates[i], coordinates[j]) <= z

# Each city is left exactly once
for i in range(n):
    problem += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1

# Each city is entered exactly once
for j in range(n):
    problem += pulp.lpSum(x[i][j] for i in range(n) if i != j) == 1

# Subtour elimination constraints (using Miller-Tucker-Zemlin formulation)
u = pulp.LpVariable.dicts('u', range(n), lowBound=1, upBound=n, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n*x[i][j] <= n-1

# Solve the problem
problem.solve()

# Check whether a feasible solution Exists
if pulp.LpStatus[problem.status] == 'Optimal':
    # Create a tour from the decision variables
    path = []
    for i in range(n):
        for j in range(n):
            if x[i][j].varValue == 1:
                path.append((i, j))

    # Start from depot, follow path
    tour = [0]
    while len(tour) < n:
        current = tour[-1]
        for _, next_city in path:
            if next_city == current:
                path.remove((current, next_city))
                tour.append(next_city)
                break

    # Close the tour by returning to the depot
    tour.append(0)

    # Calculate max distance and total travel cost
    max_distance = 0
    total_distance = 0
    for i in range(len(tour)-1):
        d = distance(coordinates[tour[i]], coordinates[tour[i+1]])
        total_distance += d
        if d > max_distance:
            max_distance = d

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No feasible solution found")