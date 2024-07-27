import pulp
import math

# Function to calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Coordinates of all cities including the depot
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

n = len(coordinates)

# Create a distance matrix
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Create decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints (SEC) using MTZ formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=1, upBound=n, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solve the problem
status = problem.solve()

if pulp.LpStatus[status] == 'Optimal':
    print("Solution found")
else:
    print("An optimal solution has not been found.")

# Extract the tour
tour = []
visited = [False] * n
current = 0
while not visited[current]:
    visited[current] = True
    tour.append(current)
    for j in range(n):
        if x[current, j].varValue == 1:
            current = j
            break
tour.append(0)  # Return to depot

# Calculate the total cost
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Outputting the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")