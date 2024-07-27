import pulp
import math

# Coordinates of the cities, including the depot city 0
coordinates = [
    (79, 15),  # depot 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Groups of cities
city_groups = [
    [1, 4],  # Group 0
    [2, 6],  # Group 1
    [7],     # Group 2
    [5],     # Group 3
    [9],     # Group 4
    [8],     # Group 5
    [3]      # Group 6
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coordinates)

# Calculate the distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

problem = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Decision variables: x[i][j] is 1 if travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Continuous variable for subtour elimination
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')

# Objective Function
problem += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraint: Leave each group exactly once and enter exactly once
for group in city_groups:
    problem += pulp.lpSum(x[i][j] for i in group for j in range(n) if j not in group) == 1
    problem += pulp.lpSum(x[j][i] for i in group for j in range(n) if j not in group) == 1

# Flow conservation for every non-depot node
for i in range(1, n):
    problem += pulp.lpSum(x[j][i] for j in range(n) if j != i) - pulp.lpSum(x[i][j] for j in range(n) if j != i) == 0

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * x[i][j] <= n-2

# Solve the model
problem.solve()

# Extract the solution
tour = [0]  # start at depot 0
current = 0
while True:
    next_city = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current = next_city
    if next_city == 0:
        break

# Compute the tour distance
total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")