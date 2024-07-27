import pulp
import math

# City Coordinates
cities = [
    (8, 11),   # Depot city: 0
    (40, 6),   (95, 33),  (80, 60),  (25, 18),  (67, 23),  (97, 32),
    (25, 71),  (27, 91),  (61, 16),  (20, 97),  (91, 46),  (40, 87),
    (5, 59),   (62, 88),  (13, 43),  (61, 28),  (60, 63),  (93, 15)
]

n = len(cities)  # Number of cities, including the depot

# Distance calculation
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Problem initialization
problem = pulp.LpProblem("Min_Max_Distance_TSP", pulp.LpMinimize)

# Variables
x = [[pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary) for j in range(n)] for i in range(n)]
z = pulp.LpVariable("z", lowBound=0)

# Objective
problem += z, "Minimize_the_maximum_distance_between_consecutive_cities"

# Constraints
for i in range(n):
    problem += sum(x[i][j] for j in range(n) if i != j) == 1
    problem += sum(x[j][i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i][j] * euclidean_distance(cities[i], cities[j]) <= z

# Subtour Elimination
u = [pulp.LpVariable(f"u_{i}", cat=pulp.LpContinuous, lowBound=1, upBound=n-1) for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1)*x[i][j] <= n-2

# Solve the problem
problem.solve()

# Extract the solution
routes = [[pulp.value(x[i][j]) for j in range(n)] for i in range(n)]
tour = []
current = 0
total_distance = 0
max_link_distance = 0

for i in range(n):
    tour.append(current)
    next_city = routes[current].index(1)  # Find the next city with a connection value of 1
    dist = euclidean_distance(cities[current], cities[next_city])
    total_distance += dist
    max_link_distance = max(max_link_distance, dist)
    current = next_city

# Close the tour by returning to the depot
tour.append(0)
dist = euclidean_distance(cities[current], cities[0])
total_distance += dist
max_link_distance = max(max_link_distance, dist)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_link_distance}")