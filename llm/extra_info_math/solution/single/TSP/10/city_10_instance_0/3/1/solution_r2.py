import pulp
import math

# Coordinates of cities, including the depot city
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define integer programming problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Binary decision variables: x[i][j] is 1 if path from i to j is taken
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Objective: Minimize the sum of the distances for the paths taken
problem += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraint: Enter each city exactly once
for j in range(1, n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Constraint: Leave each city exactly once
for i in range(1, n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Start and end at the depot city 0
problem += pulp.lpSum(x[0, j] for j in range(1, n)) == 1
problem += pulp.lpSum(x[i, 0] for i in range(1, n)) == 1

# Subtour elimination
for k in range(3, n + 1):
    for subset in itertools.combinations(range(1, n), k):
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the TSP
problem.solve()

# Check the status
if pulp.LpStatus[problem.status] == 'Optimal':
    # Extract the tour from variables
    tour = []
    current_city = 0
    for _ in range(n):
        tour.append(current_city)
        next_cities = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1.0]
        if not next_cities:
            break
        current_city = next_cities[0]
    tour.append(0)  # Return to start

    total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print("Tour:", tour)
    print("Total travel cost:", total_distance)
else:
    print("Failed to find an optimal solution. Status:", pulp.LpStatus[problem.status])