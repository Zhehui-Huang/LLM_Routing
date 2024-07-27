import pulp
import math

# City coordinates
cities = [
    (8, 11),   # Depot city: 0
    (40, 6),   (95, 33),  (80, 60),  (25, 18),  (67, 23),  (97, 32),
    (25, 71),  (27, 91),  (61, 16),  (20, 97),  (91, 46),  (40, 87),
    (5, 59),   (62, 88),  (13, 43),  (61, 28),  (60, 63),  (93, 15)
]

n = len(cities)  # Number of cities, including the depot

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Initialize LP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = [[pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for j in range(n)] for i in range(n)]
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Objective
problem += z, "Minimize the maximum distance between consecutive cities"

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1, f"From_city_{i}"
    problem += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1, f"To_city_{i}"

# Distance constraints to control the maximum distance
for i in range(n):
    for j in range(n):
        if i != j:
            d = euclidean_distance(cities[i], cities[j])
            problem += d * x[i][j] <= z, f"Max_dist_from_{i}_to_{j}"

# Subtour elimination using MTZ constraints
u = [pulp.LpVariable(f"u_{i}", lowBound=0, upBound=n-1, cat='Integer') for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i][j] <= n - 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Output the solution
if status == pulp.LpStatusOptimal:
    tour = [0]
    current = 0
    total_distance = 0
    max_link_distance = 0
    
    for _ in range(n):
        next_city = next(j for j in range(n) if pulp.value(x[current][j]) == 1)
        tour.append(next_city)
        dist = euclidean_siistance(cities[current], cities[next_city])
        total_distance += dist
        max_link_distance = max(max_link_distance, dist)
        current = next_city
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_link_distance}")
else:
    print("An optimal solution could not be found.")