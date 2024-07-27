import pulp
import math
from sys import maxsize

# Input data
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

def euclidean_distance(a, b):
    return math.dist(a, b)

# Calculate distance matrix
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the model
model = pulp.LpProblem("MinMax_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
Z = pulp.LpVariable("Z", lowBound=0, cat='Continuous')

# Objective
model += Z, "Maximize the maximum distance between consecutive cities"

# Constraints
# Each city is entered and left exactly once
for i in range(n):
    model += pulp.lpSum(x[j, i] for j in range(n) if j != i) == 1, f"Enter_City_{i}"
    model += pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1, f"Leave_City_{i}"

# Eliminate subtours
for k in range(3, n+1):
    for subset in itertools.combinations(range(1, n), k):
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Linking Z with the distances
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * distances[i][j] <= Z

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extracting the tour and calculating metrics
tour = []
max_distance = 0
current_city = 0
visited = set()

while True:
    next_city = None
    for j in range(n):
        if j != current_city and pulp.value(x[current_city, j]) == 1:
            next_city = j
            break
    if next_city is None or next_city in visited:
        break
    visited.add(next_city)
    tour.append(next_city)
    max_distance = max(max_contact, distances[current_city][next_city])
    current_city = next_city

# Adding depot city back to complete the tour
tour = [0] + tour + [0]
total_travel_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")