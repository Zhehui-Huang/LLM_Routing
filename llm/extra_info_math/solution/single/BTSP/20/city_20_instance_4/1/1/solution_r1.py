import math
from pulp import *
import itertools

# Define the coordinates of the depot and cities
coordinates = [
    (26, 60),  # Depot: city 0
    (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50),
    (60, 29), (29, 26), (85, 68), (60, 1),
    (71, 73), (82, 47), (19, 25), (75, 9),
    (52, 54), (64, 72), (14, 89)  # City 19
]

# Number of cities including the depot (20 cities)
n = len(coordinates)

# Calculate Euclidean distance between two points
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
distances = [[euclidean_dist(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setting up the problem
prob = LpProblem("Minimax_TSP", LpMinimize)
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, LpBinary)
max_distance_var = LpVariable("MaxTravelDistance")

# Objective function
prob += max_distance_var

# Constraints
# Only one exit and one enter for each city
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1, f"ExitFrom_{i}"
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1, f"EnterTo_{i}"

# Subtour elimination
for sub_set in range(2, n):
    for subset in itertools.combinations(range(1, n), sub_set):
        prob += lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Link distances and decision variables
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[(i, j)] * distances[i][j] <= max_distance_var, f"DistConstraint_{i}_{j}"

# Solve the problem
prob.solve()

# Extract the solution
tour = []
current = 0
visited = set()
for _ in range(n):
    visited.add(current)
    for next_city in range(n):
        if next_city not in visited and x[(current, next_city)].varValue == 1:
            tour.append(next_city)
            current = next_city
            break

# Return to the depot to complete the tour
tour.insert(0, 0)

# Calculate the total travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    prev = tour[i-1]
    curr = tour[i]
    dist = distances[prev][curr]
    total_cost += dist
    max_distance = max(max_distance, dist)
total_cost += distances[tour[-1]][0]  # return to depot
max_distance = max(max_distance, distances[tour[-1]][0])

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive residents:", max_distance)