import pulp
import math
import itertools

# Coordinates of the cities including the depot
coords = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

n = len(coords)  # Number of cities including the depot

# Euclidean distance calculation function
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generating distance matrix
distances = [[distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Define the optimization model
model = pulp.LpProblem("Minimax TSP", pulp.LpMinimize)

# Define decision variables
x = pulp.LpVariable.dicts("x", (range(n), range(n)), 0, 1, pulp.LpBinary)
max_dist = pulp.LpVariable("max_dist", lowBound=0)

# Objective function to minimize the maximum distance traveled between consecutive cities
model += max_dist

# Constraints
for i in range(n):
    model += pulp.lpSum([x[i][j] for j in range(n) if i != j]) == 1  # leave each city only once
    model += pulp.lpSum([x[j][i] for j in range(n) if i != j]) == 1  # enter each city only once

# Max distance constraints for the objective
for i in range(n):
    for j in range(n):
        if i != j:
            model += max_dist >= distances[i][j] * x[i][j]

# Sub-tour elimination
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        model += pulp.lpSum([x[i][j] for i in subset for j in subset if i != j]) <= len(subset) - 1

# Solve the problem
model.solve()

# Extract solution
if model.status == 1:  # Check if the solution is optimal
    edges = [(i, j) for i in range(n) for j in range(n) if pulp.value(x[i][j]) == 1]
    tour = []
    visited = [False] * n
    current_city = 0
    while True:
        tour.append(current_city)
        visited[current_city] = True
        next_cities = [j for (i, j) in edges if i == current_city and not visited[j]]
        if not next_cities:
            break
        current_city = next_cities[0]
    tour.append(tour[0])  # complete the tour by returning to the starting city

    # Calculate total distance and maximum segment distance
    total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_segment_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    # Outputs
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_segment.button}")

else:
    print("No solution found.")