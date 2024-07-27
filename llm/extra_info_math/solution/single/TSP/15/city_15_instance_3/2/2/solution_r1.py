import pulp
import math
import itertools

# Define the cities, including the depot city at index 0
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Number of cities including the depot
n = len(cities)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Calculate costs for all city pairs
costs = { (i, j): euclidean_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j }

# Create the TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define decision variables
x = pulp.LpVariable.dicts('x', costs.keys(), cat='Binary')

# Objective function
model += pulp.lpSum([costs[i, j] * x[i, j] for i, j in costs.keys()])

# Constraints: Depart from each city exactly once
for i in range(n):
    model += pulp.lpSum([x[i, j] for j in range(n) if (i, j) in x]) == 1

# Constraints: Enter each city exactly once
for j in range(n):
    model += pulp.lpSum([x[i, j] for i in range(n) if (i, j) in x]) == 1

# Subtour elimination
for s in range(3, n):
    for S in itertools.combinations(range(1, n), s):
        model += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# Prepare the output
tour = []
current_location = 0

while True:
    next_locations = [j for j in range(n) if (current_location, j) in x and pulp.value(x[current_location, j]) == 1]
    if not next_locations:
        break
    next_location = next_locations[0]
    tour.append(next_location)
    current_location = next_location
    if next_location == 0:
        break

total_cost = sum(costs[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Result
print(f"Tour: {[0] + tour}")
print(f"Total travel cost: {total_cost}")