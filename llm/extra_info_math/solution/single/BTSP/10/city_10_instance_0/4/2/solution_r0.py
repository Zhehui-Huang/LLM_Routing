import math
import pulp

# Given coordinates of the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Helper function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[i, j] = calculate Distance(cities[i], cities[j])

# Create the optimization model
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if path from city i to city j is taken, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
M = pulp.LpVariable("M")
model += M

# Constraints
# Each city must be left exactly once
for i in cities:
    model += pulp.lpSum(x[i, j] for j in cities if i != j) == 1

# Each city must be entered exactly once
for j in cities:
    model += pulp.lpSum(x[i, j] for i in cities if i != j) == 1

# Subtour elimination
for S in range(2, len(cities)):
    for subset in itertools.combinations(cities.keys(), S):
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Set M as the maximum distance of the selected paths
for i in cities:
    for j in cities:
        if i != j:
            model += M >= x[i, j] * distances[i, j]

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# Check if a feasible solution is found
if status != 1:
    print("Failed to find a feasible solution.")
else:
    # Retrieving the solution
    tour = []
    position = 0
    while len(tour) < len(cities):
        tour.append(position)
        next_moves = [j for j in cities if position != j and pulp.value(x[position, j]) == 1]
        position = next_moves[0]

    tour.append(0)  # Return to the depot

    total_distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

    # Output the results
    print("Tour:", tour)
    print("Total travel cost:", round(total_distance, 2))
    print("Maximum distance between consecutive cities:", round(max_distance, 2))