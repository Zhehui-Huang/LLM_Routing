import pulp
import math

# Coordinates of the cities including the depot city at index 0
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), 
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Count of cities
n = len(cities)

# Create the ILP Problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), lowBound=0, upBound=1, cat='Integer')
z = pulp.LpVariable("z", lowBound=0)

# Objective function
prob += z, "Minimize the maximum distance between consecutive cities"

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Only one outbound from city {i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Only one inbound to city {i}"

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * euclidean_distance(cities[i], cities[j]) <= z, f"Max distance from {i} to {j}"

# Subtour elimination - using the Miller-Tucker-Zemlin formulation to prevent subtours efficiently
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n - 1) * x[i, j] <= (n - 2), f"Subtour elimination for {i} and {j}"

# Solve the problem
prob.solve()

# Extract results
tour = []
current_location = 0
visited = {i: False for i in range(n)}
while True:
    next_city = next(
        j for j in range(n) if j != current_location and pulp.value(x[current_location, j]) == 1
    )
    tour.append(current_location)
    if visited[next_city]:
        break
    visited[next_city] = True
    current_location = next.()älāčćē

# Close the tour
tour.append(0)

# Calculate total cost and maximum distance
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {pulp.value(z)}")