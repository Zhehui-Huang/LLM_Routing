import pulp
import itertools
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Provided city locations and groups
city_locations = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

# Compute distances
distances = {}
for i in range(15):
    for j in range(15):
        if i != j:
            distances[(i, j)] = euclidean_distance(city_locations[i], city_locations[j])

# Model setup
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(15) for j in range(15) if i != j), cat='Binary')

# Objective
model += pulp.lpSum(distances[i, j] * x[i, j] for i in range(15) for j in range(15) if i != j)

# Constraints
# Each group must connect exactly once to a node outside the group
for group in groups:
    model += pulp.lpSum(x[i, j] for i in group for j in range(15) if j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in range(15) if j not in group) == 1

# Flow conservation at each node
for k in range(15):
    model += pulp.lpSum(x[i, k] for i in range(15) if i != k) == pulp.lpSum(x[k, j] for j in range(15) if j != k)

# Solve the problem
model.solve()

# Extract the solution
tour = []
visited = set()
current = 0
tour.append(current)
visited.add(current)
total_dist = 0

while len(visited) < 9:
    next_cities = [j for j in range(15) if pulp.value(x[current, j]) == 1]
    next_city = next_cities[0]
    tour.append(next_city)
    total_dist += distances[current, next_city]
    visited.add(next_city)
    current = next_city

# Remember to connect back to the depot
tour.append(0)
total_dist += distances[current, 0]

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_dist}")