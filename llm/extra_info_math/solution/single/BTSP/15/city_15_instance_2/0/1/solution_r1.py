import pulp
import math
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}
n = len(cities)

# Calculate the Euclidean distance between two cities
def dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Set up the problem instance
model = pulp.LpProblem("Minimize_Maximum_Distance_in_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
max_dist = pulp.LpVariable("max_dist", lowBound=0, cat='Continuous')

# Objective function
model += max_dist

# Constraints
for i in cities:
    model += pulp.lpSum(x[j, i] for j in cities if i != j) == 1
    model += pulp.lpSum(x[i, j] for j in cities if i != j) == 1

# Avoid subtours
for s in range(2, n):
    for S in combinations(cities, s):
        model += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Link max_dist to the route distances
for i in cities:
    for j in cities:
        if i != j:
            model += max_dist >= dist(i, j) * x[i, j]

# Solve the problem
model.solve()

# Extract solution
tour = []
for i in cities:
    for j in cities:
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# We need to order the tour correctly starting from 0
ordered_tour = [0]
visited = set()
visited.add(0)
current = 0

while len(ordered_tour) < n:
    for (i, j) in tour:
        if i == current and j not in visited:
            ordered_tour.append(j)
            visited.add(j)
            current = j
            break

# Add the depot city at the end to complete the tour
ordered_tour.append(0)

# Calculate costs
total_cost = sum(dist(ordered_tour[i], ordered_tour[i+1]) for i in range(len(ordered_tour)-1))
max_distance = max(dist(ordered_tour[i], ordered_tour[i+1]) for i in range(len(ordered_tour)-1))

# Display the final outputs
print("Tour:", ordered_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)