import pulp
import math

# City coordinates
depot_and_cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Preparing distances
n = len(depot_and_cities)
distances = [[distance(depot_and_cities[i], depot_and_cities[j]) for j in range(n)] for i in range(n)]

# Creating the optimization model
model = pulp.LpProblem("Minimize_max_distance", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')

# Objective to minimize the maximum distance
max_distance = pulp.LpVariable("max_distance")
model += max_distance

for i in range(n):
    for j in range(n):
        if i != j:
            model += x[(i, j)] * distances[i][j] <= max_distance

# Constraints
# Enter each city once
for j in range(n):
    model += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Leave each city once
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Subtour elimination
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        model += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve model
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the tour from the result
tour = []
current_city = 0
while True:
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(current_city)
    current_city = next_city
    if current_city == 0:
        break
tour.append(0)  # Return to depot

# Calculate the tour cost and maximum distance
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_step_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_step_distance)