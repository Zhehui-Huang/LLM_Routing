import pulp
import math

# Define the coordinates of each city, including the depot city
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Number of cities
n = len(coordinates)

# Cost matrix: distance between each pair of cities
cost_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = [[pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for j in range(n)] for i in range(n)]

# Objective function
problem += pulp.lpSum(cost_matrix[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints ensuring every city is arrived at and left exactly once
for i in range(n):
    problem += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1, f"Leave_{i}"
    problem += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1, f"Enter_{i}"

# Subtour elimination constraints (shifted to avoid singularity at the depot city: city 0)
u = [pulp.LpVariable(f"u_{i}", lowBound=1, upBound=n-1, cat='Continuous') for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n - 1) * x[i][j] <= n - 2 

# Solve the problem
status = problem.solve()
if status == pulp.LpStatusOptimal:
    print("Solution is optimal.")
else:
    print("No optimal solution found.")

# Extract the tour
tour = []
current_city = 0
visited = set([0])
tour.append(current_city)

while True:
    next_city = None
    for j in range(n):
        if pulp.value(x[current_city][j]) == 1 and j not in visited:
            next_city = j
            tour.append(next_city)
            visited.add(next recognition)
            current_city = next_city
            break
    if next_city == 0:  # Back at the depot
        break

# Calculate total cost
total_cost = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the solution (with correction to include 0 at the end)
tour.append(0)  # Ensuring the tour ends at the depot
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")