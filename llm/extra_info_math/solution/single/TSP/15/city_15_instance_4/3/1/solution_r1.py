import pulp
import math
import itertools

# Given coordinates of each city including the depot at index 0
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coordinates)

# Distances between each pair of cities
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i, j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            distances[i, j] = 0

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum(distances[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j), "Total Travel Distance"

# Constraints
for i in range(n):
    problem += (pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1), f"Leave_city_{i}"
    problem += (pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1), f"Enter_city_{i}"

# Subtour constraints
for s in range(2, n):
    for subset in itertools.combinations(range(1, n), s):
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1, f"Subtour_{subset}"

# Solving the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))
if status == pulp.LpStatusOptimal:
    print("An optimal solution has been found.")
else:
    print("Failed to find an optimal solution.")

# Extract the tour
tour = []
initial_city = 0
tour.append(initial_city)

while len(tour) < n:
    next_cities = [j for j in range(n) if j not in tour and pulp.value(x[tour[-1], j]) == 1]
    if next_cities:
        tour.append(next_cities[0])

# Append the initial city to complete the circuit
tour.append(initial_city)

total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")