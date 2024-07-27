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
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), lowBound=0, upBound=1, cat='Binary')
z = pulp.LpVariable("z", lowBound=0)

# Objective function to minimize the maximum distance between consecutive cities
prob += z, "Minimize the maximum distance between consecutive cities"

# Constraints for ensuring each city is visited exactly once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Outgoing constraint at city {i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Incoming constraint at city {i}"

# Upper bound maximum distance between consecutive cities
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * euclidean_distance(cities[i], cities[j]) <= z, f"Distance constraint from {i} to {j}"

# Subtour Elimination Constraints improved version
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=1, upBound=n-1, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve the problem
prob.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract solution - check if the solution is optimal
if prob.status == pulp.LpStatusOptimal:
    tour = []
    remaining = list(range(n))
    current_city = 0

    # Construct the tour
    while True:
        tour.append(current_city)
        remaining.remove(current_city)
        next_cities = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        current_city = next_cities[0]
    tour.append(0)  # return to starting city

    # Compute total distance and maximum distance segment
    total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    max_segment_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    # Output the results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance:.2f}")
    print(f"Maximum distance between consecutive cities: {pulp.value(z):.2f}")
else:
    print("No optimal solution found.")